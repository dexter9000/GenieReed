from PyQt5.QtWidgets import QDialog

from ui.ui_about_dlg import Ui_AboutDialog


class AboutDlg(QDialog, Ui_AboutDialog):
    def __init__(self, parent=None):
        super(QDialog, self).__init__(parent)
        self.setupUi(self)
