from PyQt5.QtWidgets import QWidget, QListWidget, QLineEdit


class MultiComboBox(QWidget):

    def __init__(self):
        pass

    def setupUi(self, QueryForm):
        QueryForm.setObjectName("QueryForm")
        QueryForm.resize(868, 706)
        pListWidget = QListWidget()
        pLineEdit = QLineEdit()
