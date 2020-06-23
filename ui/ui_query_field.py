# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_query_field.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(400, 300)
        self.horizontalLayout = QtWidgets.QHBoxLayout(Form)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cond_bool = QtWidgets.QComboBox(Form)
        self.cond_bool.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cond_bool.setObjectName("cond_bool")
        self.cond_bool.addItem("")
        self.cond_bool.addItem("")
        self.cond_bool.addItem("")
        self.horizontalLayout.addWidget(self.cond_bool)
        self.cond_field = QtWidgets.QComboBox(Form)
        self.cond_field.setObjectName("cond_field")
        self.horizontalLayout.addWidget(self.cond_field)
        self.btn_add = QtWidgets.QPushButton(Form)
        self.btn_add.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_del = QtWidgets.QPushButton(Form)
        self.btn_del.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.cond_bool.setItemText(0, _translate("Form", "must"))
        self.cond_bool.setItemText(1, _translate("Form", "must_not"))
        self.cond_bool.setItemText(2, _translate("Form", "should"))
        self.btn_add.setText(_translate("Form", "+"))
        self.btn_del.setText(_translate("Form", "-"))
