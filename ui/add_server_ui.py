# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MCES_Settings_uiMbuRAj.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import *
from PySide6.QtGui import *
from PySide6.QtWidgets import *
from qfluentwidgets import CardWidget
from qfluentwidgets import IconWidget
from qfluentwidgets import LineEdit
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import SingleDirectionScrollArea
from qfluentwidgets import TitleLabel


class Ui_Add_Server_Ui(object):
    def setupUi(self, Add_Server_Ui):
        if not Add_Server_Ui.objectName():
            Add_Server_Ui.setObjectName(u"Add_Server_Ui")
        Add_Server_Ui.resize(855, 1005)
        self.verticalLayout = QVBoxLayout(Add_Server_Ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SingleDirectionScrollArea = SingleDirectionScrollArea(Add_Server_Ui)
        self.SingleDirectionScrollArea.setObjectName(u"SingleDirectionScrollArea")
        self.SingleDirectionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 827, 916))
        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.CardWidget_2 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMinimumSize(QSize(600, 100))
        self.CardWidget_2.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_6 = QHBoxLayout(self.CardWidget_2)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.horizontalLayout_6.setContentsMargins(20, -1, -1, -1)
        self.MCServerIcon = IconWidget(self.CardWidget_2)
        self.MCServerIcon.setObjectName(u"MCServerIcon")
        self.MCServerIcon.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_6.addWidget(self.MCServerIcon)

        self.Label1 = TitleLabel(self.CardWidget_2)
        self.Label1.setObjectName(u"Label1")

        self.horizontalLayout_6.addWidget(self.Label1)

        self.ServerName_edit = LineEdit(self.CardWidget_2)
        self.ServerName_edit.setObjectName(u"ServerName_edit")
        self.ServerName_edit.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(QFont.Weight(50))
        self.ServerName_edit.setFont(font)

        self.horizontalLayout_6.addWidget(self.ServerName_edit)


        self.verticalLayout_2.addWidget(self.CardWidget_2)

        self.CardWidget_3 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.CardWidget_3.setMinimumSize(QSize(600, 100))
        self.CardWidget_3.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_7 = QHBoxLayout(self.CardWidget_3)
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.horizontalLayout_7.setContentsMargins(20, -1, -1, -1)
        self.MCServerIcon_2 = IconWidget(self.CardWidget_3)
        self.MCServerIcon_2.setObjectName(u"MCServerIcon_2")
        self.MCServerIcon_2.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_7.addWidget(self.MCServerIcon_2)

        self.Label2 = TitleLabel(self.CardWidget_3)
        self.Label2.setObjectName(u"Label2")

        self.horizontalLayout_7.addWidget(self.Label2)

        self.Sync_Folders_edit = QLineEdit(self.CardWidget_3)
        self.Sync_Folders_edit.setObjectName(u"Sync_Folders_edit")
        self.Sync_Folders_edit.setMaximumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.Sync_Folders_edit.setFont(font1)

        self.horizontalLayout_7.addWidget(self.Sync_Folders_edit)


        self.verticalLayout_2.addWidget(self.CardWidget_3)

        self.CardWidget_4 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_4.setObjectName(u"CardWidget_4")
        self.CardWidget_4.setMinimumSize(QSize(600, 100))
        self.CardWidget_4.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_8 = QHBoxLayout(self.CardWidget_4)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.horizontalLayout_8.setContentsMargins(20, -1, -1, -1)
        self.MCServerIcon_3 = IconWidget(self.CardWidget_4)
        self.MCServerIcon_3.setObjectName(u"MCServerIcon_3")
        self.MCServerIcon_3.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_8.addWidget(self.MCServerIcon_3)

        self.Label3 = TitleLabel(self.CardWidget_4)
        self.Label3.setObjectName(u"Label3")

        self.horizontalLayout_8.addWidget(self.Label3)

        self.Server_Core_dir_edit = QLineEdit(self.CardWidget_4)
        self.Server_Core_dir_edit.setObjectName(u"Server_Core_dir_edit")
        self.Server_Core_dir_edit.setMaximumSize(QSize(400, 50))
        self.Server_Core_dir_edit.setFont(font1)

        self.horizontalLayout_8.addWidget(self.Server_Core_dir_edit)


        self.verticalLayout_2.addWidget(self.CardWidget_4)

        self.CardWidget_5 = CardWidget(self.scrollAreaWidgetContents)
        self.CardWidget_5.setObjectName(u"CardWidget_5")
        self.CardWidget_5.setMinimumSize(QSize(600, 100))
        self.CardWidget_5.setMaximumSize(QSize(16777215, 100))
        self.horizontalLayout_9 = QHBoxLayout(self.CardWidget_5)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(20, -1, -1, -1)
        self.MCServerIcon_4 = IconWidget(self.CardWidget_5)
        self.MCServerIcon_4.setObjectName(u"MCServerIcon_4")
        self.MCServerIcon_4.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_9.addWidget(self.MCServerIcon_4)

        self.Label4 = TitleLabel(self.CardWidget_5)
        self.Label4.setObjectName(u"Label4")

        self.horizontalLayout_9.addWidget(self.Label4)

        self.MemoryEdit = LineEdit(self.CardWidget_5)
        self.MemoryEdit.setObjectName(u"MemoryEdit")
        self.MemoryEdit.setMaximumSize(QSize(400, 50))

        self.horizontalLayout_9.addWidget(self.MemoryEdit)


        self.verticalLayout_2.addWidget(self.CardWidget_5)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_2.addItem(self.verticalSpacer)

        self.SingleDirectionScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.SingleDirectionScrollArea)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(-1, -1, -1, 0)
        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_2.addItem(self.horizontalSpacer)

        self.back_button = PrimaryPushButton(Add_Server_Ui)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(100, 50))
        self.back_button.setMaximumSize(QSize(300, 100))
        self.back_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.back_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(Add_Server_Ui)

        QMetaObject.connectSlotsByName(Add_Server_Ui)
    # setupUi

    def retranslateUi(self, Add_Server_Ui):
        Add_Server_Ui.setWindowTitle(QCoreApplication.translate("Add_Server_Ui", u"Form", None))
        self.Label1.setText(QCoreApplication.translate("Add_Server_Ui", u"\u670d\u52a1\u5668\u540d\u79f0(\u82f1\u8bed)", None))
        self.ServerName_edit.setText("")
        self.Label2.setText(QCoreApplication.translate("Add_Server_Ui", u"\u540c\u6b65\u8def\u5f84", None))
        self.Label3.setText(QCoreApplication.translate("Add_Server_Ui", u"\u670d\u52a1\u5668\u6838\u5fc3\u540d(.jar)", None))
        self.Label4.setText(QCoreApplication.translate("Add_Server_Ui", u"\u4f7f\u7528\u5185\u5b58(xG)\uff0c\u5199G", None))
        self.back_button.setText(QCoreApplication.translate("Add_Server_Ui", u"\u4fdd\u5b58\u5e76\u8fd4\u56de", None))
    # retranslateUi

