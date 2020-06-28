# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_filter_combobox.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_FilterComboBox(object):
    def setupUi(self, FilterComboBox):
        FilterComboBox.setObjectName("FilterComboBox")
        FilterComboBox.resize(331, 142)
        FilterComboBox.setMaximumSize(QtCore.QSize(16777215, 142))
        self.verticalLayout = QtWidgets.QVBoxLayout(FilterComboBox)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.lineEdit = QtWidgets.QLineEdit(FilterComboBox)
        self.lineEdit.setMaximumSize(QtCore.QSize(16777215, 22))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.comboBox = QtWidgets.QComboBox(FilterComboBox)
        self.comboBox.setMaximumSize(QtCore.QSize(22, 22))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout.addWidget(self.comboBox)
        self.verticalLayout.addLayout(self.horizontalLayout)
        self.listView = QtWidgets.QListView(FilterComboBox)
        self.listView.setMaximumSize(QtCore.QSize(16777215, 0))
        self.listView.setObjectName("listView")
        self.verticalLayout.addWidget(self.listView)

        self.retranslateUi(FilterComboBox)
        QtCore.QMetaObject.connectSlotsByName(FilterComboBox)

    def retranslateUi(self, FilterComboBox):
        _translate = QtCore.QCoreApplication.translate
        FilterComboBox.setWindowTitle(_translate("FilterComboBox", "Form"))
