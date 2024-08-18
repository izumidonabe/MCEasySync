import os.path
import sys

from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtWidgets import QFrame, QHBoxLayout, QApplication, QWidget, QStackedWidget
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont, Dialog)
from qfluentwidgets import FluentIcon as FIF

from ui.add_server import add_server_Ui
from ui.mces_settings import mces_settings
from ui.mces_settings_ui import Ui_MCES_Settings_ui
from ui.mcserver_manage_ui import mcserver_manage_Ui
from ui.serverlist import serverlist
from ui.serverlist_ui import Ui_serverlist_ui


class Widget(QFrame):

    def __init__(self, text: str, parent=None):
        super().__init__(parent=parent)
        self.label = SubtitleLabel(text, self)
        self.hBoxLayout = QHBoxLayout(self)

        setFont(self.label, 40)
        self.label.setAlignment(Qt.AlignCenter)
        self.hBoxLayout.addWidget(self.label, 2, Qt.AlignCenter)
        self.setObjectName(text.replace(' ', '-'))



class Window(MSFluentWindow):
    def __init__(self):

        super().__init__()
        self._initialized = True
        #用于切换页面
        server_ui_stack = QStackedWidget()
        server_ui_stack.setObjectName("serverlist_ui")

        #serverlist_ui里面的一级界面-服务器列表
        serverlist_ui = serverlist()
        server_ui_stack.addWidget(serverlist_ui)

        #serverlist_ui里面的二级界面-MCES服务器设置
        MCES_settings_ui = mces_settings()
        MCES_settings_ui.back_button_clicked_Sig.connect(self.change_page_to_serverlist_stack)
        self.MCES_Settings_Index = server_ui_stack.addWidget(MCES_settings_ui)

        #serverlist_ui里面的三级界面-添加mc服务器
        add_server_ui = add_server_Ui()
        add_server_ui.back_button_clicked_Sig.connect(self.change_page_to_serverlist_stack)
        self.add_server_ui_index = server_ui_stack.addWidget(add_server_ui)

        #serverlist_ui里面的四级界面-mc服务器配置
        self.mcserver_manage = mcserver_manage_Ui()
        self.mc_manage_index = server_ui_stack.addWidget(self.mcserver_manage)



        self.server_ui_stack = server_ui_stack
        #临时调试
        self.homeInterface = Widget('Main', self)
        #self.homeInterface = mcserver_manage_Ui()
        self.serverListInterface = server_ui_stack
        self.appInterface = Widget('Application Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.libraryInterface = Widget('library Interface', self)
        self.initNavigation()
        self.initWindow()



    def change_page_to_serverlist_stack(self): #TODO Better way to switch pages
        serverlist_ui = serverlist()
        serverlist_ui.open_MCES_config_signal.connect(self.on_MCES_server_set_button_clicked)
        serverlist_ui.open_AddServer_signal.connect(self.on_AddServer_button_clicked)
        serverlist_ui.open_MC_Server_Manage_signal.connect(self.open_MC_Server_manage_ui)

        if not os.path.exists("Servers/MCES_config.json"):
            w = Dialog("警告", "你还没有配置MCES服务器，必须先配置相关信息才能使用MCES功能", self)
            w.yesButton.setText('立刻配置')
            w.cancelButton.hide()
            if w.exec():
                print('确认')
                self.server_ui_stack.setCurrentIndex(self.MCES_Settings_Index)
                self.stackedWidget.addWidget(self.server_ui_stack)
                self.stackedWidget.setCurrentWidget(self.server_ui_stack)
            else:
                print(1)

        else:
            self.server_ui_stack.addWidget(serverlist_ui)
            self.server_ui_stack.setCurrentWidget(serverlist_ui)

            print("实时设置")
            self.stackedWidget.addWidget(self.server_ui_stack)
            self.stackedWidget.setCurrentWidget(self.server_ui_stack)

    def on_MCES_server_set_button_clicked(self):
        print("MCES服务器设置")
        self.server_ui_stack.setCurrentIndex(self.MCES_Settings_Index)

    def on_AddServer_button_clicked(self):
        print("添加服务器按钮")
        self.server_ui_stack.setCurrentIndex(self.add_server_ui_index)

    def open_MC_Server_manage_ui(self,server_name):
        print("打开"+server_name+" MC服务器管理界面")
        self.mcserver_manage.reinitailze()
        self.server_ui_stack.setCurrentIndex(self.mc_manage_index)


    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页', FIF.HOME_FILL)
        #self.addSubInterface(self.serverListInterface, FIF.APPLICATION, '服务器')
        #对serverListInterface进行重加载所用的高级按钮


        self.navigationInterface.addItem(
            routeKey=self.serverListInterface.objectName(),
            icon=FIF.APPLICATION,
            text='服务器',
            onClick=lambda: self.change_page_to_serverlist_stack(),
            selectable=True,
        )

        self.addSubInterface(self.appInterface, FIF.APPLICATION, '应用')
        self.addSubInterface(self.videoInterface, FIF.VIDEO, '视频')

        self.addSubInterface(self.libraryInterface, FIF.BOOK_SHELF, '库', FIF.LIBRARY_FILL, NavigationItemPosition.BOTTOM)

        # 添加自定义导航组件
        self.navigationInterface.addItem(
            routeKey='Help',
            icon=FIF.HELP,
            text='帮助',
            onClick=self.showMessageBox,
            selectable=False,
            position=NavigationItemPosition.BOTTOM,
        )

        self.navigationInterface.setCurrentItem(self.homeInterface.objectName())

    def initWindow(self):
        self.resize(1280, 720)
        self.setWindowIcon(QIcon(':/qfluentwidgets/images/logo.png'))
        self.setWindowTitle('PyQt-Fluent-Widgets')

        desktop = QApplication.desktop().availableGeometry()
        w, h = desktop.width(), desktop.height()
        self.move(w//2 - self.width()//2, h//2 - self.height()//2)

    def showMessageBox(self):
        w = MessageBox(
            '支持作者🥰',
            '个人开发不易，如果这个项目帮助到了您，可以考虑请作者喝一瓶快乐水🥤。您的支持就是作者开发和维护项目的动力🚀',
            self
        )
        w.yesButton.setText('来啦老弟')
        w.cancelButton.setText('下次一定')

        if w.exec():
            QDesktopServices.openUrl(QUrl("https://qfluentwidgets.com/zh/price/"))



