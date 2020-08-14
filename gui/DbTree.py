from PyQt5.QtCore import Qt
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QMenu, QAction

from ui.ui_db_tree import Ui_DbTree


class DbTree(QWidget, Ui_DbTree):

    def __init__(self, parent=None):
        super(DbTree, self).__init__(parent)
        self.setupUi(self)
        self.initSetupUi()

    def initSetupUi(self):
        # DbIndexForm.setObjectName("DbIndexForm")
        # self.setGeometry(QtCore.QRect(0, 0, 85, 425))
        self.treeWidget.setContextMenuPolicy(Qt.CustomContextMenu)
        # self.treeWidget.customContextMenuRequested.connect(self.connRightMenuShow)
        self.treeWidget.customContextMenuRequested.connect(self.connRightMenuShow)

    def add_host(self, result):
        pass

    def add_index_item(self, host, result):
        pass

    def testHost(self):
        # self.
        pass

    def connRightMenuShow(self, pos):  # 添加右键菜单
        curItem = self.treeWidget.currentItem()
        if (curItem == None): return
        menu = QMenu(self)
        disconnect = QAction('Disconnect', menu)
        disconnect.triggered.connect(self.disconnect)
        menu.addAction(disconnect)
        menu.addAction(QAction('Status', menu))
        menu.exec_(QCursor.pos())

    def disconnect(self):
        print("disconnect")
        pass