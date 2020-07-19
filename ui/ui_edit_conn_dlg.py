# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_edit_conn_dlg.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(400, 300)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(Dialog)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame = QtWidgets.QFrame(Dialog)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.formLayout = QtWidgets.QFormLayout(self.frame)
        self.formLayout.setLabelAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.frame)
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.txt_name = QtWidgets.QLineEdit(self.frame)
        self.txt_name.setObjectName("txt_name")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.txt_name)
        self.label_2 = QtWidgets.QLabel(self.frame)
        self.label_2.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.txt_host = QtWidgets.QLineEdit(self.frame)
        self.txt_host.setObjectName("txt_host")
        self.formLayout.setWidget(1, QtWidgets.QFormLayout.FieldRole, self.txt_host)
        self.label_3 = QtWidgets.QLabel(self.frame)
        self.label_3.setObjectName("label_3")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_3)
        self.txt_port = QtWidgets.QLineEdit(self.frame)
        self.txt_port.setObjectName("txt_port")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.txt_port)
        self.verticalLayout.addWidget(self.frame)
        self.verticalLayout_2.addLayout(self.verticalLayout)
        spacerItem = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_2.addItem(spacerItem)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_test_connect = QtWidgets.QPushButton(Dialog)
        self.btn_test_connect.setObjectName("btn_test_connect")
        self.horizontalLayout_2.addWidget(self.btn_test_connect)
        self.test_progress = QtWidgets.QProgressBar(Dialog)
        self.test_progress.setEnabled(True)
        self.test_progress.setProperty("value", 99)
        self.test_progress.setTextVisible(False)
        self.test_progress.setObjectName("test_progress")
        self.horizontalLayout_2.addWidget(self.test_progress)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.horizontalLayout_2.addWidget(self.buttonBox)
        self.verticalLayout_2.addLayout(self.horizontalLayout_2)

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Edit Connect"))
        self.label.setText(_translate("Dialog", "Connection Name:"))
        self.label_2.setText(_translate("Dialog", "Host:"))
        self.label_3.setText(_translate("Dialog", "Port:"))
        self.btn_test_connect.setText(_translate("Dialog", "Test Connect"))
