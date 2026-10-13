import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from PySide6.QtGui import QIcon
from PySide6.QtCore import QSize

from ui_xo import Ui_MainWindow


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()

        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        self.is_x_turn = True
        self.heart_icon = QIcon("heart.png")
        self.icon_size = QSize(50, 50)

        self.buttons = [
            self.ui.btn1, self.ui.btn2, self.ui.btn3,
            self.ui.btn4, self.ui.btn5, self.ui.btn6,
            self.ui.btn7, self.ui.btn8, self.ui.btn9,
        ]

        for btn in self.buttons:
            btn.clicked.connect(self.on_cell_clicked)

        self.ui.resetBtn.clicked.connect(self.reset_game)

    def on_cell_clicked(self):
        btn = self.sender()
        if btn.text() != "" or not btn.icon().isNull():
            return

        if self.is_x_turn:
            btn.setText("X")
            self.is_x_turn = False
        else:
            btn.setText("")
            btn.setIcon(self.heart_icon)
            btn.setIconSize(self.icon_size)
            self.is_x_turn = True

        self.check_winner()

    def check_winner(self):
        combos = [
            (0, 1, 2), (3, 4, 5), (6, 7, 8),
            (0, 3, 6), (1, 4, 7), (2, 5, 8),
            (0, 4, 8), (2, 4, 6),
        ]

        for a, b, c in combos:
            m1 = self.cell_mark(a)
            m2 = self.cell_mark(b)
            m3 = self.cell_mark(c)
            if m1 != "" and m1 == m2 == m3:
                self.show_winner(m1)
                return

        if all(btn.text() != "" or not btn.icon().isNull() for btn in self.buttons):
            self.ui.label.setText("Ничья!")

    def cell_mark(self, index):
        btn = self.buttons[index]
        if btn.text() != "":
            return btn.text()
        if not btn.icon().isNull():
            return "♥"
        return ""

    def show_winner(self, mark):
        if mark == "X":
            self.ui.label.setText("Победили крестики!")
        else:
            self.ui.label.setText("Победили сердечки!")

    def reset_game(self):
        for btn in self.buttons:
            btn.setText("")
            btn.setIcon(QIcon())

        self.is_x_turn = True
        self.ui.label.setText("Крестики-Нолики")


if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())