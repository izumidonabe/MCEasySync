import hashlib
#import lzma
import os
import shutil
import requests
from requests.exceptions import ChunkedEncodingError
from requests.exceptions import RequestException
from tqdm import tqdm
from urllib3.exceptions import IncompleteRead

server_host = "null"
server_port = "null"
server_url = "null"
password = "null"
username = "null"


def get_server_address(usname, passwd, server_address, port):
    global server_host, server_port, server_url
    server_host = server_address
    server_port = int(port)
    server_url = f'http://{server_host}:{server_port}'  # 服务器地址
    global username
    global password
    username = usname
    password = passwd
    hash = hashlib.md5()
    hash.update(password.encode('utf-8'))
    password = hash.hexdigest()
    print(server_url)
    print(f"登录用户名{username}")
    print(f"登录密码{password}")  # delete


def compress_directory(path, destination_file):  # 方法已弃用
    with lzma.open(destination_file, "wb") as f:
        for dirpath, dirnames, filenames in os.walk(path):
            for filename in filenames:
                filepath = os.path.join(dirpath, filename)
                with open(filepath, "rb") as infile:
                    f.write(infile.read())



#最早计划将整个文件夹打包进行上传，但考虑到服务器上传带宽可能受限，已经弃用
'''
def decompress_file(compressed_file, decompressed_file):
    with lzma.open(compressed_file, "rb") as f:
        with open(decompressed_file, "wb") as outfile:
            outfile.write(f.read())'''


def calculate_file_md5(file_path):
    md5_hash = hashlib.md5()
    with open(file_path, "rb") as f:
        # 遍历文件的每个块并计算散列值
        for chunk in iter(lambda: f.read(4096), b""):
            md5_hash.update(chunk)
    return md5_hash.hexdigest()


# 服务器配置


def upload(filename):
    file_size = os.path.getsize(filename)
    with open(filename, 'rb') as file:
        with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
            files = {'file': file}
            response = requests.post(f'{server_url}/upload', auth=(username, password), files=files, stream=True)
            for chunk in response.iter_content(chunk_size=8192):
                if chunk:
                    pbar.update(len(chunk))

    if response.status_code == 200:
        print(f'{filename}文件上传成功！')
    else:
        print(f'{filename}上传失败！')


# 下载文件
max_retries = 3


# 下载文件
def download(filename):
    params = {'filename': filename}
    retries = 3
    success = False

    for retry in range(1, retries + 1):
        try:
            response = requests.get(f'{server_url}/download', params=params, auth=(username, password), stream=True,
                                    timeout=30)

            if response.status_code == 200:
                file_size = int(response.headers.get('Content-Length', 0))

                with open(filename, 'wb') as file:
                    with tqdm(total=file_size, unit='B', unit_scale=True) as pbar:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                file.write(chunk)
                                pbar.update(len(chunk))

                success = True
                print(f'{filename}文件下载成功！')
                break  # Exit the loop on successful download
            else:
                print(f'{filename}文件下载失败！')

        except (ChunkedEncodingError, IncompleteRead, RequestException) as e:
            print(f'下载异常，尝试重新下载（第 {retry} 次）', str(e))

    if not success:
        print('下载失败！请稍后重试。')


def world_format(save):
    save_1 = f"server/{save}"
    file_paths = []

    # 遍历目录下的所有文件和子目录
    for root, dirs, files in os.walk(save_1):
        for file in files:
            # 获取文件的相对路径
            file_path = os.path.join(root, file)
            file_paths.append(file_path)

    for i, item in enumerate(file_paths):
        file_paths[i] = item.replace("\\", "/")
    for i, item in enumerate(file_paths):
        old_file_name = file_paths[i]
        new_file_name = old_file_name.replace("/", "~")  # 浪号肯定没有人用吧
        new_file_name = new_file_name.replace(" ", "")  # 删除空格
        if not os.path.exists(f"{save}_formatted"):
            os.mkdir(f"{save}_formatted")
        new_file_name = f"{save}_formatted/" + new_file_name
        shutil.copyfile(f"{old_file_name}", f"{new_file_name}")
        os.remove(old_file_name)


donotdoit = []  # 用于固定文件，应该添加一个读取逻辑，——无需在检测到md5差异后上传


