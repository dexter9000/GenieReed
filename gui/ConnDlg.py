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
        self.delConn.clicked.connect(self.delRow)

    def cleanHosts(self):
        for i in range(self.tableWidget.rowCount()):
            self.tableWidget.removeRow(0)

    def loadHosts(self, hosts):
        self.cleanHosts()
        for host in hosts:
            self.addNewHost(host)
        self.tableWidget.selectRow(0)

    def selectHost(self):
        items = self.tableWidget.selectedItems()
        if len(items) == 0:
            return None
        return self.config.get_list_item('connections', items[0].row())

    def getConnection(self):
        return self.selectHost()

    def addRow(self):
        rowNum = self.tableWidget.rowCount()
        self.tableWidget.insertRow(rowNum)
        self.tableWidget.setItem(rowNum, 0, QtWidgets.QTableWidgetItem())
        self.tableWidget.setItem(rowNum, 1, QtWidgets.QTableWidgetItem())
        self.tableWidget.setItem(rowNum, 2, QtWidgets.QTableWidgetItem())
        return rowNum

    def addNewHost(self, host):
        rowIndex = self.addRow()
        self.tableWidget.item(rowIndex, 0).setText(host['name'])
        self.tableWidget.item(rowIndex, 1).setText(host['host'])
        self.tableWidget.item(rowIndex, 2).setText(str(host['port']))

    def saveNewHost(self, host):
        self.config.add_list_item('connections', host)
        self.config.save_config()

    def delRow(self):
        items =self.tableWidget.selectedItems()
        if len(items) == 0:
            return
        item = self.tableWidget.selectedItems()[0]
        row = self.tableWidget.row(item)
        self.tableWidget.removeRow(row)
        self.config.del_list_item('connections', row)
        self.config.save_config()

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
        if host is None:
            return
        editConnDlg = EditConnDlg()
        editConnDlg.initHost(host['name'], host['host'], host['port'], host['username'], host['password'])
        editConnDlg.exec_()
        pass
