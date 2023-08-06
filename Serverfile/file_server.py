import time
from functools import wraps

from flask import Flask, request, jsonify, send_file
import os
from tqdm import tqdm
import sys

# 定义输出重定向的目标文件
output_file = "info.txt"

# 保存旧的标准输出对象
old_stdout = sys.stdout

# 打开文件，以追加模式写入
file = open(output_file, "a")

# 重定向标准输出到文件
sys.stdout = file
try:
    app = Flask(__name__)

    # 预设的用户名和密码

    users = {"admin": "5f4dcc3b5aa765d61d8327deb882cf99", "test_user": "5f4dcc3b5aa765d61d8327deb882cf99"}


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
            #print(auth.username, auth.password)
            if not auth or not check_auth(auth.username, auth.password):
                return jsonify({'message': '登录验证失败！'}), 401
            return f(*args, **kwargs)

        return decorated


    # 验证用户名和密码是否匹配


    @app.route('/upload', methods=['POST'])
    @login_required
    def upload():
        file = request.files['file']
        if file:
            # 保存上传的文件到指定目录
            upload_folder = app.config.get('UPLOAD_FOLDER')
            if not os.path.exists(upload_folder):
                os.makedirs(upload_folder)
            #filename = secure_filename(file.filename)
            print(file.filename)
            struct_time = time.localtime()
            print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))
            filename=file.filename.replace("/","_")
            file_path = os.path.join(upload_folder, filename)

            # 获取文件大小
            file_size = int(request.headers.get('Content-Length'))

            with open(file_path, 'wb') as f:
                # 使用tqdm显示上传进度条
                with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
                    while True:
                        buff = file.read(8192)
                        if not buff:
                            break
                        f.write(buff)
                        pbar.update(len(buff))

            return jsonify({'message': '文件上传成功！'}), 200
        else:
            return jsonify({'message': '文件上传失败！'}), 400


    from flask import send_file, make_response


    @app.route('/download', methods=['GET'])
    @login_required
    def download():
        filename = request.args.get('filename')

        if filename:
            print(filename)
            struct_time = time.localtime()
            print(time.strftime("%Y-%m-%d %H:%M:%S", struct_time))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], filename)

            if os.path.exists(file_path):
                file_size = os.path.getsize(file_path)
                #download_filename = secure_filename(filename)
                download_filename = filename.replace("/","_")

                response = make_response()
                response.headers['Content-Disposition'] = f'attachment; filename={download_filename}'
                response.headers['Content-Type'] = 'application/octet-stream'
                response.headers['Content-Length'] = str(file_size)
                response.headers['Cache-Control'] = 'no-cache'

                with open(file_path, 'rb') as file:
                    response.data = file.read()

                return response
            else:
                return jsonify({'message': '文件不存在！'}), 404
        else:
            return jsonify({'message': '文件下载失败！'})


    if __name__ == '__main__':
        # 上传文件保存的目录
        upload_folder = 'uploads'
        if not os.path.exists(upload_folder):
            os.makedirs(upload_folder)
        app.config['UPLOAD_FOLDER'] = upload_folder
        app.run(debug=True)
finally:
    # 恢复原来的标准输出对象
    sys.stdout = old_stdout

    # 关闭文件
    file.close()