from PyQt5 import QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog

from gui.EditConnDlg import EditConnDlg
from ui.ui_conn_dlg import Ui_ConnDlg


class ConnDlg(QDialog, Ui_ConnDlg):
    def __init__(self, config, parent=None):
        super(QDialog, self).__init__(parent)
        self.config = config
        self.setupUi(self)
        self.setWindowModality(Qt.ApplicationModal)
        self.initAction()

    def initAction(self):
        self.addConn.clicked.connect(self.openNewConnDlg)
        self.editConn.clicked.connect(self.openEditConnDlg)
        self.delConn.clicked.connect(self.addRow)

    def cleanHosts(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)

    def loadHosts(self, hosts):
        self.cleanHosts()
        for host in hosts:
            self.addNewHost(host)
        self.tableWidget.selectRow(0)

    def selectHost(self):
        list = self.tableWidget.selectedItems()
        self.selectedHost = {
            "name": list[0].text(),
            "host": list[1].text(),
            "port": int(list[2].text())
        }
        return self.selectedHost

    def getConnection(self):
        self.selectHost()
        return self.selectedHost

    def addRow(self):
        rowNum = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowNum)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(rowNum, 0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(rowNum, 1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setItem(rowNum, 2, item)
        return rowNum

    def addNewHost(self, host):
        rowIndex = self.addRow()
        item = self.tableWidget.item(rowIndex, 0)
        item.setText(host['name'])
        item = self.tableWidget.item(rowIndex, 1)
        item.setText(host['host'])
        item = self.tableWidget.item(rowIndex, 2)
        item.setText(str(host['port']))

    def saveNewHost(self, host):
        self.config.add_list_item('connections', host)
        self.config.save_config()
        pass

    def delHost(self):
        pass

    def closeDlg(self):
        self.close()

    def openNewConnDlg(self):
        editConnDlg = EditConnDlg()
        editConnDlg.setWindowTitle('New Connect')
        result = editConnDlg.exec_()
        if (result == 1):
            self.addNewHost(editConnDlg.getHost())
            self.saveNewHost(editConnDlg.getHost())

    def openEditConnDlg(self):
        host = self.selectHost()
        editConnDlg = EditConnDlg()
        editConnDlg.initHost(host['name'], host['host'], host['port'])
        editConnDlg.exec_()
        pass
