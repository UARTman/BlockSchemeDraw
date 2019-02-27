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
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.setLayout(self.currLayout)

        self.show()


class BlockFrame(QFrame):
    def __init__(self, inp=[], **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()

        # self.typeLbl = QLabel()
        # self.typeLbl.setText('block')
        # self.currlayout.addWidget(self.typeLbl)
        for i in inp[1]:
            if type(i) == str:
                cf = CodeFrame(inp=i, parent=self)
            elif i[0] == 'block':
                cf = BlockFrame(inp=i, parent=self)
            elif i[0] == 'if':
                cf = IfFrame(inp=i, parent=self)
            elif i[0] == 'while':
                cf = WhileFrame(inp=i, parent=self)
            elif i[0] == 'repeat':
                cf = RepeatFrame(inp=i, parent=self)
            else:
                continue
            self.contentList.append(cf)
            self.currlayout.addWidget(cf)
            self.currlayout.setAlignment(cf, Qt.AlignTop)
        self.setGeometry(300, 300, 350, 300)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setLayout(self.currlayout)
        self.show()


class IfFrame(QFrame):
    def __init__(self, inp=[], **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('if')
        self.currlayout.addWidget(self.typeLbl)
        self.require = CodeFrame(inp[1][0])
        self.currlayout.addWidget(self.require)
        self.hb = QHBoxLayout()
        self.thenlayout = QVBoxLayout()
        self.thenlayout.addWidget(BlockFrame(['block', inp[2]]))
        self.elselayout = QVBoxLayout()
        self.elselayout.addWidget(BlockFrame(['block', inp[3]]))
        self.hb.addLayout(self.thenlayout)
        self.hb.addLayout(self.elselayout)
        self.currlayout.addLayout(self.hb)
        self.setGeometry(300, 300, 350, 300)
        self.setLayout(self.currlayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


class WhileFrame(QFrame):
    def __init__(self, inp=[], **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('while')
        self.currlayout.addWidget(self.typeLbl)
        self.condLabel = CodeFrame(inp[1][0])
        self.currlayout.addWidget(self.condLabel)
        self.doBlock = BlockFrame(['block', inp[2]])
        self.currlayout.addWidget(self.doBlock)
        self.setGeometry(300, 300, 350, 300)
        self.setLayout(self.currlayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


class RepeatFrame(QFrame):
    def __init__(self, inp=[], **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('repeat')
        self.currlayout.addWidget(self.typeLbl)
        self.doBlock = BlockFrame(['block', inp[2]])
        self.currlayout.addWidget(self.doBlock)
        self.untLbl = QLabel()
        self.untLbl.setText('until')
        self.currlayout.addWidget(self.untLbl)
        self.condLabel = CodeFrame(inp[1][0])
        self.currlayout.addWidget(self.condLabel)
        self.setGeometry(300, 300, 350, 300)
        self.setLayout(self.currlayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
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
        ['while', ['cond'], ['1', '2', '3']],
        ['repeat', ['end'], ['1', '2', '3']]
    ]]
    bl = BlockFrame(inp=block)
    # ex2.show()
    print(2)
    sys.exit(app.exec_())
