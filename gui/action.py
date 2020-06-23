from es import EsClient
from gui.AboutDlg import AboutDlg
from gui.ConnDlg import ConnDlg
from gui.QueryWidget import QueryWidget
from gui.ui_db_index_widget import Ui_DbIndexForm


class GuiAction:

    def __init__(self, window):
        self.window = window
        self.config = window.config
        self.initAction()
        pass

    def loadIndex(self, client):
        self.window.dbWidgets = []
        self.window.dbLists = []

        newDbWidget = Ui_DbIndexForm(self, client.getHost())

        self.window.dbWidgets.append(newDbWidget)
        self.window.dbList.addItem(newDbWidget, client.getHost())
        self.window.dbList.setCurrentIndex(self.window.dbList.count() - 1)

        result = client.indices()
        for item in result:
            newDbWidget.addColl(item)

    def showMessage(self, message):
        self.window.statusBar().showMessage(message)

    def actiondebugClick(self):
        print("actiondebug_click")
        collName = ["111", "222"]
        for item in collName:
            self.addColl(self.window.dbListWidget, item)

    def selectIndex(self, host, index, indeies):
        self.addNewQueryTab(host, index, indeies)
        pass

    def addNewQueryTab(self, host, index, indeies):
        es = EsClient()
        es.openHost(host)
        pattern = es.scheme(index)
        tab = QueryWidget(host, index, indeies, pattern, es)
        tab.addAllIndex([index])
        self.window.tabWidget.addTab(tab, index)
        self.window.tabWidget.setCurrentWidget(tab)
        pass

    def initAction(self):
        self.window.actiondebug.triggered.connect(self.actiondebugClick)

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

            self.loadIndex(self.es)
            # QMessageBox.information(self, "温馨提示", "数据库连接成功！", QMessageBox.Yes, QMessageBox.Yes)

    def openAboutDlg(self):
        aboutDlg = AboutDlg()
        aboutDlg.exec_()
