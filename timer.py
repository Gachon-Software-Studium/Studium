import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("timer.ui")[0]

class Timer(QDialog, QWidget, form_class):
    def __init__(self):
        super(Timer,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.toolButton_4.clicked.connect(self.back)

    def back(self):
        self.close()

