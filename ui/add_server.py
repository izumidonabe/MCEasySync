from PySide6.QtCore import Signal
from PySide6.QtWidgets import QWidget

from Server import MinecraftServer, Server
from ui.add_server_ui import Ui_Add_Server_Ui


class add_server_Ui(QWidget,Ui_Add_Server_Ui):
    back_button_clicked_Sig = Signal()
    def __init__(self):
        super(add_server_Ui, self).__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.BackB_clicked)



    def BackB_clicked(self):
        print("BackB_clicked")
        server_folder = self.ServerName_edit.text()
        server_name = server_folder.split("/")[-1]
        folders_to_sync = self.Sync_Folders_edit.text()
        folders_to_sync = eval(folders_to_sync)
        server_core = self.Server_Core_dir_edit.text()
        server_memory = self.MemoryEdit.text()
        kwargs = {"server_folder": server_folder, "folders_to_sync": folders_to_sync, "server_core": server_core,
                  "server_memory": server_memory}
        mcserver = MinecraftServer(**kwargs)
        mcserver.save_config()

        if Server.MCESServer is None:
            kwargs = {"config_file": "Servers/MCES_config.json"}
            Server.MCESServer = Server(**kwargs)
        Server.MCESServer.add_game_server(server_name)


        self.back_button_clicked_Sig.emit()

