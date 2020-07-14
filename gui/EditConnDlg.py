from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from es import EsClient
from ui.ui_edit_conn_dlg import Ui_Dialog


class EditConnDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.initAction()
        ProgressBar(self, minimum=0, maximum=100, objectName="RedProgressBar")

    def initAction(self):
        self.btn_test_connect.clicked.connect(self.testConnect)
        pass


    def getHost(self):
        host = {
            "name": self.txt_name.text(),
            "host": self.txt_host.text(),
            "port": int(self.txt_port.text())
        }
        return host

    def testConnect(self):
        host = self.getHost()
        es = EsClient()
        es.testHost(host['host'] + ':' + str(host['port']))
