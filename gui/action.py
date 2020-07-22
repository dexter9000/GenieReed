from PyQt5.QtWidgets import QMessageBox

from es import EsClient
from gui.AboutDlg import AboutDlg
from gui.ConnDlg import ConnDlg
from gui.QueryWidget import QueryWidget
from gui.SignalThread import SignalThread
from gui.ui_db_index_widget import Ui_DbIndexForm


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

    def addIndexItem(self, host, result):
        self.window.dbWidgets = []
        self.window.dbLists = []
        newDbWidget = Ui_DbIndexForm(self, host)
        self.window.dbWidgets.append(newDbWidget)
        self.window.dbList.addItem(newDbWidget, host)
        self.window.dbList.setCurrentIndex(self.window.dbList.count() - 1)
        for item in result:
            newDbWidget.addColl(item)

    def loadIndexFunc(self):
        return self.es.indices()

    def loadIndexSignalFn(self, result):
        if result['result'] == 'succ':
            self.addIndexItem(self.es.getHost(), result['data'])
            self.showMessage("Total Index : " + str(len(result['data'])))
        elif result['result'] == 'error':
            QMessageBox.critical(self.window, "失败", "连接失败")
        # self.test_progress.setVisible(False)

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
        pass

    def initAction(self):
        self.window.actiondebug.triggered.connect(self.actionDebugClick)

    def openConnDlg(self):
        connDlg = ConnDlg(self.config)
        connDlg.loadHosts(self.config.get("connections"))
        result = connDlg.exec_()
        print(result)

        if(result == 1):
            self.hostInfo = connDlg.getConnection()
            if (self.hostInfo == None):
                return

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
        self.my_thread = SignalThread()#实例化线程对象
        self.my_thread.my_signal.connect(self.set_label_func)
        pass

    def set_label_func(self, num):
        pass