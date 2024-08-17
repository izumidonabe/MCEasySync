# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'MCES_Settings_uihPDsCc.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import PushButton
from qfluentwidgets import PrimaryPushButton
from qfluentwidgets import IconWidget
from qfluentwidgets import CardWidget
from qfluentwidgets import SingleDirectionScrollArea
from qfluentwidgets import TitleLabel
from qfluentwidgets import LineEdit
from qfluentwidgets import PasswordLineEdit


class Ui_mces_settings_ui(object):
    def setupUi(self, MCES_Settings_ui):
        if not MCES_Settings_ui.objectName():
            MCES_Settings_ui.setObjectName(u"MCES_Settings_ui")
        self.verticalLayout = QVBoxLayout(MCES_Settings_ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.SingleDirectionScrollArea = SingleDirectionScrollArea(MCES_Settings_ui)
        self.SingleDirectionScrollArea.setObjectName(u"SingleDirectionScrollArea")
        self.SingleDirectionScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 761, 494))
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
        self.MCServerIcon.setObjectName(u"MCESServerIcon")
        self.MCServerIcon.setMaximumSize(QSize(60, 60))

        self.horizontalLayout_6.addWidget(self.MCServerIcon)

        self.MCServerNameL = TitleLabel(self.CardWidget_2)
        self.MCServerNameL.setObjectName(u"MCESServerNameL")

        self.horizontalLayout_6.addWidget(self.MCServerNameL)

        self.LineEdit = LineEdit(self.CardWidget_2)
        self.LineEdit.setObjectName(u"LineEdit")
        self.LineEdit.setMaximumSize(QSize(400, 50))
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.LineEdit.setFont(font)

        self.horizontalLayout_6.addWidget(self.LineEdit)


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

        self.MCServerNameL_2 = TitleLabel(self.CardWidget_3)
        self.MCServerNameL_2.setObjectName(u"MCServerNameL_2")

        self.horizontalLayout_7.addWidget(self.MCServerNameL_2)

        self.lineEdit = QLineEdit(self.CardWidget_3)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setMaximumSize(QSize(400, 50))
        font1 = QFont()
        font1.setPointSize(12)
        self.lineEdit.setFont(font1)

        self.horizontalLayout_7.addWidget(self.lineEdit)


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

        self.MCServerNameL_3 = TitleLabel(self.CardWidget_4)
        self.MCServerNameL_3.setObjectName(u"MCServerNameL_3")

        self.horizontalLayout_8.addWidget(self.MCServerNameL_3)

        self.lineEdit_2 = QLineEdit(self.CardWidget_4)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setMaximumSize(QSize(400, 50))
        self.lineEdit_2.setFont(font1)

        self.horizontalLayout_8.addWidget(self.lineEdit_2)


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

        self.MCServerNameL_4 = TitleLabel(self.CardWidget_5)
        self.MCServerNameL_4.setObjectName(u"MCServerNameL_4")

        self.horizontalLayout_9.addWidget(self.MCServerNameL_4)

        self.PasswordLineEdit = PasswordLineEdit(self.CardWidget_5)
        self.PasswordLineEdit.setObjectName(u"PasswordLineEdit")
        self.PasswordLineEdit.setMaximumSize(QSize(400, 50))
        self.PasswordLineEdit.setFont(font)

        self.horizontalLayout_9.addWidget(self.PasswordLineEdit)


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

        self.back_button = PrimaryPushButton(MCES_Settings_ui)
        self.back_button.setObjectName(u"back_button")
        self.back_button.setMinimumSize(QSize(100, 50))
        self.back_button.setMaximumSize(QSize(300, 100))
        self.back_button.setCheckable(False)

        self.horizontalLayout_2.addWidget(self.back_button)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(MCES_Settings_ui)

        QMetaObject.connectSlotsByName(MCES_Settings_ui)
    # setupUi

    def retranslateUi(self, MCES_Settings_ui):
        MCES_Settings_ui.setWindowTitle(QCoreApplication.translate("MCES_Settings_ui", u"Form", None))
        self.MCServerNameL.setText(QCoreApplication.translate("MCES_Settings_ui", u"MCES\u670d\u52a1ip:", None))
        self.LineEdit.setText(QCoreApplication.translate("MCES_Settings_ui", u"114", None))
        self.MCServerNameL_2.setText(QCoreApplication.translate("MCES_Settings_ui", u"MCES\u670d\u52a1\u7aef\u53e3:", None))
        self.MCServerNameL_3.setText(QCoreApplication.translate("MCES_Settings_ui", u"MCES\u7528\u6237\u540d:", None))
        self.MCServerNameL_4.setText(QCoreApplication.translate("MCES_Settings_ui", u"MCES\u5bc6\u7801:", None))
        self.back_button.setText(QCoreApplication.translate("MCES_Settings_ui", u"\u4fdd\u5b58\u5e76\u8fd4\u56de", None))
    # retranslateUi

