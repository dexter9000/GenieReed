from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QMessageBox

from es import EsClient
from gui.SignalThread import SignalThread
from ui.ui_edit_conn_dlg import Ui_Dialog


class EditConnDlg(QDialog, Ui_Dialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
        self.initSetupUi()
        self.initAction()

    def initSetupUi(self):
        self.test_progress.setVisible(False)
        self.setWindowModality(Qt.ApplicationModal)

    def initAction(self):
        self.btn_test_connect.clicked.connect(self.testConnect)

    def initHost(self, name, host, port):
        self.txt_name.setText(name)
        self.txt_host.setText(host)
        self.txt_port.setText(str(port))

    def getHost(self):
        return {
            "name": self.txt_name.text(),
            "host": self.txt_host.text(),
            "port": int(self.txt_port.text())
        }

    def testConnect(self):
        self.test_progress.setVisible(True)
        my_thread = SignalThread(self.testConnectFunc)
        my_thread.my_signal.connect(self.testConnectSignalFn)
        my_thread.start()

    def testConnectFunc(self):
        host = self.getHost()
        es = EsClient()
        es.testHost(host['host'] + ':' + str(host['port']))

    def testConnectSignalFn(self, result):
        print(result)
        if result['result'] == 'succ':
            QMessageBox.information(self, "成功", "连接成功")
        elif result['result'] == 'error':
            QMessageBox.critical(self, "失败", "连接失败")
        self.test_progress.setVisible(False)
