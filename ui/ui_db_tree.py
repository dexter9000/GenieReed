# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_db_tree.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_DbTree(object):
    def setupUi(self, DbTree):
        DbTree.setObjectName("DbTree")
        DbTree.resize(400, 300)
        self.verticalLayout = QtWidgets.QVBoxLayout(DbTree)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(DbTree)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon/database_server.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_0.setIcon(0, icon)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icon/collection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item_1.setIcon(0, icon1)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1.setIcon(0, icon1)
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_0.setIcon(0, icon)
        self.verticalLayout.addWidget(self.treeWidget)

        self.retranslateUi(DbTree)
        QtCore.QMetaObject.connectSlotsByName(DbTree)

    def retranslateUi(self, DbTree):
        _translate = QtCore.QCoreApplication.translate
        DbTree.setWindowTitle(_translate("DbTree", "Form"))
        self.treeWidget.headerItem().setText(0, _translate("DbTree", "connections"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("DbTree", "db1"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("DbTree", "index1"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("DbTree", "index2"))
        self.treeWidget.topLevelItem(1).setText(0, _translate("DbTree", "db2"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
from ui import icon_rc
