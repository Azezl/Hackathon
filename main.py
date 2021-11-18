import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication, QWidget, QFrame
import sqlite3
import FAR_API



class Welcome_Screen(QDialog):
    def __init__(self):
        super(Welcome_Screen,self).__init__()
        loadUi("Welcome_Screen.ui",self)
        self.password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Login.clicked.connect(self.gotofirst)
        self.guest.clicked.connect(self.gotofirst)

    def gotofirst(self):
        first = First_Window()
        widget.addWidget(first)
        widget.setCurrentIndex(widget.currentIndex()+1)


class First_Window(QDialog):
    def __init__(self):
        super(First_Window,self).__init__()
        loadUi("First_Window.ui",self)
        self.Button1.clicked.connect(self.gotofunction)


    def gotofunction(self):
        far_field = self.Far.text()
        test_field = self.test.text()
        product_field = self.product.currentText()
        print("Button Clicked")

        if ((len(far_field) == 0) and ((len(test_field) == 0) or (product_field != 'None'))):
            self.errmsg.setText("Please Enter Valid Details")
        else:
            print("Processing Far Field")
            if (len(far_field) != 0):
                print("Before")
                var = FAR_API.far_01_api_id(far_field)
                print("After")
                if(var == 'Test does not exist in FAR'):
                    self.errmsg.setText("Test does not exist in FAR")
                else:
                    print("Correct far link Entered")
                    self.far_dict = var
                    third = Second_Window()
                    widget = widget.addWidget(third)
                    widget.setCurrentIndex(widget.currentIndex() + 1)
            else:
                var = FAR_API.far_01_api_product_testName()




class Second_Window(QDialog):
    def __init__(self):
        print("Entered Third Window")
        super(Second_Window,self).__init__()
        loadUi("Second_Window.ui",self)
        print("Exited")
        #self.Check.setText(far_dict['test_id'])







app = QApplication(sys.argv)
welcome = Welcome_Screen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(welcome)
widget.setFixedWidth(800)
widget.setFixedHeight(600)
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")