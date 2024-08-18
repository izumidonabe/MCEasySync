from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from qfluentwidgets import CardWidget, GroupHeaderCardWidget, InfoBarIcon, FluentIcon, SubtitleLabel, BodyLabel, \
    PushButton, PrimaryPushButton, ProgressBar, ComboBox, StrongBodyLabel
from qfluentwidgets import SimpleCardWidget
from qfluentwidgets import HeaderCardWidget
from qfluentwidgets import ScrollArea
from qfluentwidgets.components.widgets.flyout import IconWidget



class Ui_McServer_manage_UI(object):
    def setupUi(self, McServer_UI):
        if not McServer_UI.objectName():
            McServer_UI.setObjectName(u"McServer_UI")

        self.verticalLayout = QVBoxLayout(McServer_UI)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.ScrollArea = ScrollArea(McServer_UI)
        self.ScrollArea.setObjectName(u"ScrollArea")
        self.ScrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 729, 452))

        self.verticalLayout_2 = QVBoxLayout(self.scrollAreaWidgetContents)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")

        #header_font = QFont("Microsoft YaHei", 12)

        self.FrpServerManageCard = GroupHeaderCardWidget(self.scrollAreaWidgetContents)
        self.FrpServerManageCard.setObjectName(u"FrpServerManageCard")
        self.FrpServerManageCard.setTitle("Frp服务器管理",)
        #self.FrpServerManageCard.headerLabel.setFont(QFont(header_font))
        #组1
        self.frp_server_status_title = StrongBodyLabel()
        self.frp_server_status_title.setText("SERVER STATUS")
        group = self.FrpServerManageCard.addGroup(FluentIcon.APPLICATION, "服务器状态", "FRP端口映射服务器", self.frp_server_status_title)
        group.setSeparatorVisible(True)
        #添加自定义工具行
        self.hintIcon = IconWidget(FluentIcon.INFO)
        #self.hintIcon.setFixedSize(16,16)
        self.hintLabel = BodyLabel("点击右侧按钮切换服务器状态")
        self.startfrpButton = PrimaryPushButton(FluentIcon.PLAY_SOLID,"启动")
        self.stopfrpButton = PushButton(FluentIcon.POWER_BUTTON,"停止")
        self.FrpServerManageCard.bottomLayout = QHBoxLayout()
        self.FrpServerManageCard.bottomLayout.setSpacing(10)
        self.FrpServerManageCard.bottomLayout.setContentsMargins(15,15,24,20)

        self.FrpServerManageCard.bottomLayout.addWidget(self.hintIcon, 0,Qt.AlignLeft)
        self.FrpServerManageCard.bottomLayout.addWidget(self.hintLabel, 0,Qt.AlignLeft)
        self.FrpServerManageCard.bottomLayout.addStretch(1)
        self.FrpServerManageCard.bottomLayout.addWidget(self.stopfrpButton, 0,Qt.AlignRight)
        self.FrpServerManageCard.bottomLayout.addWidget(self.startfrpButton, 0,Qt.AlignRight)

        self.FrpServerManageCard.vBoxLayout.addLayout(self.FrpServerManageCard.bottomLayout)
        self.verticalLayout_2.addWidget(self.FrpServerManageCard)

        #同步服务状态
        self.SyncManageCard = GroupHeaderCardWidget(self.scrollAreaWidgetContents)
        self.SyncManageCard.setObjectName(u"SyncManageCard")
        self.SyncManageCard.setTitle("同步服务管理")


        #首先选择同步模式
        self.choose_sync_mode_box = ComboBox()
        self.choose_sync_mode_box.addItems(["将本机文件同步到服务器","将服务器文件同步到本机"])
        self.choose_sync_mode_box.setFixedHeight(40)
        self.choose_sync_mode_box.setFixedWidth(300)
        self.SyncManageCard.addGroup(FluentIcon.SETTING, "选择同步模式", "选择同步模式", self.choose_sync_mode_box)

        self.Icon = IconWidget(FluentIcon.INFO)
        self.sync_process_bar = ProgressBar()
        self.sync_process_bar.setFixedWidth(300)
        self.SyncManageCard.addGroup(FluentIcon.INFO, "同步进度条", "展示目前同步的状态", self.sync_process_bar)

        self.sync_start_button = PrimaryPushButton(FluentIcon.PLAY_SOLID,"开始同步")
        self.SyncManageCard.addGroup(FluentIcon.SYNC, "同步操作", "务必在确定服务器关闭后进行（服务器弹窗关闭）", self.sync_start_button)


        self.verticalLayout_2.addWidget(self.SyncManageCard)

        #MC服务器管理
        self.MCServerManageCard = GroupHeaderCardWidget(self.scrollAreaWidgetContents)
        self.MCServerManageCard.setObjectName(u"MCServerManageCard")
        self.MCServerManageCard.setTitle("Minecraft服务器管理")
        self.mcserver_status_title = StrongBodyLabel("MCSERVER STATUS")
        self.MCServerManageCard.addGroup(FluentIcon.GAME, "服务器状态", "Minecraft服务器状态（可能不准，请以弹出的服务器窗口为准）", self.mcserver_status_title)
        self.hintIcon = IconWidget(FluentIcon.INFO)
        self.hintLabel = BodyLabel("点击右侧按钮切换服务器状态")
        self.startmcButton = PrimaryPushButton(FluentIcon.PLAY_SOLID, "启动")
        self.stopmcButton = PushButton(FluentIcon.POWER_BUTTON, "停止")
        self.MCServerManageCard.bottomLayout = QHBoxLayout()
        self.MCServerManageCard.bottomLayout.setSpacing(10)
        self.MCServerManageCard.bottomLayout.setContentsMargins(15, 15, 24, 20)

        self.MCServerManageCard.bottomLayout.addWidget(self.hintIcon, 0, Qt.AlignLeft)
        self.MCServerManageCard.bottomLayout.addWidget(self.hintLabel, 0, Qt.AlignLeft)
        self.MCServerManageCard.bottomLayout.addStretch(1)
        self.MCServerManageCard.bottomLayout.addWidget(self.stopmcButton, 0, Qt.AlignRight)
        self.MCServerManageCard.bottomLayout.addWidget(self.startmcButton, 0, Qt.AlignRight)

        self.MCServerManageCard.vBoxLayout.addLayout(self.MCServerManageCard.bottomLayout)




        self.verticalLayout_2.addWidget(self.MCServerManageCard)

        self.verticalSpacer = QSpacerItem(20, 40, QSizePolicy.Minimum, QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(self.verticalSpacer)



        self.ScrollArea.setWidget(self.scrollAreaWidgetContents)

        self.verticalLayout.addWidget(self.ScrollArea)


        QMetaObject.connectSlotsByName(McServer_UI)