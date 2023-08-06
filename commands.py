import os.path
import time

import minecraft_start
from minecraft_save import *

mcserver = minecraft_start.minecraft_server()
# 这个文件下放所有命令及实现
start = 0
global login
username = ""
password = ""

server_host = ""

login_status = False


def start_local():
    global start, login_status
    print(login_status)
    if login_status:
        if start == 0:

            print("正在尝试开启本地服务器")
            try:
                md5_download_server("world_formatted")
                world_deformat("world_formatted")
            except:
                print("world世界下载失败，但可能并不是个问题")
            try:
                md5_download_server("world_nether_formatted")
                world_deformat("world_nether_formatted")
            except:
                print("world_nether世界下载失败，但可能并不是个问题")
            try:
                md5_download_server("world_end_formatted")
                world_deformat("world_end_formatted")
            except:
                print("world_end世界下载失败，但可能并不是个问题")
            if os.path.exists("server/plugins"):
                try:
                    md5_download_server("plugins_formatted")
                    world_deformat("plugins_formatted")
                except:
                    print("plugin文件夹下载失败，这是一个严重的问题，请联系服务器管理员")
            if os.path.exists("server/mods"):
                try:
                    md5_download_server("mods_formatted")
                    world_deformat("mods_formatted")
                except:
                    print("plugin文件夹下载失败，这是一个严重的问题，请联系服务器管理员")
            time.sleep(1)
            print("文件同步完成，正在启动服务端")
            start = 1

            mcserver.start()
        else:
            print("服务器已经在运行了")
    else:
        print("未登录，请输入login来尝试登录")


def stop_local():
    global start
    if login_status:
        if start != 0:
            print("正在尝试关闭本地服务器，请耐心等待文件同步")
            mcserver.save_all()
            mcserver.stop()
            mcserver.minecraft_process.wait()
            os.chdir("..")
            start = 0
        else:
            print("服务器没有运行，请开启服务器吧")
    else:
        print("未登录")


def sync():
    if login_status:
        if start == 0:
            print(os.getcwd())

            world_format("world")
            md5_update_server("world_formatted")

            print("world世界上传失败，但可能不是个问题")
            try:
                world_format("world_nether")
                md5_update_server("world_nether_formatted")
            except:
                print("world_nether世界上传失败，但可能不是个问题")
            try:
                world_format("world_end")
                md5_update_server("world_end_formatted")
            except:
                print("world_end世界上传失败，但可能不是个问题")
            if os.path.exists("server/plugins"):
                world_format("plugins")
                md5_update_server("plugins_formatted")

                print("plugin文件夹下载失败，这是一个严重的问题，请联系服务器管理员")
            if os.path.exists("server/mods"):
                try:
                    world_format("mods")
                    md5_update_server("mods_formatted")
                except:
                    print("mods文件夹下载失败，这是一个严重的问题，请联系服务器管理员")
            print("文件上传完成")
        else:
            print("服务器正在运行，请关闭后再试")
    else:
        print("未登录")


def client_exit():
    if start == 0:
        print("客户端即将在114514微秒后关闭")
        time.sleep(0.114514)
        exit()
    if start != 0:
        print("服务器还在运行中呢，请输入stop_local关闭服务器后再试")


def register():
    print("请联系管理员进行注册")


def user_login(usname, passwd, server_address, port):
    get_server_address(usname, passwd, server_address, port)
    global login_status
    login_status = True


def file_lock_open(usname):
    if login_status:
        with open("filelock.txt") as filelock:
            data = []
            data.append(usname)
            filelock.seek(0)
            filelock.truncate()
            filelock.writeline(data)
            filelock.close()
        upload("filelock.txt")
    else:
        print("未登录")

def check_file_lock():
    if login_status:
        download("filelock.txt")
        if os.path.getsize("filelock.txt"):
            return True
        else:
            return False
    print("未登录")
    return False


def file_lock_close(usname):
    if login_status:
        download("filelock.txt")
        with open("filelock.txt") as filelock:
            if filelock.readline(0) != usname:
                print("你不能主动关闭别人开启的服务器")
                print(usname)
            else:
                filelock.seek(0)
                filelock.truncate()
                filelock.close()
                upload("filelock.txt")
    print("未登录")