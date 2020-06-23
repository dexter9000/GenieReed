# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_tree_view.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(479, 384)
        self.verticalLayout = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout.setObjectName("verticalLayout")
        self.treeWidget = QtWidgets.QTreeWidget(Dialog)
        self.treeWidget.setObjectName("treeWidget")
        item_0 = QtWidgets.QTreeWidgetItem(self.treeWidget)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_1 = QtWidgets.QTreeWidgetItem(item_0)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        item_2 = QtWidgets.QTreeWidgetItem(item_1)
        self.verticalLayout.addWidget(self.treeWidget)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout.addWidget(self.buttonBox)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.treeWidget.headerItem().setText(0, _translate("Dialog", "Key"))
        self.treeWidget.headerItem().setText(1, _translate("Dialog", "Value"))
        self.treeWidget.headerItem().setText(2, _translate("Dialog", "Type"))
        __sortingEnabled = self.treeWidget.isSortingEnabled()
        self.treeWidget.setSortingEnabled(False)
        self.treeWidget.topLevelItem(0).setText(0, _translate("Dialog", "doc"))
        self.treeWidget.topLevelItem(0).child(0).setText(0, _translate("Dialog", "name"))
        self.treeWidget.topLevelItem(0).child(0).setText(1, _translate("Dialog", "Alex"))
        self.treeWidget.topLevelItem(0).child(0).setText(2, _translate("Dialog", "String"))
        self.treeWidget.topLevelItem(0).child(1).setText(0, _translate("Dialog", "address"))
        self.treeWidget.topLevelItem(0).child(1).setText(2, _translate("Dialog", "Object"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(0, _translate("Dialog", "city"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(1, _translate("Dialog", "NanJing"))
        self.treeWidget.topLevelItem(0).child(1).child(0).setText(2, _translate("Dialog", "String"))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(0, _translate("Dialog", "zip"))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(1, _translate("Dialog", "20000"))
        self.treeWidget.topLevelItem(0).child(1).child(1).setText(2, _translate("Dialog", "Number"))
        self.treeWidget.setSortingEnabled(__sortingEnabled)
