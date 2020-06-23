# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_conn_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_ConnDlg(object):
    def setupUi(self, ConnDlg):
        ConnDlg.setObjectName("ConnDlg")
        ConnDlg.resize(625, 625)
        self.verticalLayout = QtWidgets.QVBoxLayout(ConnDlg)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(ConnDlg)
        self.frame.setObjectName("frame")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.frame)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.widget = QtWidgets.QWidget(self.frame)
        self.widget.setObjectName("widget")
        self.gridLayout = QtWidgets.QGridLayout(self.widget)
        self.gridLayout.setObjectName("gridLayout")
        self.addConn = QtWidgets.QPushButton(self.widget)
        self.addConn.setMaximumSize(QtCore.QSize(50, 50))
        self.addConn.setObjectName("addConn")
        self.gridLayout.addWidget(self.addConn, 0, 0, 1, 1)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem, 0, 4, 1, 1)
        self.delConn = QtWidgets.QPushButton(self.widget)
        self.delConn.setMaximumSize(QtCore.QSize(60, 16777215))
        self.delConn.setAutoDefault(True)
        self.delConn.setObjectName("delConn")
        self.gridLayout.addWidget(self.delConn, 0, 2, 1, 1)
        self.editConn = QtWidgets.QPushButton(self.widget)
        self.editConn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.editConn.setObjectName("editConn")
        self.gridLayout.addWidget(self.editConn, 0, 1, 1, 1)
        self.testConn = QtWidgets.QPushButton(self.widget)
        self.testConn.setMaximumSize(QtCore.QSize(50, 16777215))
        self.testConn.setObjectName("testConn")
        self.gridLayout.addWidget(self.testConn, 0, 3, 1, 1)
        self.verticalLayout_2.addWidget(self.widget)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.verticalLayout_2.addWidget(self.lineEdit)
        self.tableWidget = QtWidgets.QTableWidget(self.frame)
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.tableWidget.setSelectionMode(QtWidgets.QAbstractItemView.SingleSelection)
        self.tableWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectRows)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(3)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        self.verticalLayout_2.addWidget(self.tableWidget)
        self.verticalLayout.addWidget(self.frame)
        self.buttonBox = QtWidgets.QDialogButtonBox(ConnDlg)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(ConnDlg)
        self.buttonBox.accepted.connect(ConnDlg.accept)
        self.buttonBox.rejected.connect(ConnDlg.reject)
        self.tableWidget.doubleClicked['QModelIndex'].connect(ConnDlg.accept)
        QtCore.QMetaObject.connectSlotsByName(ConnDlg)

    def retranslateUi(self, ConnDlg):
        _translate = QtCore.QCoreApplication.translate
        ConnDlg.setWindowTitle(_translate("ConnDlg", "Dialog"))
        self.addConn.setText(_translate("ConnDlg", "New"))
        self.delConn.setText(_translate("ConnDlg", "Delete"))
        self.editConn.setText(_translate("ConnDlg", "Edit"))
        self.testConn.setText(_translate("ConnDlg", "Test"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("ConnDlg", "Name"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("ConnDlg", "DB Server"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("ConnDlg", "Status"))
