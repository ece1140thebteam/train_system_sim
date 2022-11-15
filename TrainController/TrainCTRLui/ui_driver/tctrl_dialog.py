import sys

from PyQt6.QtWidgets import QApplication, QDialog, QMainWindow, QPushButton, QDialogButtonBox, QVBoxLayout,QLabel


class trainDialog(QDialog):
    def __init__(self, message):
        super().__init__()

        self.setWindowTitle("ALERT!")

        QBtn = QDialogButtonBox.StandardButton.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        self.buttonBox.rejected.connect(self.reject)

        self.layout = QVBoxLayout()
        userMessage = QLabel(message)
        self.layout.addWidget(userMessage)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)