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
        result = {
            self.cond_operator.currentText(): {
                self.cond_field.currentText(): self.cond_value.text()
            }
        }
        return result

    def getGroup(self):
        return self.cond_bool.currentText()


    def initAction(self):
        # self.btn_add.clicked.connect(self.addField)
        self.btn_del.clicked.connect(self.delField)
        self.cond_field.currentTextChanged.connect(self.changeField)
        pass

    def addField(self):
        print("addField")
        pass

    def delField(self):
        print("delField")
        self.status = False
        self.father.updateQueryFields(self)
        pass

    def changeField(self):
        print(self.cond_field.currentText())

        pass
