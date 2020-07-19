from PyQt5.QtWidgets import QMessageBox, QWidget


class Error(QWidget):

    def showError(self, txt):
        QMessageBox.critical(self, "错误", txt, QMessageBox.Yes, QMessageBox.Yes)

    def showSuccess(self, txt):
        QMessageBox.alert(self, "错误", txt, QMessageBox.Yes, QMessageBox.Yes)