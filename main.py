from PyQt5.QtWidgets import QMainWindow
SCREEN_SIZE = [680, 480]
import sys
from PyQt5 import uic
from random import randint
from PyQt5.QtGui import QPainter, QColor
from PyQt5.QtWidgets import QApplication



class Suprematism(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('UI.ui', self)
        self.setMouseTracking(True)
        self.coords_ = []
        self.qp = QPainter()
        self.flag = False
        self.status = None

    def drawf(self):
        self.flag = True
        self.update()

    def paintEvent(self, event):
        if self.flag:
            self.qp = QPainter()
            self.qp.begin(self)
            self.draw(self.status)
            self.qp.end()

    def draw(self, status):
        if status == 1:
            R = randint(20, 100)
            self.qp.setBrush(QColor(255, 255, 0))
            self.qp.drawEllipse(int(self.coords_[0] - R / 2),
                                int(self.coords_[1] - R / 2), R, R)

    def mousePressEvent(self, event):
        self.coords_ = [event.x(), event.y()]
        self.status = 1
        self.drawf()

    def mouseMoveEvent(self, event):
        self.coords_ = [event.x(), event.y()]



def except_hook(cls, exception, traceback):
    sys.__excepthook__(cls, exception, traceback)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    sys.excepthook = except_hook
    ex = Suprematism()
    ex.show()
    sys.exit(app.exec_())