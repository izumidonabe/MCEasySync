import os
import subprocess
import threading
import time

import psutil


class minecraft_server():

    def __init__(self):
        self.minecraft_process = None

    def start(self):
        global minecraft_process

        os.chdir("server/")

        available_memory = psutil.virtual_memory().available  # 根据内存修改启动参数
        if available_memory >= 8 * 1024 * 1024 * 1024:
            minecraft_memory = "4G"
        elif available_memory >= 4 * 1024 * 1024 * 1024:
            minecraft_memory = "3G"
        else:
            minecraft_memory = "2G"

        # 启动参数
        minecraft_args = ["java", f"-Xmx{minecraft_memory}", "-Xms1G", "-jar"]
        minecraft_core = "server.jar"
        minecraft_args.append(minecraft_core)
        # 创建子进程
        self.minecraft_process = subprocess.Popen(minecraft_args, stdin=subprocess.PIPE, stdout=subprocess.PIPE,
                                                  stderr=subprocess.STDOUT)

        # 读取Minecraft服务器输出的子线程函数
        def read_output(output_stream):
            for output_line in iter(output_stream.readline, b''):
                print(output_line.decode('iso-8859-1').strip())

        # 创建子线程读取Minecraft服务器输出
        output_thread = threading.Thread(target=read_output, args=(self.minecraft_process.stdout,))
        output_thread.start()

    def save_all(self):
        command = "save-all"
        self.minecraft_process.stdin.write(command.encode('iso-8859-1') + b'\n')
        self.minecraft_process.stdin.flush()

    def stop(self):
        command = "stop"
        self.minecraft_process.stdin.write(command.encode('iso-8859-1') + b'\n')
        self.minecraft_process.stdin.flush()
        self.minecraft_process.wait()
        time.sleep(20)
