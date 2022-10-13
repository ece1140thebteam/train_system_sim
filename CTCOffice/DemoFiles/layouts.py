from PyQt6.QtWidgets import QWidget, QApplication, QVBoxLayout, QPushButton, QHBoxLayout, QGridLayout
from PyQt6.QtGui import QIcon
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.manual_mode_enabled = False

        self.setWindowTitle("PyQt 6 Layouts")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)

        # vbox = QVBoxLayout()
        # hbox = QHBoxLayout()
        #
        # toggle = QPushButton("Manual Mode")
        # toggle.setCheckable(True)
        # toggle.clicked.connect(self.manual_mode)
        #
        # self.btn1 = QPushButton("Button One")
        # self.btn1.setDisabled(True)
        # self.btn2 = QPushButton("Button Two")
        # self.btn2.setDisabled(True)
        # self.btn3 = QPushButton("Button Three")
        # self.btn4 = QPushButton("Button Four")
        #
        # btn5 = QPushButton("Button Five")
        # btn6 = QPushButton("Button Six")
        #
        # hbox.addWidget(btn5)
        # hbox.addWidget(btn6)
        #
        # vbox.addWidget(toggle)
        # vbox.addWidget(self.btn1)
        # vbox.addWidget(self.btn2)
        # vbox.addWidget(self.btn3)
        # vbox.addWidget(self.btn4)
        #
        # hbox.addLayout(vbox)
        #
        # self.setLayout(hbox)

        grid = QGridLayout()
        btn1 = QPushButton("Button 1")
        btn2 = QPushButton("Button 2")
        btn3 = QPushButton("Button 3")
        btn4 = QPushButton("Button 4")
        btn5 = QPushButton("Button 5")
        btn6 = QPushButton("Button 6")
        btn7 = QPushButton("Button 7")
        btn8 = QPushButton("Button 8")

        grid.addWidget(btn1, 0, 0)
        grid.addWidget(btn2, 0, 1)
        grid.addWidget(btn3, 0, 2)
        grid.addWidget(btn4, 0, 3)
        grid.addWidget(btn5, 1, 0)
        grid.addWidget(btn6, 1, 1)
        grid.addWidget(btn7, 1, 2)
        grid.addWidget(btn8, 1, 3)

        self.setLayout(grid)

    def manual_mode(self):
        self.manual_mode_enabled = not self.manual_mode_enabled
        if self.manual_mode_enabled:
            self.btn1.setDisabled(False)
            self.btn2.setDisabled(False)
        else:
            self.btn1.setDisabled(True)
            self.btn2.setDisabled(True)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
