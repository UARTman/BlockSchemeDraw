import sys
from PyQt5.QtWidgets import QWidget, QApplication, QLabel, QFrame, QVBoxLayout, QHBoxLayout, \
    QGridLayout, QSizePolicy
from PyQt5.QtCore import Qt



# from PyQt5.QtGui import QPainter, QColor, QFont, QPen
# from PyQt5.QtCore import Qt


class CodeFrame(QFrame):
    def __init__(self, inp='', **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.currLayout = QVBoxLayout()
        self.TextLabel = QLabel(self)
        self.TextLabel.setText(inp)

        self.currLayout.addWidget(self.TextLabel)

        self.setLayout(self.currLayout)

        self.show()


class BlockFrame(QFrame):
    def __init__(self, inp=[], **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()

        self.typeLbl = QLabel()
        self.typeLbl.setText('block')
        self.currlayout.addWidget(self.typeLbl)
        for i in inp[1]:
            if type(i) == str:
                cf = CodeFrame(inp=i, parent=self)
            elif i[0] == 'block':
                cf = BlockFrame(inp=i, parent=self)
            cf.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
            self.contentList.append(cf)
            self.currlayout.addWidget(cf)
            self.currlayout.setAlignment(cf, Qt.AlignTop)

        self.setGeometry(300, 300, 350, 300)
        self.setLayout(self.currlayout)

        self.show()







if __name__ == '__main__':
    print(1)
    app = QApplication(sys.argv)
    # w = QWidget()
    # ex2 = QFrame()
    # ex2.setWindowTitle('BlockSchemeGen alpha 0.1')
    mc = '''import sys
from PyQt4 import QtGui, QtCore

class Widget(QtGui.QWidget):
    def __init__(self):
        super(Widget, self).__init__()

        self.initUI()

    def initUI(self):
        self.setWindowTitle('TEST')
        self.resize(200, 100)

        self.label = QtGui.QLabel(self)
        self.label.move(20, 20)
        self.label.setText('Hello')

        # Какой атрибут установить, чтобы размер подгонялся под текст?
        # self.label.setScaledContents(True)

        button = QtGui.QPushButton('Click me', self)
        button.move(20, 50)
        self.connect(button, QtCore.SIGNAL('clicked()'),
            self.function)

    def function(self):
        self.label.setText('Jack Sparrow!')
        self.label.adjustSize() # без этого текст больший предыдущего будет обрезаться.

if __name__ == '__main__':

    app = QtGui.QApplication(sys.argv)
    w = Widget()
    w.show()
    sys.exit(app.exec_())'''
    # ex1 = CodeFrame(inp=mc, parent=ex2)
    # ex1.resize(150, 150)
    block = ['block', [
        '1',
        'Hello Again',
        '134',
        ['block', ['1',
                   '2',
                   'Hello World',
                   ['block', [
                       '1',
                       'Hello Again, guys!'
                   ]]
                   ]]
    ]]
    bl = BlockFrame(inp=block)
    # ex2.show()
    print(2)
    sys.exit(app.exec_())
