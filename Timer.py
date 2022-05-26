from PyQt5.QtCore import QTimer
from PyQt5.QtWidgets import *
from PyQt5 import uic
import datetime
import winsound as sd
import firebase_admin
from firebase_admin import credentials
from firebase_admin import db

from multiprocessing import Process
from threading import Thread

# firebase
import Drowsiness_Detection
import Sticker

db_url = 'https://studium-28d4b-default-rtdb.firebaseio.com/'
cred = credentials.Certificate('studium-28d4b-firebase-adminsdk-94egj-795b3ae3e7.json')
default_app = firebase_admin.initialize_app(cred, {'databaseURL': db_url})

# 데이터 update
ref = db.reference('test')

form_class = uic.loadUiType("ui/Timer.ui")[0]


# Timer ui
class Timer(QDialog, QWidget, form_class):
    def __init__(self):
        super(Timer, self).__init__()

        self.initUI()

        self.timer = QTimer(self)
        self.timer.timeout.connect(self.run_watch)
        self.timer.setInterval(1)
        self.mscounter = 0
        self.isreset = False
        self.showLCD()
        self.show()

    def initUI(self):
        self.setupUi(self)
        self.StartButton.clicked.connect(self.start)
        self.ResetButton.clicked.connect(self.reset)
        self.PauseButton.clicked.connect(self.stop)
        self.BackButton.clicked.connect(self.back)

    def showLCD(self):
        text = str(datetime.timedelta(milliseconds=self.mscounter))[:-7]
        self.lcdNumber.setDigitCount(10)
        if not self.isreset:
            self.lcdNumber.display(text)
        else:
            self.lcdNumber.display('0')

    def run_watch(self):
        self.mscounter += 1
        self.showLCD()

    def start(self):
        detect_return=0
        p0 = Process(target=self.timer.start(),)
        p0.start()
        p0.join()


    def reset(self):
        self.timer.stop()
        ref.update({'time': self.mscounter / 1000})
        self.mscounter = 0
        self.isreset = False
        self.showLCD()

    def stop(self):
        self.timer.stop()

    def back(self):
        self.close()

    #def detect_start(self):
    #    while 1:
    #        if self.detect_return == 0:
    #            self.detect_return = Drowsiness_Detection.detect()
    #        else:
    #            break

    #def timer_start(self):
    #    self.timer.start()

def beepsound():
    fr = 2000
    du = 1000
    sd.Beep(fr, du)


def time_check(i):
    playtime = i
    print("playtime : %2f" % playtime)
    if playtime > 10:
        beepsound()
        print("Time Limit over")
        # 졸음 stack +1
