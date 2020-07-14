import json
import math

from PyQt5 import QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QMenu, QAction

from es.EsParser import EsParser
from gui.FilterComboBox import FComboBox
from gui.QueryField import QueryField
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
        self.fields = []
        self.setupUi(self)
        self.initSetupUi()
        self.label_host.setText(host)
        self.label_index.setText(index)
        self.initAction()
        self.initQuery()
        self.lockTableResult()
        self.isIgnoreNone = self.btn_ignore_null.isChecked()

    def initSetupUi(self):
        self.fieldNames = EsParser.getFullFieldNames(self.pattern)
        self.fieldNames.insert(0, '')
        # self.combo_include.addItems(self.fieldNames)
        # self.combo_include.setCurrentIndex(-1)
        # self.combo_exculde.addItems(self.fieldNames)
        # self.combo_sort.addItems(self.fieldNames)
        # self.groupBox.add
        self.btn_pre_page.setEnabled(False)
        self.btn_next_page.setEnabled(False)
        # self.tree_result.header().setResizeMode(QHeaderView.ResizeToContents)
        self.initBasicQuery()

    def updateUi(self):
        if (self.totalPage > self.page):
            self.btn_next_page.setEnabled(True)
        else:
            self.btn_next_page.setEnabled(False)

        if (self.page > 1):
            self.btn_pre_page.setEnabled(True)
        else:
            self.btn_pre_page.setEnabled(False)

    def initBasicQuery(self):
        self.addField()
        self.initSource()

    def initAction(self):
        self.btn_query.clicked.connect(self.search)
        self.btn_pre_page.clicked.connect(self.toPrePage)
        self.btn_next_page.clicked.connect(self.toNextPage)
        self.table_result.doubleClicked.connect(self.openViewDocument)
        # self.table_result.itemEntered.connect(self.showItem)
        self.table_result.customContextMenuRequested.connect(self.docRightMenuShow)
        self.txt_page.editingFinished.connect(self.toPage)
        self.btn_ignore_null.toggled.connect(self.ignoreNone)
        self.field_group.setAcceptDrops(True)

    def initSource(self):
        print('initSource')
        self.combo_include = FComboBox(self.group_other)
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_include)
        pass

    def dropEvent(self, QDropEvent):
        pass

    def dragEnterEvent(self, QDragEnterEvent):
        pass

    def addField(self):
        field_query_line = QueryField(self.fieldNames, self)
        field_query_line.btn_add.clicked.connect(self.addField)
        # field_query_line.btn_del.clicked.connect(self.delField)
        self.field_group_layout.addWidget(field_query_line)
        self.fields.append(field_query_line)

    def updateQueryFields(self, target):
        print("QueryWidget::updateQueryFields")
        for index, field in enumerate(self.fields):
            if field == target:
                self.field_group_layout.removeRow(index)
                self.fields.remove(field)
                break
        pass

    def getQueryFields(self):
        result = self.getBasicQuery()

        for field in self.fields:
            result['query']['bool'][field.getGroup()].append(field.getQuery())
        return result

    def ignoreNone(self, ignore):
        self.isIgnoreNone = ignore

    def getBasicQuery(self):
        return {"query": {"bool": {"must": [], "must_not": [], "should": []}},
                "_source": {"excludes": []}, "sort": [], "aggs": {}}

    def initQuery(self):
        query = '{"query": {"bool": {"must": [{"match_all": {}}],"must_not": [],"should": []}},"_source":{"excludes":[]},"sort": [],"aggs": {}}'
        self.text_query.setPlainText(query)

    def addAllIndex(self, indexList):
        self.combo_index.addItems(indexList)

    def search(self):
        query = self.getQuery()
        result = self.es.search(self.index, query, self.page, self.size)
        self.addTableResult(result)
        self.addTreeResult(result)
        self.addJsonResult(result)
        self.label_total.setText(str(self.es.total))
        self.totalPage = math.ceil(self.es.total / self.size)
        self.page_info.setText('Document ' + str(self.page) + ' of ' + str(self.totalPage))
        self.updateUi()

    def getQuery(self):
        if self.tabWidget.currentWidget() == self.tab_comp:
            query = json.loads(self.text_query.toPlainText())
        else:
            query = self.getQueryFields()
            print(query)
            # query = json.loads(
            #     '{"query": {"bool": {"must": [{"match_all": {}}],"must_not": [],"should": []}},"_source":{"includes":["cdp_id"]},"sort": [],"aggs": {}}')
        return query

    def getBasicQuery(self):
        query = json.loads(
            '{"query": {"bool": {"must": [{"match_all": {}}],"must_not": [],"should": []}},"_source":{"includes":[],"excludes":[]},"sort": [],"aggs": {}}')
        if self.combo_include.currentText() != '':
            query['_source']['includes'] = [self.combo_include.currentText()]
        if self.combo_exclude.currentText() != '':
            query['_source']['excludes'] = [self.combo_exclude.currentText()]
        if self.combo_sort.currentText() != '':
            query['sort'] = [self.combo_sort.currentText()]
        return query

    def getBasicFieldQuery(self):

        pass

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
            if field in line:
                item = QtWidgets.QTableWidgetItem(str(line[field]))
                item.setToolTip(str(line[field]))
                self.table_result.setItem(rowNum, colNum, item)

    def getFields(self, doc):
        result = []
        for f in doc:
            result.append(f)
        result = sorted(result, key=str.lower)
        return result

    def addJsonResult(self, result):
        self.json_result.setText(json.dumps(result, ensure_ascii=False, sort_keys=True, indent=2))

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
            self.addTreeRecord(doc, tree)

    def addTreeRecord(self, doc, tree):
        if (isinstance(doc, dict)):
            tree.setText(0, "{doc}")
            tree.setText(1, '{ ' + str(len(doc.keys())) + ' fields }')
            tree.setText(2, 'Document')
            for field in doc:
                self.addTreeDict(field, doc[field], tree)

    def addTreeDict(self, field, doc, tree):
        if (isinstance(doc, list)):
            child = QtWidgets.QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, '[ ' + str(len(doc)) + ' elements ]')
            child.setText(2, self.getFieldType(field))
            for i, item in enumerate(doc):
                self.addTreeDict(str(i), item, child)
            return

        if (isinstance(doc, dict)):
            child = QtWidgets.QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, '{ ' + str(len(doc.keys())) + ' fields }')
            child.setText(2, self.getFieldType(field))
            for field in doc:
                self.addTreeDict(field, doc[field], child)
            return

        if doc is not None or self.isIgnoreNone:
            child = QtWidgets.QTreeWidgetItem(tree)
            child.setText(0, field)
            child.setText(1, str(doc))
            child.setText(2, self.getFieldType(field))

    def getFieldType(self, field):
        if field in self.properties:
            if 'properties' in self.properties[field]:
                return ''
            else:
                return self.properties[field]['type']
        else:
            return ''

    def getFullFieldType(self, field):
        if field in self.properties:
            if 'properties' in self.properties[field]:
                return ''  # TODO
            else:
                return self.properties[field]['type']
        else:
            return ''

    def docRightMenuShow(self, pos):  # 添加右键菜单
        menu = QMenu(self)
        menu.addAction(QAction('Edit', menu))
        menu.addAction(QAction('View', menu))
        menu.addAction(QAction('Copy', menu))
        # menu.triggered.connect(self.menuSlot)
        menu.exec_(QCursor.pos())
