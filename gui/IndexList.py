from PyQt5.QtWidgets import QApplication, QTreeWidget, QWidget


class Ui_Form(QWidget):

    def __init__(self, host,  parent=None):
        super(QWidget, self).__init__(parent)
        self.host = host
        self.setupUi(self)

    def setupUi(self, Form):
        Form.setObjectName("Form")

    def getAllIndex(self):
        return