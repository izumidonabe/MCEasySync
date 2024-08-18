import json

from PySide2.QtWidgets import QWidget

from Server import frpClient, MinecraftServer, Server
from ui.mc_Server_manage_Ui import Ui_McServer_manage_UI


class mcserver_manage_Ui(QWidget,Ui_McServer_manage_UI):
    def __init__(self):
        super(mcserver_manage_Ui, self).__init__()
        self.setupUi(self)
        self.FRPC = frpClient()
        self.MCSERVER = None
        self.MCES_SERVER = None

    def reinitailze(self,server_name):
        self.FRPC = frpClient()
        mcserver_config = "Servers/"+server_name+"/MCES_configs/MCES_config.json"
        kwargs = {"config_file":mcserver_config}
        self.MCSERVER = MinecraftServer(**kwargs)
        self.MCES_SERVER = Server.MCESServer

        self.startfrpButton.clicked.connect(self.start_frp)

    def start_frp(self):
        self.FRPC.start()

    def stop_frp(self):
        self.FRPC.stop()
