import sys
import webbrowser
import pyperclip as clip
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from random import randint
from time import sleep
from threading import Timer
class MyApp(QWidget):
    
    def __init__(self):
        super().__init__()
        uic.loadUi("prnt.ui", self)
        self.setWindowTitle("Prnt.sc generator")
        self.generate.clicked.connect(self.gen)
        self.openb.clicked.connect(self.inbro)
        self.openb2.clicked.connect(self.opinbro)
    
    def gen(self):
        global base
        base = "https://prnt.sc/"
        for i in range(6):
            num = randint (97,122)
            base+=chr(num)
            clip.copy(base)
        self.pipboard.setText('{0}'.format("Copied link to clip board!"))
        self.output.setText('{0}'.format(base))
        #time.sleep(10)
        #Timer(3.0,self.pipboard.setText('{0}'.format("a ")))

    def inbro(self):
        #link=gen(self)
        print(base)
        webbrowser.open(base)
    
    def opinbro(self):
        global base
        base = "https://prnt.sc/"
        for i in range(6):
            num = randint (97,122)
            base+=chr(num)
            clip.copy(base)
        self.pipboard.setText('{0}'.format("Copied link to clip board!"))
        
        self.output.setText('{0}'.format(base))
        print(base)
        webbrowser.open(base)
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    
    except SystemExit:
        print('Closing Window...')
