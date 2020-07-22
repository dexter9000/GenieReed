import json
import math

from PyQt5 import QtWidgets
from PyQt5.QtGui import QCursor
from PyQt5.QtWidgets import QWidget, QMenu, QAction, QMessageBox, QHeaderView

from es.EsParser import EsParser
from gui.DragLabel import DragLabel
from gui.FilterComboBox import FComboBox
from gui.QueryField import QueryField
from gui.SignalThread import SignalThread
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

    def setIgnoreNone(self, ignoreNone):
        self.isIgnoreNone = ignoreNone
        pass

    def initSetupUi(self):
        self.fieldNames = EsParser.getFullFieldNames(self.pattern)
        self.splitter.setStyleSheet("QSplitter::handle { background-color: white; }")
        self.btn_pre_page.setEnabled(False)
        self.btn_next_page.setEnabled(False)
        self.initBasicQuery()
        self.dragLabel = DragLabel(self.dragField)
        self.field_area_layout.addWidget(self.dragLabel)
        self.search_progress.setVisible(False)

        self.tree_result.header().setSectionResizeMode(QHeaderView.ResizeToContents|QHeaderView.Custom)

    def updateUi(self):
        if self.totalPage > self.page:
            self.btn_next_page.setEnabled(True)
        else:
            self.btn_next_page.setEnabled(False)

        if self.page > 1:
            self.btn_pre_page.setEnabled(True)
        else:
            self.btn_pre_page.setEnabled(False)

    def initAction(self):
        self.btn_query.clicked.connect(self.search)
        self.btn_pre_page.clicked.connect(self.toPrePage)
        self.btn_next_page.clicked.connect(self.toNextPage)
        self.table_result.doubleClicked.connect(self.openViewDocument)
        # self.table_result.itemEntered.connect(self.showItem)
        self.table_result.customContextMenuRequested.connect(self.docRightMenuShow)
        self.txt_page.editingFinished.connect(self.toPage)
        self.btn_ignore_null.toggled.connect(self.tree_result.setIgnoreNone)

    def initBasicQuery(self):
        self.addField()
        self.initSource()

    def initSource(self):
        self.combo_include.addItems(self.fieldNames)
        self.combo_exclude.addItems(self.fieldNames)
        self.combo_sort.addItems(self.fieldNames)
        # self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_include)

    def addField(self):
        field_query_line = QueryField(self.fieldNames, self)
        field_query_line.btn_add.clicked.connect(self.addField)
        self.field_group_layout.addWidget(field_query_line)
        self.fields.append(field_query_line)
        return field_query_line

    def dragField(self, e):
        query = {}
        query = e.source().getQuery(e)
        # if (isinstance(e.source(), ResultTable)):
        # elif (isinstance(e.source(), QTreeWidget)):
        #     query = self.getQueryFromTable(e)

        field_query_line = self.addField()
        field_query_line.set_query(query)

    def updateQueryFields(self, target):
        print("QueryWidget::updateQueryFields")
        for index, field in enumerate(self.fields):
            if field == target:
                self.field_group_layout.removeRow(index)
                self.fields.remove(field)
                break
        pass

    def getQuery(self):
        if self.tabWidget.currentWidget() == self.tab_comp:
            query = json.loads(self.text_query.toPlainText())
        else:
            query = self.getQueryFields()
        return query

    def getBasicQuery(self):
        query = {"query": {"bool": {"must": [], "must_not": [], "should": []}},
                 "_source": {"excludes": []}, "sort": [], "aggs": {}}
        query['_source']['includes'] = self.combo_include.selectedItems()
        query['_source']['excludes'] = self.combo_exclude.selectedItems()
        query['sort'] = self.getSortQuery()
        return query

    def getSortQuery(self):
        query = []
        fields = self.combo_sort.selectedItems()
        sort_type = self.combo_sort_type.currentText()
        for field in fields:
            query.append({field: {'order': sort_type}})
        return query

    def getQueryFields(self):
        result = self.getBasicQuery()
        for field in self.fields:
            result['query']['bool'][field.getGroup()].append(field.getQuery())
        if len(result['query']['bool']['must']) == 0 and len(result['query']['bool']['should']) == 0:
            result['query']['bool']['should'].append({"match_all": {}})
        return result

    def initQuery(self):
        query = '{"query": {"bool": {"must": [{"match_all": {}}],"must_not": [],"should": []}},"_source":{"excludes":[]},"sort": [],"aggs": {}}'
        self.text_query.setPlainText(query)

    def search(self):
        my_thread = SignalThread(self.searchFn)
        my_thread.my_signal.connect(self.searchSignalFn)
        my_thread.start()
        self.search_progress.setVisible(True)

    def searchFn(self):
        query = self.getQuery()
        self.page = int(self.txt_page.text())
        self.size = int(self.txt_size.text())
        return self.es.search(self.index, query, self.page, self.size)

    def searchSignalFn(self, result):
        if result['result'] == 'succ':
            self.table_result.addTableResult(result['data'])
            self.tree_result.addTreeResult(result['data'])
            self.addJsonResult(result['data'])
            self.label_total.setText(str(self.es.total))
            self.totalPage = math.ceil(self.es.total / self.size)
            self.page_info.setText('Document ' + str(self.page) + ' of ' + str(self.totalPage))
            self.updateUi()
        elif result['result'] == 'error':
            QMessageBox.critical(self, "失败", "查询失败")
        self.search_progress.setVisible(False)

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
