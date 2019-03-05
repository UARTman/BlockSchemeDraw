import sys
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
# from PyQt5.QtGui import QPainter, QColor, QFont, QPen
# from PyQt5.QtCore import Qt

with open('in.pas', 'r', encoding='utf-8') as f:
    InputStr = ' ' + f.read()
OutputArray = []


def inside(inp, **kw):
    if len(inp) == 1:
        if type(inp[0]) == str:
            return CodeFrame(inp[0], **kw)
        elif type(inp[0]) == list:
            if inp[0][0] == 'block':
                return BlockFrame(inp[0], **kw)
    return BlockFrame(['block', inp], **kw)


def consist_of(inp=' ', chars=[' ', '\n']):
    for i in chars:
        inp = inp.replace(i, '')
    if inp != '':
        return False
    return True


def clean(inp=[], garb=[' ', '\n', ';', '.']):
    ret = []
    for i in inp:
        if type(i) == str:
            if not consist_of(i, garb):
                ret.append(i)
        elif type(i) == list:
            k = []
            for j in i:
                if type(j) == list:
                    k.append(clean(j, garb))
                else:
                    k.append(j)
            ret.append(k)
    return ret


def is_keyword(inp=' ', kwrd=' ', allowed_start=[' ', '\n'], allowed_end=[' ', '\n', ';']):

    if kwrd == 'end':
        allowed_end.append('.')
    if kwrd not in inp:
        return False
    else:
        inp1 = inp.replace(kwrd, '')
        if len(inp1) == 0:
                return True
        if len(inp1) == 1:
            if inp1[0] in allowed_end or inp1[0] in allowed_start:
                return True
        if len(inp1) == 2:
            if inp1[0] in allowed_start and inp1[-1] in allowed_end:
                if (inp1[0] == inp[0] and inp1[-1] == inp[-1]) or (inp1[0] == inp[-2] and inp1[-1] == inp[-1]):
                    return True
    return False


def parse_be(start=0, end='end', out=OutputArray, inp=InputStr):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None
        if is_keyword(inp=inp[i-1: i + len(end) + 1], kwrd=end):  #

            return i + len(end)
        if is_keyword(inp=inp[i-1:i+6], kwrd='begin'):
            out.append(['block', []])
            k = parse_be(start=i + 5, out=out[-1][1])
            i = k
            continue
        if is_keyword(inp=inp[i-1:i+3], kwrd='if'):
            out.append(['if', [], [], []])
            k = parse_if(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='while'):
            out.append(['while', [], []])
            k = parse_while(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+4], kwrd='for'):
            out.append(['for', [], [], [], []])
            k = parse_for(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k
            continue

        if inp[i] == "'":
            if len(out) == 0:
                out.append('')
            if type(out[-1]) == str:
                out[-1] += inp[i]
            else:
                out.append(inp[i])
            k = parse_str(start=i + 1, out=out)
            i = k
            out[-1] += "'"
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='repeat'):
            out.append(['repeat', [], []])
            k = parse_repeat(start=i + 6, out=out[-1][1], out1=out[-1][2])
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


def parse_str(start=0, end="'", out=OutputArray, inp=InputStr):
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


def parse_if(start=0, end=';', out=OutputArray, inp=InputStr, out1=[], out2=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if is_keyword(inp=inp[i-1:i+len(end)+1], kwrd=end):  #
            return i + len(end)

        if is_keyword(inp=inp[i-1:i + 6], kwrd='begin'):
            out.append(['block', []])
            k = parse_be(start=i + 5, out=out[-1][1])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='if'):
            out.append(['if', [], [], []])
            k = parse_if(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='while'):
            out.append(['while', [], []])
            k = parse_while(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='repeat'):
            out.append(['repeat', [], []])
            k = parse_repeat(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+4], kwrd='for'):
            out.append(['for', [], [], [], []])
            k = parse_for(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+5], kwrd='then'):
            out = out1
            i = i + 4
            continue
        if is_keyword(inp=inp[i-1:i+5], kwrd='else'):
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
            k = parse_str(start=i + 1, out=out)
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


def parse_while(start=0, end=';', out=OutputArray, inp=InputStr, out1=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if is_keyword(inp=inp[i-1:i + 6], kwrd='begin'):
            out.append(['block', []])
            k = parse_be(start=i + 5, out=out[-1][1])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='if'):
            out.append(['if', [], [], []])
            k = parse_if(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='while'):
            out.append(['while', [], []])
            k = parse_while(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='repeat'):
            out.append(['repeat', [], []])
            k = parse_repeat(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+4], kwrd='for'):
            out.append(['for', [], [], [], []])
            k = parse_for(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='do'):
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
            k = parse_str(start=i + 1, out=out)
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


def parse_repeat(start=0, end=';', out=OutputArray, inp=InputStr, out1=[]):
    i = start  # Index
    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if is_keyword(inp=inp[i-1:i + 6], kwrd='begin'):
            out.append(['block', []])
            k = parse_be(start=i + 5, out=out[-1][1])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='if'):
            out.append(['if', [], [], []])
            k = parse_if(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='while'):
            out.append(['while', [], []])
            k = parse_while(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='repeat'):
            out.append(['repeat', [], []])
            k = parse_repeat(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+4], kwrd='for'):
            out.append(['for', [], [], [], []])
            k = parse_for(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='until'):
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
            k = parse_str(start=i + 1, out=out)
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


