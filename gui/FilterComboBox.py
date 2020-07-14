from PyQt5.QtCore import QModelIndex, QSize, Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QListWidget, QComboBox, QLineEdit, QListView, QCheckBox, QHBoxLayout, \
    QListWidgetItem


class CheckedItem(QWidget):
    def __init__(self, text, parent=None):
        super(QWidget, self).__init__(parent)
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.checkbox = QCheckBox(self)
        self.checkbox.setMaximumWidth(1000)
        self.checkbox.setCheckable(True)
        self.checkbox.setCheckState(Qt.Unchecked)
        self.checkbox.setText(text)
        self.layout.addWidget(self.checkbox)

    def sizeHint(self):
        # 决定item的高度
        return QSize(200, 22)


class FilterComboBox(QComboBox):

    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.items = []
        self.setupUi()
        self.initAction()

    def setupUi(self):
        # self.setEditable(True)
        # dataList = QListWidget(self)
        # dataList.addItem('111')
        # dataList.addItem('112')
        self.dataListView = QListView()
        self._model = QStandardItemModel(self.dataListView)
        self.dataListView.setModel(self._model)

        self.addItem("111")
        self.addItem("122")

        self.setView(self.dataListView)
        # self.setModel(dataList.model())
        pLineEdit = QLineEdit(self)
        self.setLineEdit(pLineEdit)
        qss = '''QComboBox QAbstractItemView::item {
                    height: 25px;
                }
                QListView::item:hover {
                    background: #BDD7FD;
                }'''
        self.setStyleSheet(qss)

    def initAction(self):
        self.activated.connect(self.setTopText)
        pass

    def setTopText(self):
        pass

    def addItem(self, str):
        self.items.append(str)
        item = QStandardItem()
        self._model.appendRow(item)  # 添加item

        index = self._model.indexFromItem(item)
        widget = CheckedItem(str)
        # item.setSizeHint(widget.sizeHint())  # 主要是调整item的高度
        self.dataListView.setIndexWidget(index, widget)
        pass

    def addItems(self, items):
        for item in items:
            self.addItem(item)
        pass

    def showList(self):
        self.listView.setMinimumHeight(100)
        self.listView.setMaximumHeight(200)
        pass

    def hideList(self):
        pass


class FComboBox(QComboBox):
    def __init__(self, parent=None):
        super(QComboBox, self).__init__(parent)
        self.itemCheckBoxes = []
        self.items = []
        self.setupUi()

    def setupUi(self):
        self.pListWidget = QListWidget(self)
        self.pLineEdit = QLineEdit(self)
        for i in range(5):
            self.addItem(str(i))
            # pItem = QListWidgetItem(pListWidget)
            # pListWidget.addItem(pItem)
            # pItem.setData(Qt.UserRole, i)
            # pCheckBox = QCheckBox(self)
            # pCheckBox.setText(str(i))
            # pListWidget.addItem(pItem)
            # pListWidget.setItemWidget(pItem, pCheckBox)
            # connect(pCheckBox, SIGNAL(stateChanged(int)), this, SLOT(stateChanged(int)))

        self.setModel(self.pListWidget.model())
        self.setView(self.pListWidget)
        self.setLineEdit(self.pLineEdit)
        self.setEditable(True)
        # pLineEdit.setReadOnly(True)
        self.pListWidget.itemClicked.connect(self.selectClick)
        self.pLineEdit.textChanged.connect(self.textChanged)

    def addItem(self, text):
        pItem = QListWidgetItem(self.pListWidget)
        self.pListWidget.addItem(pItem)
        pItem.setData(Qt.UserRole, text)
        pCheckBox = QCheckBox(self)
        pCheckBox.setText(text)

        qss = 'QCheckBox {margin-left: 10px;}'
        pCheckBox.setStyleSheet(qss)

        self.pListWidget.addItem(pItem)
        self.pListWidget.setItemWidget(pItem, pCheckBox)

        pCheckBox.stateChanged.connect(self.stateChanged)
        self.items.append(text)
        self.itemCheckBoxes.append(pCheckBox)

    def selectClick(self):
        print('click')
        pass

    def stateChanged(self, p_int):
        print("stateChanged")
        strs = map(lambda x: x.text(), filter(lambda x: x.isChecked(), self.itemCheckBoxes))
        txt = ",".join(str(i) for i in strs)
        self.pLineEdit.setText(txt)
        pass

    def textChanged(self, p_str):
        pass

    def filterItems(self, text):

        pass
