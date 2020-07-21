from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget

from ui.ui_query_field import Ui_QueryField


class QueryField(QWidget, Ui_QueryField):

    def __init__(self, fieldNames, father, parent=None):
        super(QWidget, self).__init__(parent)
        self.father = father
        self.fieldNames = fieldNames
        self.status = True
        self.setupUi(self)
        self.cond_operator.setVisible(False)
        self.cond_value.setVisible(False)
        self.load_items()
        self.init_action()

    def set_value(self, field, operator, value):
        self.cond_field.setCurrentText(field)
        self.cond_operator.setCurrentText(operator)
        self.cond_value.setText(value)

    def load_items(self):
        model = QStandardItemModel()
        for field in self.fieldNames:
            item = QStandardItem(field)
            item.setToolTip(field)
            model.appendRow(item)
        self.cond_field.setModel(model)

    def getQuery(self):
        if self.cond_field.currentText() == 'match_all':
            return {"match_all": {}}
        else:
            return {
                self.cond_operator.currentText(): {
                    self.cond_field.currentText(): self.cond_value.text()
                }
            }

    def getGroup(self):
        return self.cond_bool.currentText()


    def init_action(self):
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
        if self.cond_field.currentText() == 'match_all':
            self.cond_operator.setVisible(False)
            self.cond_value.setVisible(False)
        else:
            self.cond_operator.setVisible(True)
            self.cond_value.setVisible(True)
