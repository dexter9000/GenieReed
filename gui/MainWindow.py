
from PyQt5.QtCore import Qt, QCoreApplication, QBasicTimer
from PyQt5.QtWidgets import QApplication, QMainWindow

from conf import Config
from es.EsClient import EsClient
from gui.ConnDlg import ConnDlg
from gui.action import GuiAction
from ui.ui_main_window import Ui_MainWindow
from version import Version


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.initConfig()
        self.action = GuiAction(self)

        self.initAction()
        self.initSetupUi()

    def initSetupUi(self):
        self.setWindowTitle(self.windowTitle() + " by " + Version.getAuthor() + ' ' + Version.getVersion())

    def initConfig(self):
        self.config = Config()
        self.config.read_config()

    def initAction(self):
        self.actionExit.triggered.connect(self.close)
        self.actionConnect.triggered.connect(self.action.openConnDlg)
        self.actionAbout.triggered.connect(self.action.openAboutDlg)
        self.tabWidget.tabCloseRequested.connect(self.close_tab)

    def close_tab(self, index):
        self.tabWidget.removeTab(index)

    def openConnDlg(self):
        connDlg = ConnDlg()
        connDlg.setWindowModality(Qt.ApplicationModal)
        connDlg.loadHosts(self.config.get("connections"))
        connDlg.exec_()

        self.hostInfo = connDlg.getConnection()
        if (self.hostInfo == None):
            return

        self.es = EsClient()
        self.es.open(self.hostInfo['host'], self.hostInfo['port'])

        self.action.loadIndex(self.es)
        # QMessageBox.information(self, "温馨提示", "数据库连接成功！", QMessageBox.Yes, QMessageBox.Yes)
