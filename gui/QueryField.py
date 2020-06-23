from PyQt5.QtWidgets import QWidget

from ui.ui_query_field import Ui_Form


class QueryWidget(QWidget, Ui_Form):

    def __init__(self, fieldNames, parent=None):
        self.fieldNames = fieldNames
        self.cond_field.addItems(self.fieldNames)

    def getQuery(self):
        pass

    def initAction(self):
        self.btn_add.click.connect(self.addField)
        self.btn_del.click.connect(self.delField)
        pass

    def addField(self):
        print("addField")
        pass

    def delField(self):
        print("delField")
        pass
