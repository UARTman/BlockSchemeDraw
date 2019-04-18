import copy
import sys

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QLabel, QFrame, QVBoxLayout, QHBoxLayout, QSizePolicy, QGridLayout, \
    QScrollArea, QWidget


class MainWindow(QWidget):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
