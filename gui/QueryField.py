from PyQt5.QtWidgets import QWidget

from ui.ui_query_field import Ui_QueryField


class QueryField(QWidget, Ui_QueryField):

    def __init__(self, fieldNames, parent=None):
        super(QWidget, self).__init__(parent)
        self.fieldNames = fieldNames
        self.setupUi(self)
        self.cond_field.addItems(self.fieldNames)

    def getQuery(self):
        pass

    def initAction(self):
        # self.btn_add.click.connect(self.addField)
        # self.btn_del.click.connect(self.delField)
        pass

    def addField(self):
        print("addField")
        pass

    def delField(self):
        print("delField")
        pass
