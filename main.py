import sys
from PyQt5.QtWidgets import *
from PyQt5 import uic

from Timer import Timer


form_class = uic.loadUiType("ui/Main.ui")[0]


# Main ui
class MainWindow(QMainWindow, QWidget, form_class):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)

    def start(self):
        self.hide()
        self.time = Timer()
        self.time.exec()
        self.show()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myWindow = MainWindow()
    sys.exit(app.exec_())
