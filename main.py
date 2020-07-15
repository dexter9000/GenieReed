import sys

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QApplication, QMainWindow, QAction, QMenu
from PyQt5.QtCore import Qt, QCoreApplication

from ui.ui_main_window import Ui_MainWindow
from gui.ConnDlg import ConnDlg
from gui.action import GuiAction
from gui.router import GuiRouter
from es.EsClient import EsClient
from conf import Config
from version import Version


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)
        self.config = Config()
        self.config.read_config()
        self.router = GuiRouter()
        self.action = GuiAction(self)

        self.initAction()
        self.setWindowTitle(self.windowTitle() + " by " + Version.getAuthor() + ' ' + Version.getVersion())

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

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
