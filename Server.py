import json
import os
import subprocess
import time
from fileinput import filename
from http.client import IncompleteRead

import psutil
import requests
from requests.exceptions import ChunkedEncodingError, RequestException
from tqdm import tqdm

import FileHandler as fh



class Server:
    minecraft_servers = [] #用于存储可用的MinecraftServer实例 是类变量 还可以检测是否完成过MCES设置
    MCESServer = None #用于存储MCESServer实例

    def __init__(self,**kwargs):
        if kwargs.get("config_file") is not None:
            self.__dict__ = json.loads(open(kwargs.get("config_file")).read())
            if Server.MCESServer is None:
                Server.MCESServer = self
        else:
            if Server.MCESServer is None:
                #关闭进程重新启动时，需要创建一个新的实例
                self.ip = kwargs.get("ip")
                self.port = kwargs.get("port")
                self.username = kwargs.get("username")
                self.password = kwargs.get("password")
                self.minecraft_servers = kwargs.get("minecraft_servers") #存储定义的MinecraftServer服务器路径 #Servername:server_folder
                self.config_file = "Servers/MCES_config.json"
                if not self.ip.startswith("http://"):
                    self.ip = "http://" + self.ip
                json.dump(self.__dict__, open("Servers/MCES_config.json", "w")) #保存配置文件
                print("已经重新创建实例")
                Server.MCESServer = self
                #其他情况下，直接读取之前的实例并更新信息
            else:
                Server.MCESServer.ip = kwargs.get("ip")
                Server.MCESServer.port = kwargs.get("port")
                Server.MCESServer.username = kwargs.get("username")
                Server.MCESServer.password = kwargs.get("password")
                self.__dict__ = Server.MCESServer.__dict__
                print("已经更新实例")
                json.dump(self.__dict__, open("Servers/MCES_config.json", "w"))  # 保存配置文件

                #读取配置文件



    def add_game_server(self, server_folder):
        self.minecraft_servers.append(server_folder)
        print(self.__dict__)
        json.dump(self.__dict__, open("Servers/MCES_config.json", "w"))


    def remove_game_server(self, server_folder):
        self.minecraft_servers.remove(server_folder)

    def get_available_servers(self):
        return self.minecraft_servers

    class FileNotFoundError(Exception):
        def __str__(self):
            return "FileNotFoundError"

    class ServerConnectionError(Exception):
        def __str__(self):
            return "ServerConnectionError"

    def download(self,filepath):
        filename = os.path.basename(filepath)
        dir = os.path.dirname(filepath)
        params = {'filepath': filepath}
        retries = 3
        success = False
        for retry in range(1, retries + 1):
            try:
                response = requests.get(f'{self.ip}:{self.port}/download', params=params, auth=(self.username, self.password), stream=True,
                                        timeout=30)
                if response.status_code == 200:
                    if os.path.exists(dir) is False:
                        os.makedirs(dir)
                    with open(filepath, 'wb') as file:
                        for chunk in response.iter_content(chunk_size=8192):
                            if chunk:
                                file.write(chunk)
                    success = True
                    print(f'{filename}文件下载成功！')
                    break  # Exit the loop on successful download
                else: # Retry on 404 response

                    print(f'{filename}文件未找到，但成功连接了服务器！')
                    raise Server.FileNotFoundError

            except (ChunkedEncodingError, IncompleteRead, RequestException) as e:
                print(f'下载异常，尝试重新下载（第 {retry} 次）', str(e))

        if not success:
            print('下载失败！请稍后重试。')
            raise Server.ServerConnectionError

    def upload(self, filepath):
        dir = os.path.dirname(filepath)
        filename = os.path.basename(filepath)

        with open(filepath, 'rb') as file:
            files = {'file': file}
            data = {'directory': dir}
            print(files)
            response = requests.post(f'{self.ip}:{self.port}/upload', auth=(self.username, self.password), files=files, data= data, stream=True)
        if response.status_code == 200:
            print(f'{filename}文件上传成功！')
        else:
            print(f'{filename}上传失败！')
            raise Server.ServerConnectionError





