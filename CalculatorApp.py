from PyQt5 import QtWidgets as qtw
from PyQt5 import (QtCore, QtGui, uic)
from PyQt5.QtCore import Qt
import sys


class CalculatorWindow(qtw.QMainWindow):
    '''constructor'''
    def __init__(self):
        super(CalculatorWindow,self).__init__()
        uic.loadUi("calcUi.ui", self)
        self.show()
        
        
        #button bindings
        self.percentButton.clicked.connect(lambda:self.press_it("%"))
        self.cancelButton.clicked.connect(lambda:self.press_it("C"))
        self.backButton.clicked.connect(lambda:self.remove_it())
        self.divideButton.clicked.connect(lambda:self.press_it("/"))
        self.sevenButton.clicked.connect(lambda:self.press_it("7"))
        self.eightButton.clicked.connect(lambda:self.press_it("8"))
        self.nineButton.clicked.connect(lambda:self.press_it("9"))
        self.timesButton.clicked.connect(lambda:self.press_it("*"))
        self.fourButton.clicked.connect(lambda:self.press_it("4"))
        self.fiveButton.clicked.connect(lambda:self.press_it("5"))
        self.sixButton.clicked.connect(lambda:self.press_it("6"))
        self.minusButton.clicked.connect(lambda:self.press_it("-"))
        self.oneButton.clicked.connect(lambda:self.press_it("1"))
        self.twoButton.clicked.connect(lambda:self.press_it("2"))
        self.threeButton.clicked.connect(lambda:self.press_it("3"))
        self.addButton.clicked.connect(lambda:self.press_it("+"))
        self.posnegButton.clicked.connect(lambda:self.plusminus_it())
        self.zeroButton.clicked.connect(lambda:self.press_it("0"))
        self.pointButton.clicked.connect(lambda:self.point_it())
        self.equalButton.clicked.connect(lambda:self.math_it())
       
    
    def math_it(self):
        '''works out the answer by using the eval function'''
        displayContents = self.displayLabel.text()#
        try:
            answer = eval(displayContents) #does the math using string with operators
            self.displayLabel.setText(str(answer))
            
        except:
            self.displayLabel.setText('ERROR')
    def plusminus_it(self):
        '''switches between negative and positive values
            by replacing "-" with "" and if there is non put one
            #note there are still issues with this solution
        '''
        displayContents = self.displayLabel.text()
        if displayContents[0] =="-":
            
            self.displayLabel.setText(displayContents[1:])
            
        else:
            self.displayLabel.setText(f'-{displayContents}')
            
       
        
    def remove_it(self):
        '''removes previous character from display contents'''
        displayContents = self.displayLabel.text()
        displayContents = displayContents [:-1] # remomoves the last item from the displayContents
        self.displayLabel.setText(f'{displayContents}')
        
    def  point_it(self):
          '''puts a dot in display contenct if there is no dot already '''
          displayContents = self.displayLabel.text()
          if displayContents[-1]==".": #allows other values to have a decimal, alternative if "." in displayContents: pass
              pass
          else:
              self.displayLabel.setText(f'{displayContents}.')
          
        
    def press_it(self,pressed):
        '''handles events from all buttons connected to it'''
        if pressed == "C":
            self.displayLabel.setText("0")
        else:
            #remove leading zero
            if self.displayLabel.text() =="0":
                self.displayLabel.setText("")
                
            #concatenate input with what was there already
            self.displayLabel.setText(f'{self.displayLabel.text()}{pressed}')



def main():
    app = qtw.QApplication(sys.argv)
    calculatorWindow = CalculatorWindow()
    app.exec_()
    qtw.QApplication.quit()
main()