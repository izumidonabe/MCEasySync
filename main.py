
from commands import *

import tkinter as tk


class StdRedirector:
    def __init__(self, text_widget):
        self.text_widget = text_widget

    def write(self, message):
        self.text_widget.insert(tk.END, message)
        self.text_widget.see(tk.END)  # 滚动到最新的内容


def login():
    username = entry_username.get()
    password = entry_password.get()
    server_address = entry_server_address.get()
    port = entry_port.get()
    # 在这里编写登录验证逻辑
    print(f"登录：用户名={username}，密码={password}，服务器地址={server_address}，端口号={port}")
    user_login(username, password, server_address, port)


def start_server():
    # 在这里编写启动本地服务器逻辑
    print(f"启动本地服务器：请确保你开启了frp服务，服务器地址=82.156.5.244，端口号=25565")
    start_local()


def stop_server():
    # 在这里编写关闭本地服务器逻辑
    print("关闭本地服务器")
    stop_local()


def file_sync():
    print("同步本地存档到云端")
    sync()

def fl_open():
    print("打开文件锁")
    file_lock_open(entry_username.get())

def fl_check():
    print("查询文件锁状态")
    if check_file_lock():
        print("无人为文件上锁")
    else:
        print("文件占用中")

def fl_stop():
    print("关闭文件锁")
    file_lock_close(entry_username.get())

root = tk.Tk()
root.title("MCEasySync v1.2.0")
# 创建按钮
btn_login = tk.Button(root, text="登录", command=login)
btn_start = tk.Button(root, text="启动本地服务器", command=start_server)
btn_stop = tk.Button(root, text="关闭本地服务器", command=stop_server)
btn_sync = tk.Button(root, text="上传本地服务器存档", command=file_sync)
btn_fl_open = tk.Button(root, text="打开文件锁", command=fl_open)
btn_fl_check = tk.Button(root, text="查询文件锁状态", command=fl_check)
btn_fl_stop = tk.Button(root, text="关闭文件锁", command=fl_stop)
# 创建标签和输入框
label_username = tk.Label(root, text="用户名：")
label_password = tk.Label(root, text="密码：")
label_server_address = tk.Label(root, text="服务器地址：")
label_port = tk.Label(root, text="端口号：")
entry_username = tk.Entry(root)
entry_password = tk.Entry(root, show='*')
entry_server_address = tk.Entry(root)
entry_port = tk.Entry(root)

# 创建控制台输出区域
# console_output = scrolledtext.ScrolledText(root, height=10, width=40)
# console_output.configure()  # 设置为只读状态

# sys.stdout = StdRedirector(console_output)  # 重定向标准输出
# sys.stderr = StdRedirector(console_output)  # 重定向标准错误输出

# 设置控件的布局
btn_login.pack(side=tk.LEFT)
btn_start.pack(side=tk.LEFT)
btn_stop.pack(side=tk.LEFT)
btn_sync.pack(side=tk.LEFT)
btn_fl_stop.pack(side=tk.LEFT)
btn_fl_check.pack(side=tk.LEFT)
btn_fl_open.pack(side=tk.LEFT)
label_username.pack()
entry_username.pack()
label_password.pack()
entry_password.pack()
label_server_address.pack()
entry_server_address.pack()
label_port.pack()
entry_port.pack()
# console_output.pack()

root.mainloop()
