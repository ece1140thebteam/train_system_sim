import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class CustomDialog(QFileDialog):

   def __init__(self, *args, **kwargs):
      super(CustomDialog, self).__init__(*args, **kwargs)
      
      self.setWindowTitle("File Explorer")
 
      QBtn = QDialogButtonBox.Ok | QDialogButtonBox.Cancel

      self.buttonBox = QDialogButtonBox(QBtn)
      self.buttonBox.accepted.connect(self.accept)
      self.buttonBox.rejected.connect(self.reject)

      self.layout = QVBoxLayout()
      self.layout.addWidget(self.buttonBox)
      self.setLayout(self.layout)


class tabdemo(QTabWidget):
   def __init__(self, parent = None):
      super(tabdemo, self).__init__(parent)
      self.tab1 = QWidget()
      self.tab2 = QWidget()
      self.tab3 = QWidget()
      self.tab4 = QWidget()
      self.tab5 = QWidget()
      self.tab6 = QWidget()
      self.tab7 = QWidget()
      self.tab8 = QWidget()
      self.tab9 = QWidget()
      self.tab10 = QWidget()
      self.tab11 = QWidget()
      self.tab12 = QWidget()
		
      self.addTab(self.tab1,"Wayside 1")
      self.addTab(self.tab2,"Wayside 2")
      self.addTab(self.tab3,"Wayside 3")
      self.addTab(self.tab4,"Wayside 4")
      self.addTab(self.tab5,"Wayside 5")
      self.addTab(self.tab6,"Wayside 6")
      self.addTab(self.tab7,"Wayside 7")
      self.addTab(self.tab8,"Wayside 8")
      self.addTab(self.tab9,"Wayside 9")
      self.addTab(self.tab10,"Wayside 10")
      self.addTab(self.tab11,"Wayside 11")
      self.addTab(self.tab12,"Wayside 12")
      self.tab1UI()
      self.tab2UI()
      self.tab3UI()
      self.tab4UI()
      self.tab5UI()
      self.tab6UI()
      self.tab7UI()
      self.tab8UI()
      self.tab9UI()
      self.tab10UI()
      self.tab11UI()
      self.tab12UI()
      self.setWindowTitle("Track Controller")
      self.setGeometry(100,60,1500,900)



   def tab1UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab1.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)


   def tab2UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab2.setLayout(layout)


   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab3UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab3.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab4UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab4.setLayout(layout)


   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab5UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab5.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab6UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab6.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)
   
   
   def tab7UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab7.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab8UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab8.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab9UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab9.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab10UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab10.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab11UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab11.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)

   def tab12UI(self):
      layout = QVBoxLayout()
      self.btn1 = QPushButton("Upload PLC")
      self.btn1.clicked.connect(self.getfiles)
      layout.addWidget(self.btn1)

      self.contents = QTextEdit()
      layout.addWidget(self.contents)
      self.tab12.setLayout(layout)

   def getfiles(self, s):
      print("click", s)
      dlg = CustomDialog(self)
      if dlg.exec_():
        filenames = dlg.selectedFiles()
      f = open(filenames[0], 'r')

      with f:
         data = f.read()
         self.contents.setText(data)
		
		
def main():
   app = QApplication(sys.argv)
   ex = tabdemo()
   ex.show()
   sys.exit(app.exec_())
	
if __name__ == '__main__':
   main()



