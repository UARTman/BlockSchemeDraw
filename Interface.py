import copy
import sys


from PyQt5.QtCore import Qt, pyqtSlot
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QGridLayout, \
    QScrollArea, QWidget, QPushButton, QLineEdit, QMessageBox

from Engine import parse_be, clean, funcparse, ScrollBlock


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.blockScheme = None
        self.mainLayout = QVBoxLayout()

        self.fileInputField = QLineEdit()
        self.fileInputField.setText("in.pas")
        self.mainLayout.addWidget(self.fileInputField)

        self.submit = QPushButton()
        self.submit.setText("Запустить!")
        self.submit.clicked.connect(self.ev_submit_clicked)
        self.mainLayout.addWidget(self.submit)

        self.mainLayout.addStretch(0)

        self.setLayout(self.mainLayout)
        self.show()

    @pyqtSlot()
    def ev_submit_clicked(self):
        filename = self.fileInputField.text()
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                input_str = ' ' + f.read()
            output_array = []
        except FileNotFoundError:
            QMessageBox.question(self, "BlockSchemeGenerator", "Ошибка: файл не найден!", QMessageBox.Close,
                                 QMessageBox.Close)
            return

        try:
            parse_be(start=0, out=output_array, inp=input_str)
        except TypeError:
            pass

        output_array = clean(output_array)
        output_array = funcparse(output_array)
        output_array = clean(output_array)
        self.blockScheme = ScrollBlock(inp=['block', output_array])


if __name__ == '__main__':
    mainApp = QApplication(sys.argv)
    a = MainWindow()
    sys.exit(mainApp.exec_())
