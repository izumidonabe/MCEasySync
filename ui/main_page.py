from PySide2.QtWidgets import QWidget

from ui.Main_page_ui import Ui_main_page_ui
from updater import updater


class main_page_ui(QWidget,Ui_main_page_ui):

    def __init__(self):
        super(main_page_ui, self).__init__()
        self.setupUi(self)
        self.VERSION_TITLE.setText(updater.VERSION)
        self.UPDATE_LOG_TITLE.setText(updater.UPDATE_LOG)

