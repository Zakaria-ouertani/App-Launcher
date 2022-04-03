
import sys
import pyperclip as clip
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from random import randint
from time import sleep

class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("main.ui", self)
        self.setWindowTitle("Prnt.sc generator")
        self.generate.clicked.connect(self.gen)
        self.openb.clicked.connect(self.inbro)
        self.openb2.clicked.connect(self.opinbro)
        self.








if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    
