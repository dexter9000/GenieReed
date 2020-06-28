from PyQt5.QtWidgets import QLabel


class ClosableLabel(QLabel):

    def __init__(self, parent=None):
        super(QLabel, self).__init__(parent)

    def setupUi(self):
        # self.pListWidget = QListWidget(self)
        pass