import sys

from PyQt5.QtCore import Qt, QCoreApplication
from PyQt5.QtWidgets import QApplication

from gui.MainWindow import MyWindow

if __name__ == '__main__':
    QCoreApplication.setAttribute(Qt.AA_EnableHighDpiScaling)

    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()

    sys.exit(app.exec_())
