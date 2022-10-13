from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
from PyQt6.QtGui import QIcon, QFont
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 CheckBox")
        self.setWindowIcon(QIcon("images/TrainIcon.png"))
        self.setGeometry(500, 200, 500, 400)

        vbox = QVBoxLayout()

        tableWidget = QTableWidget()
        tableWidget.setRowCount(3)
        tableWidget.setColumnCount(3)
        tableWidget.setStyleSheet('background-color:yellow')
        tableWidget.setFont(QFont("Times New Roman", 14)) 

        tableWidget.setItem(0, 0, QTableWidgetItem("FName"))
        tableWidget.setItem(0, 1, QTableWidgetItem("LName"))
        tableWidget.setItem(0, 2, QTableWidgetItem("Email"))

        tableWidget.setItem(1, 0, QTableWidgetItem("Hudson"))
        tableWidget.setItem(1, 1, QTableWidgetItem("Panning"))
        tableWidget.setItem(1, 2, QTableWidgetItem("hup7"))

        tableWidget.setItem(2, 0, QTableWidgetItem("John"))
        tableWidget.setItem(2, 1, QTableWidgetItem("Smith"))
        tableWidget.setItem(2, 2, QTableWidgetItem("jos77"))

        vbox.addWidget(tableWidget)

        self.setLayout(vbox)




app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())