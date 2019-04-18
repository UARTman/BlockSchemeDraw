import sys

from PyQt5.QtWidgets import QApplication

from Engine import parse_be, clean, funcparse, ScrollBlock

if __name__ == '__main__':

    with open('in.pas', 'r', encoding='utf-8') as f:
        InputStr = ' ' + f.read()
    OutputArray = []

    try:
        parse_be(start=0, out=OutputArray, inp=InputStr)
    except TypeError:
        pass

    OutputArray = clean(OutputArray)
    OutputArray = funcparse(OutputArray)
    OutputArray = clean(OutputArray)
    app = QApplication(sys.argv)
    bl = ScrollBlock(inp=['block', OutputArray])
    sys.exit(app.exec_())
