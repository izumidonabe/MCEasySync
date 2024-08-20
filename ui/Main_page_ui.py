# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'main_page_uiJaQBcJ.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import CardWidget
from qfluentwidgets import BodyLabel
from qfluentwidgets import StrongBodyLabel
from qfluentwidgets import SubtitleLabel
from qfluentwidgets import TitleLabel
from qfluentwidgets import LargeTitleLabel


class Ui_main_page_ui(object):
    def setupUi(self, main_page_ui):
        if not main_page_ui.objectName():
            main_page_ui.setObjectName(u"main_page_ui")
        main_page_ui.resize(563, 510)
        self.verticalLayout = QVBoxLayout(main_page_ui)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.CardWidget = CardWidget(main_page_ui)
        self.CardWidget.setObjectName(u"CardWidget")
        self.CardWidget.setMaximumSize(QSize(16777215, 200))
        self.verticalLayout_2 = QVBoxLayout(self.CardWidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.LargeTitleLabel = LargeTitleLabel(self.CardWidget)
        self.LargeTitleLabel.setObjectName(u"LargeTitleLabel")
        self.LargeTitleLabel.setMinimumSize(QSize(100, 0))

        self.verticalLayout_2.addWidget(self.LargeTitleLabel)

        self.SubtitleLabel = SubtitleLabel(self.CardWidget)
        self.SubtitleLabel.setObjectName(u"SubtitleLabel")

        self.verticalLayout_2.addWidget(self.SubtitleLabel)


        self.horizontalLayout.addWidget(self.CardWidget)


        self.verticalLayout.addLayout(self.horizontalLayout)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.CardWidget_3 = CardWidget(main_page_ui)
        self.CardWidget_3.setObjectName(u"CardWidget_3")
        self.verticalLayout_3 = QVBoxLayout(self.CardWidget_3)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.BodyLabel = BodyLabel(self.CardWidget_3)
        self.BodyLabel.setObjectName(u"BodyLabel")
        font = QFont()
        font.setPointSize(12)
        font.setBold(False)
        font.setWeight(50)
        self.BodyLabel.setFont(font)

        self.verticalLayout_3.addWidget(self.BodyLabel)

        self.BodyLabel_2 = BodyLabel(self.CardWidget_3)
        self.BodyLabel_2.setObjectName(u"BodyLabel_2")
        self.BodyLabel_2.setFont(font)

        self.verticalLayout_3.addWidget(self.BodyLabel_2)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_3.addItem(self.verticalSpacer)


        self.horizontalLayout_2.addWidget(self.CardWidget_3)

        self.CardWidget_2 = CardWidget(main_page_ui)
        self.CardWidget_2.setObjectName(u"CardWidget_2")
        self.CardWidget_2.setMaximumSize(QSize(114514, 16777215))
        self.verticalLayout_4 = QVBoxLayout(self.CardWidget_2)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.TitleLabel = TitleLabel(self.CardWidget_2)
        self.TitleLabel.setObjectName(u"TitleLabel")

        self.verticalLayout_4.addWidget(self.TitleLabel)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.BodyLabel_4 = BodyLabel(self.CardWidget_2)
        self.BodyLabel_4.setObjectName(u"BodyLabel_4")

        self.horizontalLayout_3.addWidget(self.BodyLabel_4)

        self.VERSION_TITLE = StrongBodyLabel(self.CardWidget_2)
        self.VERSION_TITLE.setObjectName(u"VERSION_TITLE")

        self.horizontalLayout_3.addWidget(self.VERSION_TITLE)

        self.horizontalSpacer = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_3.addItem(self.horizontalSpacer)


        self.verticalLayout_4.addLayout(self.horizontalLayout_3)

        self.UPDATE_LOG_TITLE = BodyLabel(self.CardWidget_2)
        self.UPDATE_LOG_TITLE.setObjectName(u"UPDATE_LOG_TITLE")
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(False)
        font1.setWeight(50)
        self.UPDATE_LOG_TITLE.setFont(font1)
        self.UPDATE_LOG_TITLE.setWordWrap(True)

        self.verticalLayout_4.addWidget(self.UPDATE_LOG_TITLE)

        self.verticalSpacer_2 = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)

        self.verticalLayout_4.addItem(self.verticalSpacer_2)


        self.horizontalLayout_2.addWidget(self.CardWidget_2)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.retranslateUi(main_page_ui)

        QMetaObject.connectSlotsByName(main_page_ui)
    # setupUi

    def retranslateUi(self, main_page_ui):
        main_page_ui.setWindowTitle(QCoreApplication.translate("main_page_ui", u"Form", None))
        self.LargeTitleLabel.setText(QCoreApplication.translate("main_page_ui", u"Minecraft Server Easy Sync", None))
        self.SubtitleLabel.setText(QCoreApplication.translate("main_page_ui", u"\u4f60\u7684MC\u670d\u52a1\u5668\u540c\u6b65\u52a9\u624b", None))
        self.BodyLabel.setText(QCoreApplication.translate("main_page_ui", u"\u8bf7\u5728\u5de6\u4fa7\u9009\u62e9\u670d\u52a1\u5668\u754c\u9762", None))
        self.BodyLabel_2.setText(QCoreApplication.translate("main_page_ui", u"\u6765\u5f00\u59cb\u4f7f\u7528MCES\u5427", None))
        self.TitleLabel.setText(QCoreApplication.translate("main_page_ui", u"\u66f4\u65b0\u65e5\u5fd7", None))
        self.BodyLabel_4.setText(QCoreApplication.translate("main_page_ui", u"\u5f53\u524d\u7248\u672c\uff1a", None))
        self.VERSION_TITLE.setText(QCoreApplication.translate("main_page_ui", u"VERSION", None))
        self.UPDATE_LOG_TITLE.setText(QCoreApplication.translate("main_page_ui", u"UPDATELOG", None))
    # retranslateUi

