from PyQt5 import QtGui, QtCore
from PyQt5.QtWidgets import QLabel


class DragLabel(QLabel):
    MyLabelPressedSignal = QtCore.pyqtSignal()

    def __init__(self, dropFn, parent=None):
        super(DragLabel, self).__init__(parent)
        self.MyLabelPressed = 0
        self.dropFn = dropFn
        self.setAcceptDrops(True)
        self.setMinimumSize(QtCore.QSize(0, 0))
        self.setMaximumSize(QtCore.QSize(16777215, 20))
        self.setText('drag field here')
        self.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignCenter|QtCore.Qt.AlignVCenter)
        qss = '''DragLabel {
                    height: 25px;
                    background: #FFFFFF;
                    margin: 2px 10px;
                    border: 1px dashed #e3e3e3;
                }'''
        self.setStyleSheet(qss)

    '''
    def mouseDoubleClickEvent(self,e):
        print 'mouse double clicked'
    '''

    def mousePressEvent(self, e):
        print('mousePressEvent')
        self.MyLabelPressed = 1

    def mouseReleaseEvent(self, e):
        print('mouseReleaseEvent')
        if self.MyLabelPressed == 1:
            self.MyLabelPressedSignal.emit()
            self.MyLabelPressed = 0

    def dragEnterEvent(self, e):
        e.accept()


    def dropEvent(self, e):
        print(e)
        self.dropFn(e)
        # position = e.pos()
        # self.button.move(position)
        # e.setDropAction(Qt.MoveAction)
        # e.accept()