# Author: Jacob Hallberg
# Last Edited: 12/17/2017

from PyQt5 import QtCore, QtGui, QtWidgets
from Calculator import Ui_Calculator
from math import sqrt

class Calculator(QtWidgets.QMainWindow, Ui_Calculator):
    def __init__(self, parent=None):
        self.displayString = ""
        self.displayString2 = ""
        self.whichString = 0
        self.repeat = 0
        self.operator = ""
        super(Calculator, self).__init__(parent)
        self.setupUi(self)
        self.Zero.clicked.connect(self.buttonClicked)
        self.One.clicked.connect(self.buttonClicked)
        self.Two.clicked.connect(self.buttonClicked)
        self.Three.clicked.connect(self.buttonClicked)
        self.Four.clicked.connect(self.buttonClicked)
        self.Five.clicked.connect(self.buttonClicked)
        self.Six.clicked.connect(self.buttonClicked)
        self.Seven.clicked.connect(self.buttonClicked)
        self.Eight.clicked.connect(self.buttonClicked)
        self.Nine.clicked.connect(self.buttonClicked)
        self.Minus.clicked.connect(self.buttonClicked)
        self.Plus.clicked.connect(self.buttonClicked)
        self.Divide.clicked.connect(self.buttonClicked)
        self.Multiply.clicked.connect(self.buttonClicked)
        self.Equal.clicked.connect(self.buttonClicked)
        self.Decimal.clicked.connect(self.buttonClicked)
        self.PlusMinus.clicked.connect(self.buttonClicked)
        self.Sqrt.clicked.connect(self.buttonClicked)
        self.C.clicked.connect(self.buttonClicked)
        self.Back.clicked.connect(self.buttonClicked)


    def buttonClicked(self):
        sender = self.sender()
        if sender.text() in {'+', '-', '÷', '*', '='}:
            self.operations()
        elif sender.text() == 'C':
            self.clear()
        elif sender.text() == '←':
            self.backSpace()        
        elif sender.text() == '√':
            self.root()         
        elif sender.text() == '.':
            self.addDecimal()
        elif sender.text() == '±':
            self.addRemoveMinus()               
        else: 
            self.stringAppender()                    


    def operations(self):
        sender = self.sender()
        self.repeat = 0
        self.whichString = 1
        if sender.text() == '+':
            self.operator = '+'
        if sender.text() == '-':
            self.operator = '-'
        if sender.text() == '÷':
            self.operator = '÷'
        if sender.text() == '*':
            self.operator = '*'
        if sender.text() == '=': 
            if self.operator == '+':
                self.displayString = str(float(self.displayString) + float(self.displayString2))
            if self.operator == '-':
                self.displayString = str(float(self.displayString) - float(self.displayString2))
            if self.operator == '÷':
                self.displayString = str(format(float(self.displayString) / float(self.displayString2), '.2f'))
            if self.operator == '*':
                self.displayString = str(float(self.displayString) * float(self.displayString2))            

            self.displayString2 = ""
            self.whichString = 0
            self.repeat = 1
            self.NumberField.display(self.displayString)

    def stringAppender(self):
        sender = self.sender()
        if self.whichString == 0 and self.repeat == 0:
            self.displayString =  self.displayString + sender.text()
            self.NumberField.display(self.displayString)
        elif self.whichString == 1 and self.repeat == 0:
            self.displayString2 =  self.displayString2 + sender.text()
            self.NumberField.display(self.displayString2)   
        else:
            self.displayString = "" + sender.text()
            self.repeat = 0
            self.NumberField.display(self.displayString)

    def addRemoveMinus(self):
        if self.whichString == 0:
            if '-' in self.displayString:
                self.displayString = self.displayString[1:]
                self.NumberField.display(self.displayString)
            else:
                self.displayString = '-' + self.displayString
                self.NumberField.display(self.displayString)
        if self.whichString == 1:
            if '-' in self.displayString2:
                self.displayString2 = self.displayString2[1:]
                self.NumberField.display(self.displayString2)
            else:
                self.displayString2 = '-' + self.displayString2 
                self.NumberField.display(self.displayString2)

    def addDecimal(self):
        if self.whichString == 0:
            if '.' in self.displayString:
                print("Uable to add Decimal")
            else:
                self.displayString = self.displayString + sender.text() 
                self.NumberField.display(self.displayString)
        else:
            if '.' in self.displayString2:
                print("Uable to add Decimal")
            else:
                self.displayString2 = self.displayString2 + sender.text()
                self.NumberField.display(self.displayString2) 

    def backSpace(self):
        if self.whichString == 0:
            if len(self.displayString) == 1:
                self.displayString = ""
            else:    
                self.displayString = self.displayString[:1]
            self.NumberField.display(self.displayString)
        if self.whichString == 1:
            if len(self.displayString2) == 1:
                self.displayString2 = ""
            else:    
                self.displayString2 = self.displayString[:1]
            self.NumberField.display(self.displayString2)

    def root(self):
        if self.whichString == 0:
                self.displayString = str(format(sqrt(float(self.displayString)), '.2f'))
                self.NumberField.display(self.displayString)
        if self.whichString == 1:
                self.displayString2 = str(format(sqrt(float(self.displayString2)), '.2f'))
                self.NumberField.display(self.displayString2) 
                    
    def clear(self):
        self.displayString = ""
        self.displayString2 = ""
        self.whichString = 0
        self.repeat = 0
        self.operator = ""
        self.NumberField.display('0')

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    nextGui = Calculator()
    nextGui.show()
    sys.exit(app.exec_())