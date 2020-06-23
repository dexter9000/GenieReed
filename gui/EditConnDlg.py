from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from ui.ui_edit_conn_dlg import Ui_Dialog


class EditConnDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.initAction()

    def initAction(self):
        pass

    def getHost(self):
        host = {
            "name": self.txt_name.text(),
            "host": self.txt_host.text(),
            "port": int(self.txt_port.text())
        }
        return host
