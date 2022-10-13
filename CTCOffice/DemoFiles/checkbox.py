from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout, QCheckBox, QLabel
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 CheckBox")
        self.setWindowIcon(QIcon("../Images/TrainIcon.png"))
        self.setGeometry(500,200,500,400)

        self.create_checkbox()

    def create_checkbox(self):
        hbox = QHBoxLayout()
        self.check1 = QCheckBox("Python")
        self.check1.setFont(QFont("Times New Roman", 14))
        self.check1.toggled.connect(self.item_selected)
        hbox.addWidget(self.check1)

        self.check2 = QCheckBox("Java")
        self.check2.setFont(QFont("Times New Roman", 14))
        self.check2.toggled.connect(self.item_selected)
        hbox.addWidget(self.check2)

        self.check3 = QCheckBox("C++")
        self.check3.setFont(QFont("Times New Roman", 14))
        self.check3.toggled.connect(self.item_selected)
        hbox.addWidget(self.check3)

        self.check4 = QCheckBox("C#")
        self.check4.setFont(QFont("Times New Roman", 14))
        self.check4.toggled.connect(self.item_selected)
        hbox.addWidget(self.check4)

        vbox = QVBoxLayout()

        self.label = QLabel("Label")
        self.label.setFont(QFont("Sanserif", 15))
        self.label.setStyleSheet('color:red')

        vbox.addWidget(self.label)
        vbox.addLayout(hbox)

        self.setLayout(vbox)

    def item_selected(self):
        value = ""

        if self.check1.isChecked():
            value = self.check1.text()
        if self.check2.isChecked():
            value = self.check2.text()
        if self.check3.isChecked():
            value = self.check3.text()
        if self.check4.isChecked():
            value = self.check4.text()

        self.label.setText("You have selected : " + value)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())