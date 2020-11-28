from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QMenu, QAction, QWidget


class DbIndexForm(QWidget):

    def __init__(self, action, host, username, password, parent=None):
        super(QWidget, self).__init__(parent)
        self.setupUi(self)
        self.action = action
        self.host = host
        self.username = username
        self.password = password
        self.indeies = []
        self.initAction()


    def setupUi(self, DbIndexForm):
        DbIndexForm.setObjectName("DbIndexForm")
        self.setGeometry(QtCore.QRect(0, 0, 85, 425))
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.connRightMenuShow)

        self.filterEdit = QtWidgets.QLineEdit(DbIndexForm)
        self.dbListWidget = QtWidgets.QListWidget(DbIndexForm)
        self.dbListWidget.setObjectName("dbListWidget")
        self.dbListWidget.itemDoubleClicked.connect(self.selectIndex)
        self.dbListWidget.setSortingEnabled(True)
        verticalLayout = QtWidgets.QVBoxLayout(DbIndexForm)
        verticalLayout.setObjectName("verticalLayout")
        verticalLayout.addWidget(self.filterEdit)
        verticalLayout.addWidget(self.dbListWidget)

        self.retranslateUi(DbIndexForm)
        QtCore.QMetaObject.connectSlotsByName(DbIndexForm)

    def retranslateUi(self, DbIndexForm):
        _translate = QtCore.QCoreApplication.translate
        DbIndexForm.setWindowTitle(_translate("DbIndexForm", "Form"))

    def initAction(self):
        self.filterEdit.textChanged.connect(self.filterChange)
        pass

    def connRightMenuShow(self, pos):   #添加右键菜单
        menu = QMenu(self)
        menu.addAction(QAction('Info', menu))
        menu.addAction(QAction('Status', menu))
        # menu.triggered.connect(self.menuSlot)
        menu.exec_(QCursor.pos())

    def addColl(self, collName):
        self.indeies.append(collName)
        item = QtWidgets.QListWidgetItem()
        item.setText(collName)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon/collection.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        item.setIcon(icon)
        item.setToolTip(collName)
        self.dbListWidget.addItem(item)

    def filterChange(self):
        print(self.filterEdit.text())

    def selectIndex(self):
        index = self.dbListWidget.currentItem().text()
        self.action.selectIndex(self.host, self.username, self.password, index, self.indeies)
