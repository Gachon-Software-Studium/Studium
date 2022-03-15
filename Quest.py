import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

form_class = uic.loadUiType("Quest.ui")[0]
# Info ui

class Quest(QDialog, QWidget, form_class):
    def __init__(self):
        super(Quest,self).__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.BackButton.clicked.connect(self.back)

    def back(self):
        self.close()