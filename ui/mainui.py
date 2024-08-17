import sys

from PySide2.QtCore import Qt, QUrl
from PySide2.QtGui import QIcon, QDesktopServices
from PySide2.QtWidgets import QFrame, QHBoxLayout, QApplication, QWidget
from qfluentwidgets import (NavigationItemPosition, MessageBox, setTheme, Theme, MSFluentWindow,
                            NavigationAvatarWidget, qrouter, SubtitleLabel, setFont)
from qfluentwidgets import FluentIcon as FIF

from ui.mces_settings_ui import Ui_mces_settings_ui
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
    _instance = None

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Window, cls).__new__(cls, *args, **kwargs)
        return cls._instance

    def __init__(self):
        if hasattr(self, '_initialized') and self._initialized:
            return
        super().__init__()
        self._initialized = True
        serverlist_ui = QWidget()
        serverlist_ui.setObjectName("serverlist_ui")
        self.homeInterface = Widget('Main', self)
        self.serverListInterface = serverlist_ui
        self.appInterface = Widget('Application Interface', self)
        self.videoInterface = Widget('Video Interface', self)
        self.libraryInterface = Widget('library Interface', self)

        MCES_settings_ui = QWidget()
        Ui_mces_settings_ui().setupUi(MCES_settings_ui)
        self.mcesSettingsInterface = MCES_settings_ui

        self.initNavigation()
        self.initWindow()

    def easy_switch(self,widget): #在保证当前选中的导航栏不变的情况下切换页面
        self.stackedWidget.addWidget(widget)
        self.switchTo(widget)

    def change_page_to_serverlist_ui(self): #TODO Better way to switch pages
        serverlist_ui = QWidget()
        Ui_serverlist_ui().setupUi(serverlist_ui)
        self.serverListInterface = serverlist_ui
        self.easy_switch(self.serverListInterface)

    def initNavigation(self):
        self.addSubInterface(self.homeInterface, FIF.HOME, '主页', FIF.HOME_FILL)
        #self.addSubInterface(self.serverListInterface, FIF.APPLICATION, '服务器')
        #对serverListInterface进行重加载所用的高级按钮


        self.navigationInterface.addItem(
            routeKey=self.serverListInterface.objectName(),
            icon=FIF.APPLICATION,
            text='服务器',
            onClick=lambda: self.change_page_to_serverlist_ui(),
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


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = Window()
    w.show()
    app.exec_()
