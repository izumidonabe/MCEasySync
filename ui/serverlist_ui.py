# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ServerListUIVQmiEw.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton, Dialog, window
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import ToolButton
from qfluentwidgets import TransparentToolButton
from qfluentwidgets import IconWidget
from qfluentwidgets import CardWidget
from qfluentwidgets import SingleDirectionScrollArea
from qfluentwidgets import TitleLabel

from Server import Server
#from singleton_manager import get_window_instance


class Ui_serverlist_ui(object):

    def check_if_initialize_MCES_server(self,servers_ui):
        if Server.MCESServer is None:
            w = Dialog("重要通知", "我们发现您还没有配置MCES服务器相关配置，是否现在去配置？")

            if w.exec():
                print('确认')
                window.easy_switch(window.mcesSettingsInterface)




            else:
                print('取消')

    def initialize_mc_server_card(self, **kwargs):
        #TODO 测试内容
        num_of_servers = 1
        num_of_servers = len(self.server_list)

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

        self.MCServerNameL = TitleLabel(self.CardWidget)
        self.MCServerNameL.setObjectName(u"MCServerNameL")

        self.horizontalLayout_6.addWidget(self.MCServerNameL)

        self.MCServerChooseB = PushButton(self.CardWidget)
        self.MCServerChooseB.setObjectName(u"MCServerChooseB")
        self.MCServerChooseB.setMaximumSize(QSize(100, 60))

        self.horizontalLayout_6.addWidget(self.MCServerChooseB)

        self.MCServerMoreToolB = TransparentToolButton(self.CardWidget)
        self.MCServerMoreToolB.setObjectName(u"MCServerMoreToolB")
        self.MCServerMoreToolB.setMinimumSize(QSize(60, 60))

        self.horizontalLayout_6.addWidget(self.MCServerMoreToolB)

        self.verticalLayout_4.addWidget(self.CardWidget)  # 添加卡片

    def setupUi(self, serverlist_ui):
        if not serverlist_ui.objectName():
            serverlist_ui.setObjectName(u"serverlist_ui")

        #添加一个垂直布局
        self.verticalLayout_2 = QVBoxLayout(serverlist_ui)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        #添加一个横向布局，用于放置按钮
        self.UpperButtons = QHBoxLayout()
        self.UpperButtons.setObjectName(u"UpperButtons")
        self.UpperButtons.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)
        self.UpperButtons.addItem(self.horizontalSpacer)
        #添加MCServer管理按钮
        self.MCServerSetB = PushButton(serverlist_ui)
        self.MCServerSetB.setObjectName(u"MCServerSetB")
        self.MCServerSetB.setMinimumSize(QSize(100, 50))
        self.MCServerSetB.setMaximumSize(QSize(11000, 50))
        self.UpperButtons.addWidget(self.MCServerSetB)
        #添加MCESServer管理按钮
        self.MCESServerSetB = PrimaryPushButton(serverlist_ui)
        self.MCESServerSetB.setObjectName(u"MCESServerSetB")
        self.MCESServerSetB.setMaximumSize(QSize(114514, 50))
        self.UpperButtons.addWidget(self.MCESServerSetB)
        #把按钮组绑定在垂直的layout里
        self.verticalLayout_2.addLayout(self.UpperButtons)
        #添加一个滚动区域
        self.MCServersScroll = SingleDirectionScrollArea(serverlist_ui)
        self.MCServersScroll.setObjectName(u"MCServersScroll")
        self.MCServersScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 982, 453))
        #添加一个垂直布局，用于放置所有的MC服务器卡片
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        #下面的部分抽成函数

        self.check_if_initialize_MCES_server(serverlist_ui)


        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer)

        self.MCServersScroll.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.MCServersScroll)


        self.retranslateUi(serverlist_ui)

        QMetaObject.connectSlotsByName(serverlist_ui)
    # setupUi



    def retranslateUi(self, serverlist_ui):
        serverlist_ui.setWindowTitle(QCoreApplication.translate("serverlist_ui", u"Form", None))
        self.MCServerSetB.setText(QCoreApplication.translate("serverlist_ui", u"\u914d\u7f6eMCES\u670d\u52a1\u5668", None))
        self.MCESServerSetB.setText(QCoreApplication.translate("serverlist_ui", u"\u6dfb\u52a0MC\u670d\u52a1\u5668", None))
        #self.MCServerNameL.setText(QCoreApplication.translate("serverlist_ui", u"MCLABEL!!!", None))
        #self.MCServerChooseB.setText(QCoreApplication.translate("serverlist_ui", u"MC_START_BUTTON", None))
    # retranslateUi

