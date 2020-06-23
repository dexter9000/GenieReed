import json
import math

from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QMenu, QAction
from qtpy import QtWidgets

from es import EsClient
from ui.ui_query_widget import Ui_QueryForm


class QueryWidget(QWidget, Ui_QueryForm):

    def __init__(self, host, index, indeies, pattern, es, parent=None):
        super(QWidget, self).__init__(parent)
        self.index = index
        self.indeies = indeies
        self.host = host
        self.pattern = pattern
        self.es = es
        self.page = 1
        self.size = 10
        self.totalPage = 0
        self.moduleName = []
        self.properties = []
        self.setupUi(self)
        self.initSetupUi()
        self.label_host.setText(host)
        self.label_index.setText(index)
        self.initAction()
        self.initQuery()
        self.lockTableResult()

    def initSetupUi(self):
        self.fieldNames = self.getFieldNames()
        self.combo_include.addItems(self.fieldNames)
        self.combo_exculde.addItems(self.fieldNames)
        self.combo_sort.addItems(self.fieldNames)
        # self.groupBox.add
        self.btn_pre_page.setEnabled(False)
        self.btn_next_page.setEnabled(False)

    def updateUi(self):
        if(self.totalPage > self.page):
            self.btn_next_page.setEnabled(True)
        else:
            self.btn_next_page.setEnabled(False)

        if(self.page > 1):
            self.btn_pre_page.setEnabled(True)
        else:
            self.btn_pre_page.setEnabled(False)

    def getFieldNames(self):
        self.moduleName = []
        for moduleName in self.pattern:
            self.moduleName.append(moduleName)
            result = []
            self.properties = self.pattern[moduleName]['properties']
            for f in self.properties:
                result.append(f)
            result = sorted(result, key=str.lower)
        return result

    def initAction(self):
        self.btn_query.clicked.connect(self.search)
        self.btn_pre_page.clicked.connect(self.toPrePage)
        self.btn_next_page.clicked.connect(self.toNextPage)
        self.table_result.doubleClicked.connect(self.openViewDocument)
        self.table_result.customContextMenuRequested.connect(self.docRightMenuShow)
        self.txt_page.editingFinished.connect(self.toPage)

    def initQuery(self):
        query = '{"query": {"bool": {"must": [{"match_all": {}}],"must_not": [],"should": []}},"_source":{"excludes":["cdp_field_weight"],"includes":["customerSID"]},"sort": [],"aggs": {}}'
        self.text_query.setPlainText(query)

    def addAllIndex(self, indexList):
        self.combo_index.addItems(indexList)

    def search(self):
        query = json.loads(self.text_query.toPlainText())
        result = self.es.search(self.index, query, self.page, self.size)
        self.addTreeResult(result)
        self.addTableResult(result)
        self.addJsonResult(result)
        self.label_total.setText(str(self.es.total))
        self.totalPage = math.ceil(self.es.total / self.size)
        self.page_info.setText('Document ' + str(self.page) + ' of ' + str(self.totalPage))
        self.updateUi()

    def toPrePage(self):
        self.page = int(self.txt_page.text())
        if (self.page > 1):
            self.page = self.page - 1
            self.txt_page.setText(str(self.page))
        self.toPage()

    def toNextPage(self):
        self.page = int(self.txt_page.text())
        if (self.page < self.totalPage):
            self.page = self.page + 1
            self.txt_page.setText(str(self.page))
        self.toPage()

    def toPage(self):
        self.page = int(self.txt_page.text())
        self.size = int(self.txt_size.text())
        self.search()

    def addTableResult(self, result):
        fields = []
        if (isinstance(result, list)):
            if (len(result) <= 0):
                return
            fields = self.getFields(result[0])
        elif (isinstance(result, dict)):
            fields = self.getFields(result)

        self.table_result.setRowCount(0)
        self.table_result.setColumnCount(len(fields))
        self.table_result.setHorizontalHeaderLabels(fields)

        self.table_result.setRowCount(len(result))

        for rowNum, item in enumerate(result):
            self.addTableRow(rowNum, item, fields)
        pass

    def addTableRow(self, rowNum, line, fields):
        for colNum, field in enumerate(fields):
            item = QtWidgets.QTableWidgetItem(str(line[field] or ''))
            self.table_result.setItem(rowNum, colNum, item)

    def getFields(self, doc):
        result = []
        for f in doc:
            result.append(f)
        result = sorted(result, key=str.lower)
        return result

    def addJsonResult(self, result):
        self.json_result.setPlainText(json.dumps(result, sort_keys=True, indent=2))

    def addQuery(self):
        pass

    def removeQuery(self):
        pass

    def unlockTableResult(self):
        self.table_result.setEditTriggers(
            QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.EditKeyPressed)

    def lockTableResult(self):
        self.table_result.setEditTriggers(
            QtWidgets.QAbstractItemView.DoubleClicked | QtWidgets.QAbstractItemView.AnyKeyPressed | QtWidgets.QAbstractItemView.EditKeyPressed)

    def openViewDocument(self):
        doc = self.table_result.currentRow()
        print(doc)
        pass

    def addTreeResult(self, result):
        self.tree_result.clear()
        for doc in result:
            tree = QtWidgets.QTreeWidgetItem(self.tree_result)
            self.addTreeDoc(doc, tree)
        print("")

    def addTreeDoc(self, doc, tree):
        if (isinstance(doc, dict)):
            tree.setText(0, "{doc}")
            self.addTreeDict(doc, tree)
        elif (isinstance(doc, list)):
            i = 0
            for item in doc:
                self.addTreeDict(item, tree.child(i))
                i = i + 1

    def addTreeDict(self, doc, tree):
        for field in doc:
            if (isinstance(doc[field], list)):
                if(len(doc[field]) == 0):
                    child = QtWidgets.QTreeWidgetItem(tree)
                    child.setText(0, field)
                    child.setText(1, '[ ' + str(len(doc[field])) + ' elements ]')
                    child.setText(2, self.properties[field]['type'])
                    continue

                if (isinstance(doc[field][0], dict)):
                    child = QtWidgets.QTreeWidgetItem(tree)
                    self.addTreeDict(doc[field], child)
                else:
                    child = QtWidgets.QTreeWidgetItem(tree)
                    child.setText(0, field)
                    child.setText(1, '[ ' + str(len(doc[field])) + ' elements ')
                    child.setText(2, self.properties[field]['type'])
                    for i, item in enumerate(doc[field]):
                        child = QtWidgets.QTreeWidgetItem(child)
                        child.setText(0, str(i))
                        child.setText(1, str(item))
            else:
                child = QtWidgets.QTreeWidgetItem(tree)
                child.setText(0, field)
                child.setText(1, str(doc[field]))
                child.setText(2, self.properties[field]['type'])

    def docRightMenuShow(self, pos):  # 添加右键菜单
        menu = QMenu(self)
        menu.addAction(QAction('Edit', menu))
        menu.addAction(QAction('View', menu))
        menu.addAction(QAction('Copy', menu))
        # menu.triggered.connect(self.menuSlot)
        menu.exec_(QCursor.pos())
