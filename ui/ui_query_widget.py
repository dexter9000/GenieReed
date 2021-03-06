# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'ui_query_widget.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_QueryForm(object):
    def setupUi(self, QueryForm):
        QueryForm.setObjectName("QueryForm")
        QueryForm.resize(800, 706)
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(QueryForm)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.layout_line1 = QtWidgets.QHBoxLayout()
        self.layout_line1.setContentsMargins(10, -1, -1, -1)
        self.layout_line1.setObjectName("layout_line1")
        self.layout_line2 = QtWidgets.QHBoxLayout()
        self.layout_line2.setContentsMargins(-1, -1, -1, 0)
        self.layout_line2.setObjectName("layout_line2")
        self.btn_query = QtWidgets.QPushButton(QueryForm)
        self.btn_query.setMaximumSize(QtCore.QSize(22, 22))
        self.btn_query.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(":/resources/icon/execute.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_query.setIcon(icon)
        self.btn_query.setObjectName("btn_query")
        self.layout_line2.addWidget(self.btn_query)
        self.btn_query_selected = QtWidgets.QPushButton(QueryForm)
        self.btn_query_selected.setEnabled(False)
        self.btn_query_selected.setMaximumSize(QtCore.QSize(22, 22))
        self.btn_query_selected.setText("")
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(":/resources/icon/execute_selection_gt.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_query_selected.setIcon(icon1)
        self.btn_query_selected.setObjectName("btn_query_selected")
        self.layout_line2.addWidget(self.btn_query_selected)
        self.layout_line1.addLayout(self.layout_line2)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.layout_line1.addItem(spacerItem)
        self.ico_host = QtWidgets.QLabel(QueryForm)
        self.ico_host.setText("")
        self.ico_host.setPixmap(QtGui.QPixmap(":/resources/icon/computer_link.png"))
        self.ico_host.setObjectName("ico_host")
        self.layout_line1.addWidget(self.ico_host)
        self.label_host = QtWidgets.QLabel(QueryForm)
        self.label_host.setObjectName("label_host")
        self.layout_line1.addWidget(self.label_host)
        self.ico_index = QtWidgets.QLabel(QueryForm)
        self.ico_index.setText("")
        self.ico_index.setPixmap(QtGui.QPixmap(":/resources/icon/wrap_off.png"))
        self.ico_index.setObjectName("ico_index")
        self.layout_line1.addWidget(self.ico_index)
        self.label_index = QtWidgets.QLabel(QueryForm)
        self.label_index.setObjectName("label_index")
        self.layout_line1.addWidget(self.label_index)
        self.verticalLayout_9.addLayout(self.layout_line1)
        self.splitter = QtWidgets.QSplitter(QueryForm)
        self.splitter.setOrientation(QtCore.Qt.Vertical)
        self.splitter.setObjectName("splitter")
        self.query_view = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(4)
        sizePolicy.setHeightForWidth(self.query_view.sizePolicy().hasHeightForWidth())
        self.query_view.setSizePolicy(sizePolicy)
        self.query_view.setObjectName("query_view")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.query_view)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setSpacing(4)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.tabWidget = QtWidgets.QTabWidget(self.query_view)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setObjectName("tabWidget")
        self.tab_comp = QtWidgets.QWidget()
        self.tab_comp.setObjectName("tab_comp")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_comp)
        self.verticalLayout.setObjectName("verticalLayout")
        self.text_query = QtWidgets.QPlainTextEdit(self.tab_comp)
        self.text_query.setObjectName("text_query")
        self.verticalLayout.addWidget(self.text_query)
        self.tabWidget.addTab(self.tab_comp, "")
        self.tab_simple = QtWidgets.QWidget()
        self.tab_simple.setEnabled(True)
        self.tab_simple.setStyleSheet("")
        self.tab_simple.setObjectName("tab_simple")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout(self.tab_simple)
        self.horizontalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        self.splitter_simple = QtWidgets.QSplitter(self.tab_simple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.splitter_simple.sizePolicy().hasHeightForWidth())
        self.splitter_simple.setSizePolicy(sizePolicy)
        self.splitter_simple.setStyleSheet("")
        self.splitter_simple.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_simple.setObjectName("splitter_simple")
        self.group_field = QtWidgets.QGroupBox(self.splitter_simple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(14)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_field.sizePolicy().hasHeightForWidth())
        self.group_field.setSizePolicy(sizePolicy)
        self.group_field.setAcceptDrops(False)
        self.group_field.setObjectName("group_field")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.group_field)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.scrollArea = QtWidgets.QScrollArea(self.group_field)
        self.scrollArea.setAcceptDrops(False)
        self.scrollArea.setAutoFillBackground(False)
        self.scrollArea.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.field_area = QtWidgets.QWidget()
        self.field_area.setGeometry(QtCore.QRect(0, 0, 317, 86))
        self.field_area.setAcceptDrops(False)
        self.field_area.setObjectName("field_area")
        self.field_area_layout = QtWidgets.QVBoxLayout(self.field_area)
        self.field_area_layout.setContentsMargins(0, 0, 0, 0)
        self.field_area_layout.setObjectName("field_area_layout")
        self.field_group_layout = QtWidgets.QFormLayout()
        self.field_group_layout.setObjectName("field_group_layout")
        self.field_area_layout.addLayout(self.field_group_layout)
        self.scrollArea.setWidget(self.field_area)
        self.verticalLayout_3.addWidget(self.scrollArea)
        self.group_other = QtWidgets.QGroupBox(self.splitter_simple)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(6)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.group_other.sizePolicy().hasHeightForWidth())
        self.group_other.setSizePolicy(sizePolicy)
        self.group_other.setObjectName("group_other")
        self.formLayout = QtWidgets.QFormLayout(self.group_other)
        self.formLayout.setContentsMargins(4, 0, 4, 0)
        self.formLayout.setHorizontalSpacing(3)
        self.formLayout.setObjectName("formLayout")
        self.label = QtWidgets.QLabel(self.group_other)
        self.label.setMinimumSize(QtCore.QSize(50, 0))
        self.label.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label.setObjectName("label")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.label)
        self.combo_include = FComboBox(self.group_other)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.combo_include.sizePolicy().hasHeightForWidth())
        self.combo_include.setSizePolicy(sizePolicy)
        self.combo_include.setObjectName("combo_include")
        self.formLayout.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_include)
        self.label_2 = QtWidgets.QLabel(self.group_other)
        self.label_2.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_2.setObjectName("label_2")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.LabelRole, self.label_2)
        self.combo_exclude = FComboBox(self.group_other)
        self.combo_exclude.setObjectName("combo_exclude")
        self.formLayout.setWidget(2, QtWidgets.QFormLayout.FieldRole, self.combo_exclude)
        self.label_4 = QtWidgets.QLabel(self.group_other)
        self.label_4.setMaximumSize(QtCore.QSize(70, 16777215))
        self.label_4.setObjectName("label_4")
        self.formLayout.setWidget(5, QtWidgets.QFormLayout.LabelRole, self.label_4)
        self.formLayout_sort = QtWidgets.QFormLayout()
        self.formLayout_sort.setObjectName("formLayout_sort")
        self.combo_sort_type = QtWidgets.QComboBox(self.group_other)
        self.combo_sort_type.setMinimumSize(QtCore.QSize(70, 0))
        self.combo_sort_type.setMaximumSize(QtCore.QSize(60, 16777215))
        self.combo_sort_type.setObjectName("combo_sort_type")
        self.combo_sort_type.addItem("")
        self.combo_sort_type.addItem("")
        self.formLayout_sort.setWidget(0, QtWidgets.QFormLayout.LabelRole, self.combo_sort_type)
        self.combo_sort = FComboBox(self.group_other)
        self.combo_sort.setObjectName("combo_sort")
        self.formLayout_sort.setWidget(0, QtWidgets.QFormLayout.FieldRole, self.combo_sort)
        self.formLayout.setLayout(5, QtWidgets.QFormLayout.FieldRole, self.formLayout_sort)
        self.horizontalLayout_7.addWidget(self.splitter_simple)
        self.tabWidget.addTab(self.tab_simple, "")
        self.verticalLayout_8.addWidget(self.tabWidget)
        self.result_view = QtWidgets.QWidget(self.splitter)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(16)
        sizePolicy.setHeightForWidth(self.result_view.sizePolicy().hasHeightForWidth())
        self.result_view.setSizePolicy(sizePolicy)
        self.result_view.setObjectName("result_view")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.result_view)
        self.verticalLayout_4.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_4.setSpacing(16)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.widget_4 = QtWidgets.QWidget(self.result_view)
        self.widget_4.setObjectName("widget_4")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.widget_4)
        self.verticalLayout_5.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.tabs_result = QtWidgets.QTabWidget(self.widget_4)
        self.tabs_result.setObjectName("tabs_result")
        self.tab_table = QtWidgets.QWidget()
        self.tab_table.setObjectName("tab_table")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab_table)
        self.verticalLayout_6.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.table_result = ResultTable(self.tab_table)
        self.table_result.setEditTriggers(QtWidgets.QAbstractItemView.AnyKeyPressed|QtWidgets.QAbstractItemView.EditKeyPressed)
        self.table_result.setObjectName("table_result")
        self.table_result.setColumnCount(0)
        self.table_result.setRowCount(0)
        self.verticalLayout_6.addWidget(self.table_result)
        self.tabs_result.addTab(self.tab_table, "")
        self.tab_tree = QtWidgets.QWidget()
        self.tab_tree.setObjectName("tab_tree")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.tab_tree)
        self.verticalLayout_7.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.tree_result = ResultTree(self.tab_tree)
        self.tree_result.setAcceptDrops(False)
        self.tree_result.setWordWrap(True)
        self.tree_result.setObjectName("tree_result")
        self.tree_result.headerItem().setText(0, "Key")
        self.tree_result.header().setCascadingSectionResizes(True)
        self.tree_result.header().setDefaultSectionSize(300)
        self.tree_result.header().setHighlightSections(True)
        self.tree_result.header().setMinimumSectionSize(50)
        self.tree_result.header().setSortIndicatorShown(False)
        self.tree_result.header().setStretchLastSection(True)
        self.verticalLayout_7.addWidget(self.tree_result)
        self.tabs_result.addTab(self.tab_tree, "")
        self.tab_json = QtWidgets.QWidget()
        self.tab_json.setObjectName("tab_json")
        self.verticalLayout_10 = QtWidgets.QVBoxLayout(self.tab_json)
        self.verticalLayout_10.setContentsMargins(2, 2, 2, 2)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.json_result = QtWidgets.QTextBrowser(self.tab_json)
        font = QtGui.QFont()
        font.setFamily("Consolas")
        font.setPointSize(10)
        self.json_result.setFont(font)
        self.json_result.setObjectName("json_result")
        self.verticalLayout_10.addWidget(self.json_result)
        self.tabs_result.addTab(self.tab_json, "")
        self.verticalLayout_5.addWidget(self.tabs_result)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setContentsMargins(0, 0, -1, -1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label_5 = QtWidgets.QLabel(self.widget_4)
        self.label_5.setObjectName("label_5")
        self.horizontalLayout.addWidget(self.label_5)
        self.label_total = QtWidgets.QLabel(self.widget_4)
        self.label_total.setObjectName("label_total")
        self.horizontalLayout.addWidget(self.label_total)
        self.search_progress = QtWidgets.QProgressBar(self.widget_4)
        self.search_progress.setMaximumSize(QtCore.QSize(100, 16777215))
        self.search_progress.setProperty("value", 99)
        self.search_progress.setTextVisible(False)
        self.search_progress.setObjectName("search_progress")
        self.horizontalLayout.addWidget(self.search_progress)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setContentsMargins(-1, 0, -1, -1)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.btn_lock = QtWidgets.QPushButton(self.widget_4)
        self.btn_lock.setEnabled(False)
        self.btn_lock.setText("")
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(":/resources/icon/unlocked.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_lock.setIcon(icon2)
        self.btn_lock.setObjectName("btn_lock")
        self.horizontalLayout_2.addWidget(self.btn_lock)
        self.btn_ignore_null = QtWidgets.QPushButton(self.widget_4)
        self.btn_ignore_null.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_ignore_null.setCheckable(True)
        self.btn_ignore_null.setObjectName("btn_ignore_null")
        self.horizontalLayout_2.addWidget(self.btn_ignore_null)
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem2)
        self.btn_pre_page = QtWidgets.QPushButton(self.widget_4)
        self.btn_pre_page.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_pre_page.setText("")
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(":/resources/icon/arrow_left_tz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_pre_page.setIcon(icon3)
        self.btn_pre_page.setObjectName("btn_pre_page")
        self.horizontalLayout_2.addWidget(self.btn_pre_page)
        self.txt_page = QtWidgets.QLineEdit(self.widget_4)
        self.txt_page.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_page.setObjectName("txt_page")
        self.horizontalLayout_2.addWidget(self.txt_page)
        self.btn_next_page = QtWidgets.QPushButton(self.widget_4)
        self.btn_next_page.setMaximumSize(QtCore.QSize(50, 16777215))
        self.btn_next_page.setText("")
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(":/resources/icon/arrow_right_tz.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.btn_next_page.setIcon(icon4)
        self.btn_next_page.setObjectName("btn_next_page")
        self.horizontalLayout_2.addWidget(self.btn_next_page)
        self.txt_size = QtWidgets.QLineEdit(self.widget_4)
        self.txt_size.setMaximumSize(QtCore.QSize(50, 16777215))
        self.txt_size.setObjectName("txt_size")
        self.horizontalLayout_2.addWidget(self.txt_size)
        self.page_info = QtWidgets.QLabel(self.widget_4)
        self.page_info.setObjectName("page_info")
        self.horizontalLayout_2.addWidget(self.page_info)
        self.horizontalLayout.addLayout(self.horizontalLayout_2)
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.verticalLayout_4.addWidget(self.widget_4)
        self.verticalLayout_9.addWidget(self.splitter)

        self.retranslateUi(QueryForm)
        self.tabWidget.setCurrentIndex(1)
        self.tabs_result.setCurrentIndex(1)
        QtCore.QMetaObject.connectSlotsByName(QueryForm)

    def retranslateUi(self, QueryForm):
        _translate = QtCore.QCoreApplication.translate
        QueryForm.setWindowTitle(_translate("QueryForm", "Form"))
        self.label_host.setText(_translate("QueryForm", "TextLabel"))
        self.label_index.setText(_translate("QueryForm", "TextLabel"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_comp), _translate("QueryForm", "Complex"))
        self.group_field.setTitle(_translate("QueryForm", "Query"))
        self.group_other.setTitle(_translate("QueryForm", "Source"))
        self.label.setText(_translate("QueryForm", "Include:"))
        self.label_2.setText(_translate("QueryForm", "Exclude:"))
        self.label_4.setText(_translate("QueryForm", "Sort:"))
        self.combo_sort_type.setItemText(0, _translate("QueryForm", "asc"))
        self.combo_sort_type.setItemText(1, _translate("QueryForm", "desc"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_simple), _translate("QueryForm", "Basic"))
        self.tabs_result.setTabText(self.tabs_result.indexOf(self.tab_table), _translate("QueryForm", "Table"))
        self.tree_result.setSortingEnabled(False)
        self.tree_result.headerItem().setText(1, _translate("QueryForm", "Value"))
        self.tree_result.headerItem().setText(2, _translate("QueryForm", "Type"))
        self.tabs_result.setTabText(self.tabs_result.indexOf(self.tab_tree), _translate("QueryForm", "Tree"))
        self.tabs_result.setTabText(self.tabs_result.indexOf(self.tab_json), _translate("QueryForm", "JSON"))
        self.label_5.setText(_translate("QueryForm", "Total: "))
        self.label_total.setText(_translate("QueryForm", "0"))
        self.btn_ignore_null.setText(_translate("QueryForm", "None"))
        self.txt_page.setText(_translate("QueryForm", "1"))
        self.txt_size.setText(_translate("QueryForm", "10"))
        self.page_info.setText(_translate("QueryForm", "Documents 1 of 1"))
from gui.FilterComboBox import FComboBox
from gui.ResultTable import ResultTable
from gui.ResultTree import ResultTree
from ui import icon_rc
