from PyQt5.QtWidgets import QWidget

from ui.ui_query_field import Ui_QueryField


class QueryField(QWidget, Ui_QueryField):

    def __init__(self, fieldNames, father, parent=None):
        super(QWidget, self).__init__(parent)
        self.father = father
        self.fieldNames = fieldNames
        self.status = True
        self.setupUi(self)
        self.cond_field.addItems(self.fieldNames)
        self.initAction()

    def getQuery(self):
        pass

    def initAction(self):
        # self.btn_add.clicked.connect(self.addField)
        self.btn_del.clicked.connect(self.delField)
        pass

    def addField(self):
        print("addField")
        pass

    def delField(self):
        print("delField")
        self.status = False
        self.father.updateQueryFields(self)
        pass