def md5_update_server(save):  # 检测并更新服务端md5不同的文件 在游戏保存以后执行
    file_names = os.listdir(save)
    md5_dics = {}
    global donotdoit
    if f"{save}_md5_new.txt" not in donotdoit:
        donotdoit = donotdoit + [f"{save}_md5_new.txt"]  # 抽象变量名 这个里边放不是存档文件的其他文件
    if f"{save}_md5_old.txt" not in donotdoit:
        donotdoit = donotdoit + [f"{save}_md5_old.txt"]
    if f"donotdoit.txt" not in donotdoit:
        donotdoit = donotdoit + [f"donotdoit.txt"]
    for i, item in enumerate(file_names):
        if item not in donotdoit:
            md5 = calculate_file_md5(save + "/" + item)
            md5_dics[item] = md5
    try:
        download(f"{save}_md5_old.txt")
        shutil.copyfile(f"{save}_md5_old.txt", f"{save}/{save}_md5_old.txt")
    except:
        print("服务端md5数据下载失败")
    md5_dics_old = {}
    with open(save + f"/{save}_md5_old.txt") as md5_old:
        md5_old_lists = md5_old.readlines()
        for i, item in enumerate(md5_old_lists):
            md5_dics_old[item.split(" ")[0]] = item.split(" ")[1].split("\n")[0]
        md5_old.close()
    for keys in md5_dics:
        if keys not in md5_dics_old or md5_dics[keys] != md5_dics_old[keys]:
            print("发现文件更改，正在上传" + keys)
            upload(f"{save}/" + keys)

    with open(save + f"/{save}_md5_new.txt", "w") as md5_new:
        data = []
        for keys in md5_dics:
            data.append(keys + " " + md5_dics[keys] + "\n")
        md5_new.writelines(data)
        md5_new.close()
    os.remove(save + f"/{save}_md5_old.txt")
    os.rename(save + f"/{save}_md5_new.txt", save + f"/{save}_md5_old.txt")
    try:
        print("正在尝试上传新的md5")
        upload(save + f"/{save}_md5_old.txt")
    except:
        print("md5上传失败")
    with open("donotdoit.txt", "w") as donotdoitfile:
        data = []
        for item in donotdoit:
            data.append(item + "\n")
        donotdoitfile.writelines(data)
        donotdoitfile.close()
    try:
        upload("donotdoit.txt")
    except:
        print("跳过文件上传失败")


def md5_download_server(save):  # 在游戏开始之前执行
    global donotdoit
    try:
        download("donotdoit.txt")
        # shutil.copyfile("donotdoit.txt", save + "/donotdoit.txt")
    except:
        print("跳过文件下载失败")
    with open("donotdoit.txt") as donotdoitfile:
        donotdoit_new = donotdoitfile.readlines()
        for i, item in enumerate(donotdoit_new):
            donotdoit.append(donotdoit_new[i].split(" ")[0].split("\n")[0])
    if not os.path.exists(save):
        os.mkdir(save)
    file_names = os.listdir(save)
    md5_dics = {}
    if f"{save}_md5_new.txt" not in donotdoit:
        donotdoit = donotdoit + [f"{save}_md5_new.txt"]  # 抽象变量名 这个里边放不是存档文件的其他文件
    if f"{save}_md5_old.txt" not in donotdoit:
        donotdoit = donotdoit + [f"{save}_md5_old.txt"]  # 抽象变量名 这个里边放不是存档文件的其他文件
    if f"donotdoit.txt" not in donotdoit:
        donotdoit = donotdoit + [f"donotdoit.txt"]
    for i, item in enumerate(file_names):
        if item not in donotdoit:
            md5 = calculate_file_md5(save + "/" + item)
            md5_dics[item] = md5
    try:
        print("正在从服务器下载md5数据")
        download(f"{save}_md5_old.txt")
        shutil.move(f"{save}_md5_old.txt", f"{save}/{save}_md5_old.txt")
    except:
        print("服务端md5数据下载失败")
        exit()
    md5_dics_old = {}
    with open(save + f"/{save}_md5_old.txt") as md5_old:
        md5_old_lists = md5_old.readlines()
        for i, item in enumerate(md5_old_lists):
            md5_dics_old[item.split(" ")[0]] = item.split(" ")[1].split("\n")[0]
            md5_old.close()
    for keys in md5_dics_old:
        if keys in md5_dics_old and keys not in md5_dics:
            print("发现服务器文件更改，正在下载" + keys)
            download(keys)
            shutil.move(keys, f"{save}/{keys}")
        if keys in md5_dics_old and keys in md5_dics:
            if md5_dics[keys] != md5_dics_old[keys]:
                print("发现服务器文件更改，正在下载" + keys)
                download(keys)
                shutil.move(keys, f"{save}/{keys}")


def world_deformat(save):
    print("正在将世界文件恢复至标准格式")
    file_names = os.listdir(save)
    for i, item in enumerate(file_names):
        if item.startswith("server~"):
            new_file_name = item.replace("~", "/")
            old_file_name = item
            print(f"{save}/{old_file_name}")
            if not os.path.exists(new_file_name.rsplit("/", 1)[0]):
                os.makedirs(new_file_name.rsplit("/", 1)[0])
            shutil.copyfile(f"{save}/{old_file_name}", new_file_name)
            os.remove(f"{save}/{old_file_name}")
