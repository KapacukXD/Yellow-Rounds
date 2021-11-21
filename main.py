from random import randrange
import sys
from PyQt5.QtGui import QColor, QPainter
from PyQt5.QtWidgets import QApplication, QMainWindow
from UI import Ui_Form


class Rounds(QMainWindow, Ui_Form):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.do_paint = False
        self.btn.clicked.connect(self.paint)
        self.n = 7

    def paintEvent(self, event):
        qp = QPainter()
        qp.begin(self)
        if self.do_paint:
            self.draw_rounds(qp)
        qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_rounds(self, qp):
        for i in range(self.n):
            a, b = randrange(100, 900), randrange(100, 500)
            l = randrange(50, 200)
            color = QColor(randrange(0, 255), randrange(0, 255), randrange(0, 255))
            qp.setBrush(color)
            qp.drawEllipse(a - int(l / 2), b - int(l / 2), l, l)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Rounds()
    ex.show()
    sys.exit(app.exec_())
