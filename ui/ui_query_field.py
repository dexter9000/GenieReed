# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_query_field.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QueryField(object):
    def setupUi(self, QueryField):
        QueryField.setObjectName("QueryField")
        QueryField.resize(400, 37)
        QueryField.setMaximumSize(QtCore.QSize(16777215, 37))
        self.horizontalLayout = QtWidgets.QHBoxLayout(QueryField)
        self.horizontalLayout.setContentsMargins(-1, 2, -1, 2)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.cond_bool = QtWidgets.QComboBox(QueryField)
        self.cond_bool.setMaximumSize(QtCore.QSize(100, 16777215))
        self.cond_bool.setObjectName("cond_bool")
        self.cond_bool.addItem("")
        self.cond_bool.setItemText(0, "must")
        self.cond_bool.addItem("")
        self.cond_bool.setItemText(1, "must_not")
        self.cond_bool.addItem("")
        self.cond_bool.setItemText(2, "should")
        self.horizontalLayout.addWidget(self.cond_bool)
        self.cond_field = QtWidgets.QComboBox(QueryField)
        self.cond_field.setMaximumSize(QtCore.QSize(200, 16777215))
        self.cond_field.setObjectName("cond_field")
        self.horizontalLayout.addWidget(self.cond_field)
        self.widget = QtWidgets.QWidget(QueryField)
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.cond_operator = QtWidgets.QComboBox(self.widget)
        self.cond_operator.setObjectName("cond_operator")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.cond_operator.addItem("")
        self.horizontalLayout_2.addWidget(self.cond_operator)
        self.cond_value = QtWidgets.QLineEdit(self.widget)
        self.cond_value.setObjectName("cond_value")
        self.horizontalLayout_2.addWidget(self.cond_value)
        self.horizontalLayout.addWidget(self.widget)
        self.btn_add = QtWidgets.QPushButton(QueryField)
        self.btn_add.setMinimumSize(QtCore.QSize(20, 0))
        self.btn_add.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btn_add.setObjectName("btn_add")
        self.horizontalLayout.addWidget(self.btn_add)
        self.btn_del = QtWidgets.QPushButton(QueryField)
        self.btn_del.setMinimumSize(QtCore.QSize(20, 0))
        self.btn_del.setMaximumSize(QtCore.QSize(20, 16777215))
        self.btn_del.setObjectName("btn_del")
        self.horizontalLayout.addWidget(self.btn_del)

        self.retranslateUi(QueryField)
        QtCore.QMetaObject.connectSlotsByName(QueryField)

    def retranslateUi(self, QueryField):
        _translate = QtCore.QCoreApplication.translate
        QueryField.setWindowTitle(_translate("QueryField", "Form"))
        self.cond_operator.setItemText(0, _translate("QueryField", "match"))
        self.cond_operator.setItemText(1, _translate("QueryField", "text"))
        self.cond_operator.setItemText(2, _translate("QueryField", "term"))
        self.cond_operator.setItemText(3, _translate("QueryField", "wildcard"))
        self.cond_operator.setItemText(4, _translate("QueryField", "prefix"))
        self.cond_operator.setItemText(5, _translate("QueryField", "fuzzy"))
        self.cond_operator.setItemText(6, _translate("QueryField", "range"))
        self.cond_operator.setItemText(7, _translate("QueryField", "query_string"))
        self.cond_operator.setItemText(8, _translate("QueryField", "missing"))
        self.btn_add.setText(_translate("QueryField", "+"))
        self.btn_del.setText(_translate("QueryField", "-"))
