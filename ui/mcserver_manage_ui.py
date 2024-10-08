import json
from time import ctime

import winsound
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QWidget
from qfluentwidgets import Flyout, InfoBarIcon, FlyoutAnimationType

from Server import frpClient, MinecraftServer, Server
from ui.mc_Server_manage_Ui import Ui_McServer_manage_UI

class DownloadThread(QThread):
    progress = Signal(int)
    error = Signal(str)
    finished = Signal()

    def __init__(self, files, server):
        super().__init__()
        self.files = files
        self.server = server

    def run(self):
        try:
            for i, file in enumerate(self.files):
                self.server.download(file)
                self.progress.emit(i + 1)
            self.finished.emit()
        except Server.ServerConnectionError as e:
            self.error.emit(str(e))

class UploadThread(QThread):
    progress = Signal(int)
    error = Signal(str)
    finished = Signal()

    def __init__(self, files, server):
        super().__init__()
        self.files = files
        self.server = server

    def run(self):
        try:
            for i, file in enumerate(self.files):
                self.server.upload(file)
                self.progress.emit(i + 1)
            self.finished.emit()
        except Server.ServerConnectionError as e:
            self.error.emit(str(e))


class mcserver_manage_Ui(QWidget,Ui_McServer_manage_UI):
    def __init__(self):
        super(mcserver_manage_Ui, self).__init__()
        self.setupUi(self)
        self.FRPC = frpClient()
        self.MCSERVER = None
        self.MCES_SERVER = None
        self.upload_thread = None
        self.download_thread = None

    def reinitailze(self,server_name):
        self.FRPC = frpClient()
        mcserver_config = "Servers/"+server_name+"/MCES_configs/server_config.json"
        kwargs = {"config_file":mcserver_config}
        self.MCSERVER = MinecraftServer(**kwargs)
        self.MCES_SERVER = Server(**json.load(open("Servers/MCES_config.json")))

        self.frp_server_status_title.setText("stopped")

        self.startfrpButton.clicked.connect(self.start_frp)
        self.stopfrpButton.clicked.connect(self.stop_frp)

        self.startmcButton.clicked.connect(self.start_minecraft_server)
        self.stopmcButton.clicked.connect(self.stop_minecraft_server)
        print("reinitailze")
        self.sync_start_button.clicked.connect(lambda:self.sync_files())







    def start_frp(self):
        print("start frp")
        self.FRPC.start()
        self.frp_server_status_title.setText(self.FRPC.get_status())

    def stop_frp(self):
        print("stop frp")
        self.FRPC.stop()
        self.frp_server_status_title.setText(self.FRPC.get_status())

    def start_minecraft_server(self):
        #TODO 您是否忘了同步文件？
        try:
            if not self.MCSERVER.check_if_safe_to_update():
                self.raise_alert("错误","服务器上次同步的文件生成时间晚于本地文件，可认为服务器文件较新，请先同步文件再运行服务器")
                return 0
            lock = self.MCSERVER.check_file_lock()
            if lock["username"] == "":
                self.MCSERVER.use_file_lock()
            else:
                self.raise_alert("错误","文件锁已经被用户"+lock["username"]+"\n从时间"+ ctime(lock["time"]) +"开始占用\n"+"请联系他释放")
                return 0
        except Server.ServerConnectionError:
            self.raise_alert("错误","服务器连接出现问题，请重试")
            return 0
        self.MCSERVER.start_minecraft_server()
        self.mcserver_status_title.setText(self.MCSERVER.server_status)

    def stop_minecraft_server(self):
        try:
            self.MCSERVER.stop_minecraft_server()
        except :
            print("error")
        try:
            self.MCSERVER.release_file_lock()
        except Server.ServerConnectionError:
            self.raise_alert("错误","服务器连接出现问题，请重试")
            return 0
        self.MCSERVER.update_local_last_update_time()
        self.mcserver_status_title.setText(self.MCSERVER.server_status)
        self.raise_a_message("新消息","服务器已停止，别忘了同步文件哦")

    #TODO 优化文件时间检查，似乎有逻辑问题

    def sync_files(self):
        self.sync_process_bar.resume()
        chosen_index = self.choose_sync_mode_box.currentIndex() #0: 更新服务器文件 1: 更新本地
        #上传文件
        if chosen_index == 0:
            try:
                if not self.MCSERVER.check_if_safe_to_update():
                    self.raise_alert("错误","服务器上次同步的文件生成时间晚于本地文件，可认为服务器文件较新")
                    self.sync_process_bar.error()
                    return 0

                update_list = self.MCSERVER.update_server_list()
            except Server.ServerConnectionError:
                self.raise_alert("错误","服务器连接出现问题，请重试")
                self.sync_process_bar.error()
                return 0

            files_num = len(update_list)
            self.sync_process_bar.setRange(0,files_num)
            #接着开始尝试上传文件

            self.upload_thread = UploadThread(update_list, Server.MCESServer)
            self.upload_thread.progress.connect(lambda val :self.sync_process_bar.setVal(val))
            self.upload_thread.error.connect(lambda:self.raise_alert("错误","服务器连接出现问题，请重试"))
            self.upload_thread.error.connect(lambda:self.sync_process_bar.error())
            self.upload_thread.finished.connect(lambda:Server.MCESServer.upload(self.MCSERVER.server_folder + "/MCES_configs/server_md5.json"))
            self.upload_thread.finished.connect(lambda:self.MCSERVER.update_server_update_time())
            self.upload_thread.finished.connect(lambda:self.raise_a_message("新消息", "服务器更新完成"))
            self.upload_thread.start()



            # try:
            #     for file in update_list:
            #         Server.MCESServer.upload(file)
            #         self.sync_process_bar.setVal(self.sync_process_bar.getVal()+1)
            #     Server.MCESServer.upload(self.MCSERVER.server_folder + "/MCES_configs/server_md5.json")  # upload md5 to server
            #     self.MCSERVER.update_server_update_time() # update server update time
            # except Server.ServerConnectionError:
            #     self.raise_alert("错误","服务器连接出现问题，请重试")
            #     self.sync_process_bar.error()
            #     return 0
            #
            # self.raise_a_message("新消息","服务器更新完成")


        #下载文件
        else:

            try:
                Server.MCESServer.download(self.MCSERVER.server_folder + "/MCES_configs/server_md5.json")
            except Server.FileNotFoundError:
                self.raise_alert("错误","更新列表文件未找到，可能是服务器还未初始化")
                self.sync_process_bar.error()
                return 0
            except Server.ServerConnectionError:
                self.raise_alert("错误","服务器连接出现问题，请重试")
                self.sync_process_bar.error()
                return 0
            update_list = self.MCSERVER.update_local_list()
            files_num = len(update_list)
            self.sync_process_bar.setRange(0, files_num)

            self.download_thread = DownloadThread(update_list, Server.MCESServer)
            self.download_thread.progress.connect(lambda val: self.sync_process_bar.setVal(val))
            self.download_thread.error.connect(lambda: self.raise_alert("错误","服务器连接出现问题，请重试"))
            self.download_thread.error.connect(lambda: self.sync_process_bar.error())
            self.download_thread.finished.connect(lambda: self.MCSERVER.update_local_last_update_time())
            self.download_thread.finished.connect(lambda: self.raise_a_message("新消息", "本地更新完成"))
            self.download_thread.start()

            # try:
            #     for file in update_list:
            #         Server.MCESServer.download(file)
            #         self.sync_process_bar.setVal(self.sync_process_bar.getVal()+1)
            #
            # except Server.ServerConnectionError as e:
            #     self.raise_a_message("错误","服务器连接出现问题，请重试")
            #     return 0
            # self.raise_a_message("新消息", "本地更新完成")
            # self.MCSERVER.update_local_last_update_time()





    def raise_a_message(self,title,message):
        winsound.MessageBeep(winsound.MB_ICONEXCLAMATION)
        Flyout.create(
            icon=InfoBarIcon.SUCCESS,
            title=title,
            content=message,
            target=self.sync_start_button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP)

    def raise_alert(self,title,message):
        Flyout.create(
            icon=InfoBarIcon.ERROR,
            title=title,
            content=message,
            target=self.sync_start_button,
            parent=self,
            isClosable=True,
            aniType=FlyoutAnimationType.PULL_UP)





