import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon #это импортируем для сердечка

from ui_xo import Ui_MainWindow

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.is_x_turn = True
        self.heart_icon = QIcon("heart.png")
        self.icon_size = 50
