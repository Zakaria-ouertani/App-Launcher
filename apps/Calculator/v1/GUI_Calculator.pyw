import sys
from os.path import exists
from PyQt5 import uic
from PyQt5.QtWidgets import QPushButton,QMainWindow,QApplication,QShortcut
from PyQt5.QtGui import QKeySequence
from ffops import *
class MainWindow(QMainWindow):
    f = open("hist.txt","a+")
    f.close()
    def hbigg(self):
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()
        print(w," / ",h)
        if h <= 380:
            self.resize(w-2,600)
        else:
            self.resize(w-2,340)
    def wbigg(self):
        w = self.frameGeometry().width()
        h = self.frameGeometry().height()
        print(w," / ",h)
        if w <= 290:
            self.resize(600,h-32)
            self.hist.setText("History    <-")

        else:
            self.resize(280,h-32)
            self.hist.setText("History    ->")
            
    def __init__(self):
        super().__init__()
        uic.loadUi("GUI_Calculator.ui", self)
        history = open("hist.txt").read()
        self.histb.setPlainText(history)
        
        # Mouse Control
        self.show()
        self.f1.clicked.connect(self.ff1)
        self.f2.clicked.connect(self.ff2)
        self.f3.clicked.connect(self.ff3)
        self.f4.clicked.connect(self.ff4)
        self.f5.clicked.connect(self.ff5)
        self.f6.clicked.connect(self.ff6)
        self.f7.clicked.connect(self.ff7)
        self.f8.clicked.connect(self.ff8)
        self.f9.clicked.connect(self.ff9)
        self.fadd.clicked.connect(self.ffadd)
        self.fsub.clicked.connect(self.ffsub)
        self.fmul.clicked.connect(self.ffmul)
        self.fdiv.clicked.connect(self.ffdiv)
        self.fcls.clicked.connect(self.ffcls)
        self.fdel.clicked.connect(self.ffdel)
        self.paright.clicked.connect(self.ffparight)
        self.parleft.clicked.connect(self.ffparleft)
        self.f0.clicked.connect(self.ff0)
        self.f00.clicked.connect(self.ff00)
        self.frac.clicked.connect(self.ffdot)
        self.calc.clicked.connect(self.result)
        self.pgm.clicked.connect(self.hbigg)
        self.hist.clicked.connect(self.wbigg)
        self.clearhist.clicked.connect(self.ffclearhist)
        
        #Keyboard control
        QShortcut(QKeySequence("Ctrl+Q"), self).activated.connect(QApplication.instance().quit)
        QShortcut(QKeySequence("1"), self).activated.connect(self.ff1)
        QShortcut(QKeySequence("2"), self).activated.connect(self.ff2)
        QShortcut(QKeySequence("3"), self).activated.connect(self.ff3)
        QShortcut(QKeySequence("4"), self).activated.connect(self.ff4)
        QShortcut(QKeySequence("5"), self).activated.connect(self.ff5)
        QShortcut(QKeySequence("6"), self).activated.connect(self.ff6)
        QShortcut(QKeySequence("7"), self).activated.connect(self.ff7)
        QShortcut(QKeySequence("8"), self).activated.connect(self.ff8)
        QShortcut(QKeySequence("9"), self).activated.connect(self.ff9)
        QShortcut(QKeySequence("+"), self).activated.connect(self.ffadd)
        QShortcut(QKeySequence("-"), self).activated.connect(self.ffsub)
        QShortcut(QKeySequence("*"), self).activated.connect(self.ffmul)
        QShortcut(QKeySequence("/"), self).activated.connect(self.ffdiv)
        QShortcut(QKeySequence("Delete"), self).activated.connect(self.ffcls)
        QShortcut(QKeySequence("Ctrl+Backspace"), self).activated.connect(self.ffcls)
        QShortcut(QKeySequence("Backspace"), self).activated.connect(self.ffdel)
        QShortcut(QKeySequence("("), self).activated.connect(self.ffparight)
        QShortcut(QKeySequence(")"), self).activated.connect(self.ffparleft)
        QShortcut(QKeySequence("0"), self).activated.connect(self.ff0)
        QShortcut(QKeySequence("Ctrl+0"), self).activated.connect(self.ff00)
        QShortcut(QKeySequence("."), self).activated.connect(self.ffdot)
        QShortcut(QKeySequence("Ctrl+R"), self).activated.connect(self.ffclearhist)
        QShortcut(QKeySequence("Return"), self).activated.connect(self.result)
        
    def ff1(self):
        text = self.res.text()
        self.res.setText(text + "1")
    def ff2(self):
        text = self.res.text()
        self.res.setText(text + "2")

    def ff3(self):
        text = self.res.text()
        self.res.setText(text + "3")

    def ff4(self):
        text = self.res.text()
        self.res.setText(text + "4")

    def ff5(self):
        text = self.res.text()
        self.res.setText(text + "5")
        
    def ff6(self):
        text = self.res.text()
        self.res.setText(text + "6")
        
    def ff7(self):
        text = self.res.text()
        self.res.setText(text + "7")

    def ff8(self):
        text = self.res.text()
        self.res.setText(text + "8")

    def ff9(self):
        text = self.res.text()
        self.res.setText(text + "9")

    def ff0(self):
        text = self.res.text()
        self.res.setText(text + "0")

    def ff00(self):
        text = self.res.text()
        self.res.setText(text + "00")

    def ffparleft(self):
        text = self.res.text()
        self.res.setText(text + ")")

    def ffparight(self):
        text = self.res.text()
        self.res.setText(text + "(")
        
    def ffadd(self):
        text = self.res.text()
        self.res.setText(text + "+")

    def ffsub(self):
        text = self.res.text()
        self.res.setText(text + "-")

    def ffmul(self):
        text = self.res.text()
        self.res.setText(text + "*")

    def ffdiv(self):
        text = self.res.text()
        self.res.setText(text + "/")

    def ffcls(self):
        text = self.res.text()
        self.res.setText("")
    def ffdel(self):
        text = self.res.text()
        self.res.setText(text[:-1])
    def ffdot(self):
        text = self.res.text()
        self.res.setText(text + ".")
    def ffclearhist(self):
        f = open("hist.txt","w")
        f.close
        history = open("hist.txt").read()
        self.histb.setPlainText(history)
    def result(self):
        text = self.res.text()
        f = open("hist.txt","a+")
        f.write("\n" + text + " = ")
        try:
            result = str(eval(text, {}, {}))
            f.write(result + "\n")
        except Exception:
            result = "ERROR"
        self.res.setText(result)
        f.close
        history = open("hist.txt").read()
        self.histb.setPlainText(history)

#main
if __name__=="__main__":
    app=QApplication([])
    window = MainWindow()
    window.show
    app.exec()
    #sys.exit()