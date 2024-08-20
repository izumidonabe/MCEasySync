import json
import os.path

from PySide2.QtCore import Signal
from PySide2.QtWidgets import QWidget

from Server import Server
from ui.mces_settings_ui import Ui_MCES_Settings_ui


class mces_settings(QWidget,Ui_MCES_Settings_ui):
    back_button_clicked_Sig = Signal()
    def __init__(self):
        super(mces_settings, self).__init__()
        self.setupUi(self)
        self.back_button.clicked.connect(self.back_button_clicked)
        if os.path.exists("Servers/MCES_config.json"): #说明不是第一次配置
            kwargs = json.load(open("Servers/MCES_config.json"))
            self.IpEditLine.setText(kwargs.get("ip"))
            self.PortEditLine.setText(str(kwargs.get("port")))
            self.UsernameEditLine.setText(kwargs.get("username"))
            self.PasswordLineEdit.setText(kwargs.get("password"))



    def back_button_clicked(self):
        print("back_button_clicked")
        kwargs = {"config_file":None,
                  "ip":self.IpEditLine.text(),
                  "port":self.PortEditLine.text(),
                  "username":self.UsernameEditLine.text(),
                  "password":self.PasswordLineEdit.text(),
                  "minecraft_servers":[]
                  }
        if os.path.exists("Servers/MCES_config.json"):
            kwargs["minecraft_servers"] = json.load(open("Servers/MCES_config.json")).get("minecraft_servers")
        Server(**kwargs)
        self.back_button_clicked_Sig.emit()






