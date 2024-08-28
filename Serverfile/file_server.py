import time
import logging
from functools import wraps

from flask import Flask, request, jsonify, send_file
import os
from tqdm import tqdm
import sys
from gevent import pywsgi

app = Flask(__name__)
logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')

handler = logging.FileHandler("log.txt")
handler.setLevel(logging.DEBUG)
handler.setFormatter(formatter)

logger.addHandler(handler)
# 预设的用户名和密码

users = {"admin": "5f4dcc3b5aa765d61d8327deb882cf99", 
"test_user": "5f4dcc3b5aa765d61d8327deb882cf99",
}


def check_auth(user, passwd):
    print(user, passwd)
    try:

        if passwd == users[f"{user}"]:
            return True
        else:
            return False
    except:
        return False


# 登录验证装饰器
def login_required(f):
    @wraps(f)
    def decorated(*args, **kwargs):
        auth = request.authorization
        try:
            print(auth.username, auth.password)
            app.logger.info(str(auth.username)+str(auth.password)+"IS TRYING")
        except:
            return jsonify({'message': '登录验证失败！'}), 401
        if not auth or not check_auth(auth.username, auth.password):
            return jsonify({'message': '登录验证失败！'}), 401
        return f(*args, **kwargs)

    return decorated


# 验证用户名和密码是否匹配

# 记录每个请求
@app.before_request
def log_request_info():
    logger.info(f"{request.remote_addr} - {request.method} {request.full_path}")


@app.route('/upload', methods=['POST'])
@login_required
def upload():
    file = request.files['file']
    directory = request.form.get('directory')
    #希望上传的文件夹不包含..和/，防止上传到其他目录
    if directory.find('..') != -1:
        return jsonify({'message': '文件上传失败！'}), 400
    if directory.startswith('/'):
        return jsonify({'message': '文件上传失败！'}), 400
    if directory.startswith('\\'):
        return jsonify({'message': '文件上传失败！'}), 400
    if file and directory:
        # 保存上传的文件到指定目录
        upload_folder = os.path.join(app.config['UPLOAD_FOLDER'], directory)
       
        upload_folder = upload_folder.replace("\\","/")
        upload_folder = os.path.normpath(upload_folder)
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        file_path = os.path.join(upload_folder, file.filename)
        print(file_path)
        struct_time = time.localtime()
        print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))
        with open(file_path, 'wb') as f:
            while True:
                buff = file.read(8192)
                if not buff:
                    break
                f.write(buff)

        return jsonify({'message': '文件上传成功！'}), 200
    else:
        return jsonify({'message': '文件上传失败！'}), 400


from flask import send_file, make_response

#TODO 全平台路径处理
@app.route('/download', methods=['GET'])
@login_required
def download():
    filepath = request.args.get('filepath')
    if filepath.find('..') != -1:
        return jsonify({'message': '文件下载失败！'}), 400
    if filepath.startswith('/'):
        return jsonify({'message': '文件下载失败！'}), 400
    if filepath.startswith('\\'):
        return jsonify({'message': '文件下载失败！'}), 400    

    if filepath:
        
        
        struct_time = time.localtime()
        print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))
        file_path = os.path.join(app.config['UPLOAD_FOLDER'], filepath)
        file_path = file_path.replace("\\","/")
        file_path = os.path.normpath(file_path)
        print(file_path)
        print(os.path.exists(file_path))
        print(os.getcwd())

        if os.path.exists(file_path):
            file_size = os.path.getsize(file_path)
            download_filename = os.path.basename(file_path)
            response = make_response()
            response.headers['Content-Disposition'] = f'attachment; filename={download_filename}'
            response.headers['Content-Type'] = 'application/octet-stream'
            response.headers['Content-Length'] = str(file_size)
            response.headers['Cache-Control'] = 'no-cache'
            with open(file_path, 'rb') as file:
                response.data = file.read()
    
            return response
        else:
            return jsonify({'message': '文件未找到！'}), 404
    else:
        return jsonify({'message': '文件下载失败！'}), 400


if __name__ == '__main__':
    # 上传文件保存的目录
    upload_folder = 'uploads'
    if not os.path.exists(upload_folder):
        os.makedirs(upload_folder)
    app.config['UPLOAD_FOLDER'] = upload_folder
    app.debug = True
    #app.run(debug=True)
    server = pywsgi.WSGIServer(('0.0.0.0',5000),app)
    server.serve_forever()
