# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ServerListUIFQJlNj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtWidgets import *
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import PushButton
from qfluentwidgets import SingleDirectionScrollArea


class Ui_serverlist_ui(object):
    def setupUi(self, serverlist_ui):
        if not serverlist_ui.objectName():
            serverlist_ui.setObjectName(u"serverlist_ui")
        serverlist_ui.resize(1010, 551)
        self.verticalLayout_2 = QVBoxLayout(serverlist_ui)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.UpperButtons = QHBoxLayout()
        self.UpperButtons.setObjectName(u"UpperButtons")
        self.UpperButtons.setContentsMargins(-1, 10, -1, -1)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.UpperButtons.addItem(self.horizontalSpacer)

        self.MCESServerSetB = PushButton(serverlist_ui)
        self.MCESServerSetB.setObjectName(u"MCESServerSetB")
        self.MCESServerSetB.setMinimumSize(QSize(100, 50))
        self.MCESServerSetB.setMaximumSize(QSize(11000, 50))

        self.UpperButtons.addWidget(self.MCESServerSetB)

        self.MCServerSetB = PrimaryPushButton(serverlist_ui)
        self.MCServerSetB.setObjectName(u"MCServerSetB")
        self.MCServerSetB.setMaximumSize(QSize(114514, 50))

        self.UpperButtons.addWidget(self.MCServerSetB)


        self.verticalLayout_2.addLayout(self.UpperButtons)

        self.MCServersScroll = SingleDirectionScrollArea(serverlist_ui)
        self.MCServersScroll.setObjectName(u"MCServersScroll")
        self.MCServersScroll.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 982, 453))
        self.verticalLayout_4 = QVBoxLayout(self.scrollAreaWidgetContents_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        #从这里开始负责卡片的生成






        self.MCServersScroll.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_2.addWidget(self.MCServersScroll)


        self.retranslateUi(serverlist_ui)

        QMetaObject.connectSlotsByName(serverlist_ui)
    # setupUi

    def retranslateUi(self, serverlist_ui):
        serverlist_ui.setWindowTitle(QCoreApplication.translate("serverlist_ui", u"Form", None))
        self.MCESServerSetB.setText(QCoreApplication.translate("serverlist_ui", u"\u914d\u7f6eMCES\u670d\u52a1\u5668", None))
        self.MCServerSetB.setText(QCoreApplication.translate("serverlist_ui", u"\u6dfb\u52a0MC\u670d\u52a1\u5668", None))
        #self.MCServerNameL.setText(QCoreApplication.translate("serverlist_ui", u"MCLABEL!!!", None))
        #self.MCServerChooseB.setText(QCoreApplication.translate("serverlist_ui", u"MC_START_BUTTON", None))
    # retranslateUi