class frpClient:

    def __init__(self):
        self.client_status = "stopped"
        self.process = None
        self.stop()

    def start(self):
        self.client_status = "running"
        self.process = subprocess.Popen("frpc.exe -c frpc.toml", cwd="frp", shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)

    def stop(self):
        if self.process is not None:
            self.process.terminate()  # Attempt to terminate the process

            for proc in psutil.process_iter(['pid', 'name']):
                if proc.info['name'] == 'frpc.exe':
                    proc.kill()
        self.client_status = "stopped"


    def get_status(self):
        return self.client_status



class MinecraftServer:

    def __init__(self, **kwargs):
        if kwargs.get("config_file") is not None:
            self.__dict__ = json.loads(open(kwargs.get("config_file")).read())
        else:
            self.server_folder = kwargs.get("server_folder")
            self.folders_to_sync = kwargs.get("folders_to_sync")
            self.server_core = kwargs.get("server_core")
            self.server_memory = kwargs.get("server_memory") # xG x is number
            self.server_process = None
            self.server_status = "stopped"
            self.start_command = f"java -Xmx{self.server_memory} -jar {self.server_core}"
            self.server_name = self.server_folder.split("/")[-1]
            if os.path.exists(self.server_folder + "/MCES_configs") is False:
                os.mkdir(self.server_folder + "/MCES_configs/")

    def start_minecraft_server(self):
        mc_process = subprocess.Popen(self.start_command, cwd=self.server_folder, shell=True, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
        print("Minecraft Server started"+self.start_command)
        self.server_process = mc_process
        self.server_status = "running"

    def stop_minecraft_server(self):
        #TODO UI重新初始化的时候会出现问题，因为MC_Server的实例会被重新创建，但是MinecraftServer这个进程不会被绑定在新的实例上
        self.server_process.communicate(input="stop\n")
        self.server_status = "stopped"
        self.server_process = None

    # def add_server(self, server):
    #     self.server = server #添加服务器Server类 实现文件上传下载的实例


    def save_config(self):
        open(self.server_folder + "/MCES_configs/server_config.json", "w").write(json.dumps(self.__dict__))
        print("配置文件已经保存"+self.server_folder + "/MCES_configs/server_config.json")

    # def update_Server_files(self,update_list): #先这么放着，写到前端再说
    #     for file in update_list:
    #         Server.MCESServer.upload(file)
    #
    # def update_local_files(self,update_list): #先这么放着，写到前端再说
    #     for file in update_list:
    #         Server.MCESServer.download(file)

    def update_local_list(self): #更新本地的文件
        all_md5 = {}  # local md5
        for folder in self.folders_to_sync:
            all_md5.update(fh.get_all_files_md5(self.server_folder + "/" + folder))
        # download md5 from server
        # Server.MCESServer.download(self.server_folder + "/MCES_configs/server_md5.json") 迁移到前端完成
        server_md5 = json.loads(open(self.server_folder + "/MCES_configs/server_md5.json").read())
        update_list = []
        for k, v in server_md5.items():
            if all_md5.get(k) is None or server_md5.get(k) != all_md5.get(k):
                update_list.append(k)
        return update_list

    def update_server_list(self): #更新服务器的文件
        all_md5 = {}  # local md5
        for folder in self.folders_to_sync:
            all_md5.update(fh.get_all_files_md5(self.server_folder + "/" + folder))
        # download md5 from server
        init = False
        try :
            Server.MCESServer.download(self.server_folder + "/MCES_configs/server_md5.json")
        except Server.FileNotFoundError:
            print("服务器文件未找到")
            init = True

        if not init: #奇怪的变量名，如果不是第一次运行
            Server.MCESServer.download(self.server_folder + "/MCES_configs/server_md5.json")
            server_md5 = json.loads(open(self.server_folder + "/MCES_configs/server_md5.json").read())
        else:#在服务器全新的时候使用
            server_md5 = {}

        update_list = []
        json.dump(all_md5, open(self.server_folder + "/MCES_configs/server_md5.json", "w"))
        #在前端处处理异常
        #这里不应该进行下面的句子，否则可能出现文件同步失败而服务器被更新的问题
        #Server.MCESServer.upload(self.server_folder + "/MCES_configs/server_md5.json")#upload md5 to server


        for k, v in all_md5.items():
            if server_md5.get(k) is None or server_md5.get(k) != all_md5.get(k):
                update_list.append(k)
        return update_list

    def use_file_lock(self):
        username = Server.MCESServer.username
        time_now = time.time()
        open(self.server_folder + "/MCES_configs/file_lock.json", "w").write(json.dumps({"username": username, "time": time_now}))
        Server.MCESServer.upload(self.server_folder + "/MCES_configs/file_lock.json")
        os.remove(self.server_folder + "/MCES_configs/file_lock.json")

    def release_file_lock(self):
        username = ""
        time_now = ""
        open(self.server_folder + "/MCES_configs/file_lock.json", "w").write(
            json.dumps({"username": username, "time": time_now}))
        Server.MCESServer.upload(self.server_folder + "/MCES_configs/file_lock.json")
        os.remove(self.server_folder + "/MCES_configs/file_lock.json")


    def check_file_lock(self):
        try:
            Server.MCESServer.download(self.server_folder + "/MCES_configs/file_lock.json")
        except Server.FileNotFoundError:
            return {"username": "", "time": ""}
        lock = json.loads(open(self.server_folder + "/MCES_configs/file_lock.json").read())
        os.remove(self.server_folder + "/MCES_configs/file_lock.json")
        return lock

    def update_local_last_update_time(self): #生成上次更新时间
        open(self.server_folder + "/MCES_configs/last_sync_time_local.json", "w").write(json.dumps({"time": time.time()}))
        #Server.MCESServer.upload(self.server_folder + "/MCES_configs/last_sync_time.json")

    def update_server_update_time(self): #修改服务器上次更新时间
        # if os.path.exists(self.server_folder + "/MCES_configs/last_sync_time_local.json"):
        #     time_local = json.loads(open(self.server_folder + "/MCES_configs/last_sync_time_local.json").read())["time"]
        # else:
        #     time_local = 0
        open(self.server_folder + "/MCES_configs/last_sync_time.json", "w").write(json.dumps({"time": time.time()}))
        Server.MCESServer.upload(self.server_folder + "/MCES_configs/last_sync_time.json")

    def check_if_safe_to_update(self):
        try:
            Server.MCESServer.download(self.server_folder + "/MCES_configs/last_sync_time.json")
            time = json.loads(open(self.server_folder + "/MCES_configs/last_sync_time.json").read())
            server_time = time["time"]

        except Server.FileNotFoundError:
            server_time = 0

        local_time = json.loads(open(self.server_folder + "/MCES_configs/last_sync_time_local.json").read())["time"]
        if server_time > local_time:
            return False
        else:
            return True




















# args = {"server_folder": "Servers/Minecraft_Server_Test",
#         "folders_to_sync": ["world", "CustomWidgets","world_nether","world_the_end"],
#         "server_core": "paper-1.18.2-388.jar",
#         "server_memory": "2G",
#         }
# test_mc = MinecraftServer(**args)
#
#
# args = {"ip": "127.0.0.1",
#         "port": 5000,
#         "username": "admin",
#         "password": "5f4dcc3b5aa765d61d8327deb882cf99",
#         }
# test_server = Server(**args)
# test_server.download("Servers/Minecraft_Server_Test/MCES_configs/server_md5.json")
# test_mc.add_server(test_server)
# test_server.add_game_server(test_mc)
#
# updates = test_mc.update_local_list()
# test_mc.update_local_files(updates)
# frpv = frpClient()
# frpv.start()
# time.sleep(5)
# frpv.stop()

