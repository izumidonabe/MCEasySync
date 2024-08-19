#本文件用于实现多种文件方法
import os
import shutil
import hashlib


def get_file_md5(file_path):
    with open(file_path, 'rb') as f:
        md5obj = hashlib.md5()
        md5obj.update(f.read())
        hash = md5obj.hexdigest()
    return hash


def get_all_files_md5(folder):  #获取文件夹下所有文件的md5值 走相对路径
    files_md5 = {}
    for root, dirs, file in os.walk(folder):
        for f in file:
            file_path = os.path.join(root, f)
            files_md5[file_path] = get_file_md5(file_path)
    return files_md5


  #锁定文件
