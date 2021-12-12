import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Info.ui")[0]

class Info(QDialog, QWidget, form_class):
    def __init__(self):
        super(Info,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.toolButton_3.clicked.connect(self.back)

    def back(self):
        self.close()

