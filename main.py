import sys
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPainter, QColor, QFont, QPen
# from PyQt5.QtCore import Qt

with open('in.txt', 'r') as f:
    InputStr = f.read()
OutputArray = []

def FParseBE(start=0, end='end', out=OutputArray, inp=InputStr):
    i = start  # Index
    print(i, inp, len(inp))

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if inp[i:i + 5] == 'begin':
            out.append(['block', []])
            k = FParseBE(start=i + 5, out=out[-1][1])
            i = k
            continue
        if inp[i:i + 2] == 'if':
            out.append(['if', [], [], []])
            k = FParseIf(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k
            continue

        if inp[i:i + 5] == 'while':
            out.append(['while', [], []])
            k = FParseWhile(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if inp[i:i + 3] == 'for':
            out.append(['for', [], [], [], []])
            k = FParseFor(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = FParseStr(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if inp[i:i + 6] == 'repeat':
            out.append(['repeat', [], []])
            k = FParseRU(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if len(out) == 0:
            out.append('')
        if type(out[-1]) == str:
            out[-1] += inp[i]
        else:
            out.append(inp[i])

        i += 1


# # Парсер Строк

# In[129]:


def FParseStr(start=0, end="'", out=OutputArray, inp=InputStr):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None
        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if i < len(inp):  # Добавляем символ в выводную структуру
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
        else:
            return None

        i += 1


# # Парсер If

# In[130]:


def FParseIf(start=0, end=';', out=OutputArray, inp=InputStr, out1=[], out2=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if inp[i:i + 5] == 'begin':
            out.append(['block', []])
            k = FParseBE(start=i + 5, out=out[-1][1])
            i = k
            continue

        if inp[i:i + 2] == 'if':
            out.append(['if', [], [], []])
            k = FParseIf(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if inp[i:i + 5] == 'while':
            out.append(['while', [], []])
            k = FParseWhile(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 6] == 'repeat':
            out.append(['repeat', [], []])
            k = FParseRU(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 3] == 'for':
            out.append(['for', [], [], [], []])
            k = FParseFor(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if inp[i:i + 4] == 'then':
            out = out1
            i = i + 4
            continue
        if inp[i:i + 4] == 'else':
            out = out2
            i = i + 4
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = FParseStr(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if i < len(inp):  # Добавляем символ в выводную структуру
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
        else:
            return None

        i += 1


# # Парсер While

# In[131]:


def FParseWhile(start=0, end=';', out=OutputArray, inp=InputStr, out1=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if inp[i:i + 5] == 'begin':
            out.append(['block', []])
            k = FParseBE(start=i + 5, out=out[-1][1])
            i = k
            continue

        if inp[i:i + 2] == 'if':
            out.append(['if', [], [], []])
            k = FParseIf(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if inp[i:i + 5] == 'while':
            out.append(['while', [], []])
            k = FParseWhile(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 6] == 'repeat':
            out.append(['repeat', [], []])
            k = FParseRU(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 3] == 'for':
            out.append(['for', [], [], [], []])
            k = FParseFor(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if inp[i:i + 2] == 'do':
            out = out1
            i = i + 2
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = FParseStr(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if i < len(inp):  # Добавляем символ в выводную структуру
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
        else:
            return None

        i += 1


# # Парсер Repeat/Until

# In[132]:


def FParseRU(start=0, end=';', out=OutputArray, inp=InputStr, out1=[]):
    i = start  # Index
    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if inp[i:i + 5] == 'begin':
            out.append(['block', []])
            k = FParseBE(start=i + 5, out=out[-1][1])
            i = k
            continue

        if inp[i:i + 2] == 'if':
            out.append(['if', [], [], []])
            k = FParseIf(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k
            continue

        if inp[i:i + 5] == 'while':
            out.append(['while', [], []])
            k = FParseWhile(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if inp[i:i + 6] == 'repeat':
            out.append(['repeat', [], []])
            k = FParseRU(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if inp[i:i + 3] == 'for':
            out.append(['for', [], [], [], []])
            k = FParseFor(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k
            continue

        if inp[i:i + 5] == 'until':
            out = out1
            i = i + 5
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = FParseStr(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if i < len(inp):  # Добавляем символ в выводную структуру
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
        else:
            return None

        i += 1


# # Парсер for

# In[133]:


def FParseFor(start=0, end=';', out=OutputArray, inp=InputStr, out1=[], out2=[], typ=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if inp[i:i + 5] == 'begin':
            out.append(['block', []])
            k = FParseBE(start=i + 5, out=out[-1][1])
            i = k
            continue

        if inp[i:i + 2] == 'if':
            out.append(['if', [], [], []])
            k = FParseIf(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if inp[i:i + 5] == 'while':
            out.append(['while', [], []])
            k = FParseWhile(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 6] == 'repeat':
            out.append(['repeat', [], []])
            k = FParseRU(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if inp[i:i + 3] == 'for':
            out.append(['for', [], [], [], []])
            k = FParseFor(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if inp[i:i + 2] == 'to':
            out = out1
            i = i + 2
            typ.append(1)
            continue

        if inp[i:i + 6] == 'downto':
            out = out1
            i = i + 6
            typ.append(2)
            continue

        if inp[i:i + 2] == 'do':
            out = out2
            i = i + 2
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = FParseStr(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if i < len(inp):  # Добавляем символ в выводную структуру
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
        else:
            return None

        i += 1


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
    def __init__(self, inp, **kw):
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
            elif i[0] == 'for':
                cf = ForFrame(inp=i, parent=self)
            else:
                continue
            self.contentList.append(cf)
            self.currlayout.addWidget(cf)
            self.currlayout.setAlignment(cf, Qt.AlignTop)
        self.setGeometry(300, 300, 1, 1)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setLayout(self.currlayout)
        self.show()


class IfFrame(QFrame):
    def __init__(self, inp, **kw):
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
    def __init__(self, inp, **kw):
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
    def __init__(self, inp, **kw):
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


class ForFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currlayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('for')
        self.currlayout.addWidget(self.typeLbl)
        self.var = CodeFrame(inp[1][0])
        self.currlayout.addWidget(self.var)
        kk = ['', 'to', 'downto']
        self.typeLbl2 = QLabel()
        self.typeLbl2.setText(kk[inp[-1][0]])
        self.currlayout.addWidget(self.typeLbl2)
        self.toFrame = CodeFrame(inp[2][0])
        self.currlayout.addWidget(self.toFrame)
        self.doFrame = BlockFrame(['block', inp[3]])
        self.currlayout.addWidget(self.doFrame)
        self.setLayout(self.currlayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


if __name__ == '__main__':
    try:
        FParseBE(start=0,)
    except TypeError:
        pass
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
        ['repeat', ['end'], ['1', '2', '3']],
        ['for', [' i:=0 '], [' 10 '], [' jump'], [2]]
    ]]
    bl = BlockFrame(inp=['block', OutputArray])
    # ex2.show()
    sys.exit(app.exec_())
