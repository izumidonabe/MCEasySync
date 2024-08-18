import json
import os.path
import time

from PySide2.QtCore import Signal, QSize
from PySide2.QtWidgets import QWidget, QHBoxLayout, QSpacerItem, QSizePolicy
from qfluentwidgets import CardWidget, IconWidget, TitleLabel, PushButton, TransparentToolButton, FluentIcon, Dialog

from ui.serverlist_ui import Ui_serverlist_ui


class serverlist(QWidget,Ui_serverlist_ui):
    open_MCES_config_signal = Signal()
    open_AddServer_signal = Signal()
    open_MC_Server_Manage_signal = Signal(str)


    def __init__(self):
        super(serverlist, self).__init__()
        self.setupUi(self)
        print("serverlist")

        if(os.path.exists("Servers/MCES_config.json")):
            self.avalible_servers = json.load(open("Servers/MCES_config.json"))["minecraft_servers"]
        else:
            self.avalible_servers = []

        for server_name in self.avalible_servers:
            self.Add_New_Server_Card(server_name)


        self.MCServerSetB.clicked.connect(self.MCServerSetB_clicked)
        self.MCESServerSetB.clicked.connect(self.MCESServerSetB_clicked)




    def Add_New_Server_Card(self,server_name):
        try:
            self.verticalLayout_4.removeItem(self.verticalSpacer)
        except AttributeError:
            pass
        self.CardWidget = CardWidget(self.scrollAreaWidgetContents_2)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMinimumSize(QSize(600, 100))
        self.CardWidget.setMaximumSize(QSize(16777215, 100))

        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.MCServerIcon = IconWidget(self.CardWidget)
        self.MCServerIcon.setObjectName(u"MCServerIcon")
        self.MCServerIcon.setMaximumSize(QSize(60, 60))
        self.horizontalLayout_6.addWidget(self.MCServerIcon)
        self.MCServerIcon.icon = FluentIcon.GAME

        self.MCServerNameL = TitleLabel(self.CardWidget)
        self.MCServerNameL.setObjectName(u"MCServerNameL")
        self.MCServerNameL.setText(server_name)
        self.horizontalLayout_6.addWidget(self.MCServerNameL)


        self.MCServerChooseB = PushButton(self.CardWidget)
        self.MCServerChooseB.setObjectName(u"MCServerChooseB")
        self.MCServerChooseB.setMaximumSize(QSize(100, 60))
        self.MCServerChooseB.setText("打开服务器")
        self.MCServerChooseB.setProperty("Server_Name", server_name)
        self.MCServerChooseB.clicked.connect(lambda :self.MCServerChooseB_clicked(server_name))

        self.horizontalLayout_6.addWidget(self.MCServerChooseB)

        self.MCServerMoreToolB = TransparentToolButton(self.CardWidget)
        self.MCServerMoreToolB.setObjectName(u"MCServerMoreToolB")
        self.MCServerMoreToolB.setMinimumSize(QSize(60, 60))
        self.MCServerMoreToolB.setIcon(FluentIcon.MORE)


        self.horizontalLayout_6.addWidget(self.MCServerMoreToolB)

        # 在这里才把卡片组装到滚动区域里
        self.verticalLayout_4.addWidget(self.CardWidget)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)



    def MCServerSetB_clicked(self):
        self.open_AddServer_signal.emit()
        #self.Add_New_Server_Card(str(time.localtime()))

    def MCESServerSetB_clicked(self):
        self.open_MCES_config_signal.emit()

    def MCServerChooseB_clicked(self,server_name):
        print(server_name)
        self.open_MC_Server_Manage_signal.emit(server_name)
        print("MCServerChooseB_clicked")







