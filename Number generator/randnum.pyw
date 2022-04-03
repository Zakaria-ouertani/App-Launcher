import sys
from PyQt6.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout
from PyQt6.QtCore import Qt
from PyQt6 import uic
from random import randint

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        uic.loadUi('randnum.ui', self)
        self.generate.clicked.connect(self.num)
        self.setWindowTitle('Generator')
    def num(self):
        a = self.fromm.toPlainText()
        b = self.too.toPlainText()
        print(a,b)
        x = int(a)
        y = int(b) 
        r = randint(x,y)
        print(r)
        r2 = str(r)
        self.output.setText('Result: {0}'.format(r2))
if __name__ == '__main__':
    app = QApplication(sys.argv)
    
    myApp = MyApp()
    myApp.show()

    try:
        sys.exit(app.exec())
    
    except SystemExit:
        print('Closing Window...')