def parse_for(start=0, end=';', out=OutputArray, inp=InputStr, out1=[], out2=[], typ=[]):
    i = start  # Index

    while True:
        if i >= len(inp):
            return None

        if inp[i:i + len(end)] == end:  #
            return i + len(end)

        if is_keyword(inp=inp[i-1:i + 6], kwrd='begin'):
            out.append(['block', []])
            k = parse_be(start=i + 5, out=out[-1][1])
            i = k
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='if'):
            out.append(['if', [], [], []])
            k = parse_if(start=i + 2, out=out[-1][1], out1=out[-1][2], out2=out[-1][3])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+6], kwrd='while'):
            out.append(['while', [], []])
            k = parse_while(start=i + 5, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='repeat'):
            out.append(['repeat', [], []])
            k = parse_repeat(start=i + 6, out=out[-1][1], out1=out[-1][2])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+4], kwrd='for'):
            out.append(['for', [], [], [], []])
            k = parse_for(start=i + 3, out=out[-1][1], out1=out[-1][2], out2=out[-1][3], typ=out[-1][4])
            i = k - 1
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='to'):
            out = out1
            i = i + 2
            typ.append(1)
            continue

        if is_keyword(inp=inp[i-1:i+7], kwrd='downto'):
            out = out1
            i = i + 6
            typ.append(2)
            continue

        if is_keyword(inp=inp[i-1:i+3], kwrd='do'):
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
            k = parse_str(start=i + 1, out=out)
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
        self.currentLayout = QVBoxLayout()
        self.TextLabel = QLabel(self)
        self.TextLabel.setText(inp)

        self.currentLayout.addWidget(self.TextLabel)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.setLayout(self.currentLayout)

        self.show()


class BlockFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currentLayout = QVBoxLayout()
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
            self.currentLayout.addWidget(cf)
            self.currentLayout.setAlignment(cf, Qt.AlignTop)
        self.setGeometry(0, 0, 1, 1)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Expanding)
        self.setLayout(self.currentLayout)
        self.show()


class IfFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currentLayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('if')
        self.currentLayout.addWidget(self.typeLbl)
        self.require = CodeFrame(inp[1][0])
        self.currentLayout.addWidget(self.require)
        self.hb = QHBoxLayout()
        self.thenLayout = QVBoxLayout()
        self.thenLabel = QLabel()
        self.thenLabel.setText('then')
        self.thenLayout.addWidget(self.thenLabel)
        self.thenLayout.addWidget(inside(inp[2]))
        self.elseLayout = QVBoxLayout()
        self.elseLabel = QLabel()
        self.elseLabel.setText('else')
        self.elseLayout.addWidget(self.elseLabel)
        self.elseLayout.addWidget(inside(inp[3]))
        self.hb.addLayout(self.thenLayout)
        self.hb.addLayout(self.elseLayout)
        self.currentLayout.addLayout(self.hb)
        self.setGeometry(0, 0, 350, 300)
        self.setLayout(self.currentLayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


class WhileFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currentLayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('while')
        self.currentLayout.addWidget(self.typeLbl)
        self.condLabel = CodeFrame(inp[1][0])
        self.currentLayout.addWidget(self.condLabel)
        self.doBlock = inside(inp[2])
        self.currentLayout.addWidget(self.doBlock)
        self.setGeometry(0, 0, 350, 300)
        self.setLayout(self.currentLayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


class RepeatFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currentLayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('repeat')
        self.currentLayout.addWidget(self.typeLbl)
        self.doBlock = inside(inp[2])
        self.currentLayout.addWidget(self.doBlock)
        self.untLbl = QLabel()
        self.untLbl.setText('until')
        self.currentLayout.addWidget(self.untLbl)
        self.condLabel = CodeFrame(inp[1][0])
        self.currentLayout.addWidget(self.condLabel)
        self.setGeometry(0, 0, 350, 300)
        self.setLayout(self.currentLayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


class ForFrame(QFrame):
    def __init__(self, inp, **kw):
        super().__init__(**kw)
        self.setFrameStyle(2)
        self.contentList = []
        self.currentLayout = QVBoxLayout()
        self.typeLbl = QLabel()
        self.typeLbl.setText('for')
        self.currentLayout.addWidget(self.typeLbl)
        self.var = CodeFrame(inp[1][0])
        self.currentLayout.addWidget(self.var)
        self.typeLbl2 = QLabel()
        self.toFrame = CodeFrame(inp[2][0])
        self.currentLayout.addWidget(self.toFrame)
        self.doFrame = inside(inp[3])
        self.currentLayout.addWidget(self.doFrame)
        self.setLayout(self.currentLayout)
        self.setSizePolicy(QSizePolicy.Fixed, QSizePolicy.Maximum)
        self.show()


if __name__ == '__main__':
    try:
        parse_be(start=0)
    except TypeError:
        pass
    OutputArray = clean(OutputArray)
    app = QApplication(sys.argv)
    bl = BlockFrame(inp=['block', OutputArray])
    sys.exit(app.exec_())
