import sys

from PyQt5.QtWidgets import QApplication

from Interface import MainWindow

if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    a = MainWindow()
    sys.exit(mainApp.exec_())

