from PyQt5.QtWidgets import QMessageBox

from es import EsClient
from gui.AboutDlg import AboutDlg
from gui.ConnDlg import ConnDlg
from gui.QueryWidget import QueryWidget
from gui.SignalThread import SignalThread
from gui.DbIndexList import DbIndexForm


class GuiAction:

    def __init__(self, window):
        self.window = window
        self.config = window.config
        self.initAction()
        pass

    def loadIndex(self):
        my_thread = SignalThread(self.loadIndexFunc)
        my_thread.my_signal.connect(self.loadIndexSignalFn)
        my_thread.start()

    def add_index_item(self, host, result):
        self.window.dbWidgets = []
        self.window.dbLists = []
        new_db_widget = DbIndexForm(self, host)
        self.window.dbWidgets.append(new_db_widget)
        self.window.dbList.addItem(new_db_widget, host)
        self.window.dbList.setCurrentIndex(self.window.dbList.count() - 1)
        for item in result:
            new_db_widget.addColl(item)

    def loadIndexFunc(self):
        return self.es.indices()

    def loadIndexSignalFn(self, result):
        if result['result'] == 'succ':
            self.add_index_item(self.es.getHost(), result['data'])
            self.showMessage("Total Index : " + str(len(result['data'])))
        elif result['result'] == 'error':
            QMessageBox.critical(self.window, "失败", "连接失败")

    def showMessage(self, message):
        self.window.statusBar().showMessage(message)

    def selectIndex(self, host, index, indeies):
        self.addNewQueryTab(host, index, indeies)
        pass

    def addNewQueryTab(self, host, index, indeies):
        es = EsClient()
        es.openHost(host)
        pattern = es.scheme(index)
        tab = QueryWidget(host, index, indeies, pattern, es)

        self.window.tabWidget.addTab(tab, index)
        self.window.tabWidget.setCurrentWidget(tab)
        self.window.tabWidget.setTabToolTip(self.window.tabWidget.currentIndex(), index)

        width = self.window.tabWidget.width() - 50;
        tabCount = self.window.tabWidget.count();
        tabWidth = width / tabCount;
        self.window.tabWidget.setStyleSheet("#tabWidget::tab{width:" + str(tabWidth) + "px;}");

        pass

    def initAction(self):
        self.window.actiondebug.triggered.connect(self.actionDebugClick)

    def openConnDlg(self):
        connDlg = ConnDlg(self.config)
        connDlg.loadHosts(self.config.get("connections"))
        result = connDlg.exec_()
        print(result)

        if (result == 1):
            self.hostInfo = connDlg.getConnection()
            if self.hostInfo is None: return
            self.es = EsClient()
            self.es.open(self.hostInfo['host'], self.hostInfo['port'])
            self.loadIndex()
            # QMessageBox.information(self, "温馨提示", "数据库连接成功！", QMessageBox.Yes, QMessageBox.Yes)

    def openAboutDlg(self):
        aboutDlg = AboutDlg()
        aboutDlg.exec_()

    def actionDebugClick(self):
        # fc = FComboBox()
        # self.window.welcomeLayout.addWidget(fc)
        self.my_thread = SignalThread()  # 实例化线程对象
        self.my_thread.my_signal.connect(self.set_label_func)
        pass

    def set_label_func(self, num):
        pass
