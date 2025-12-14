from myPuzzle import *
from game import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import showOriginal
import HelpTips
import random
import os
from PIL import Image
import math

class ShowCode(Ui_Dialog):
    def __init__(self,path):
        super().__init__()
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.graphicsView = game(path)
        self.dialogOriginal = QDialog(self.dialog)
        self.OriginalWindow = showOriginal.Ui_Dialog()
        self.OriginalWindow.setupUi(self.dialogOriginal)
        self.n=3
        self.spinBox_num.setValue(self.n)
        self.graphicsView.setObjectName("graphicsView")
        self.horizontalLayout_2.insertWidget(0,self.graphicsView)
        self.timeCounter.setDigitCount(2)
        self.timeCounter.segmentStyle()
        self.show_originalPic.clicked.connect(self.showOri)
        self.try_newPic.clicked.connect(self.tryNew)
        self.challengeMode.clicked.connect(self.challenge)
        self.recompose.clicked.connect(self.reCom)
        self.spinBox_num.valueChanged.connect(self.pixNum)
        self.selfChoose.clicked.connect(self.selfOption)
        self.spinBox_num.setMinimum(1)
        self.help.clicked.connect(self.ShowHelpWindow)
        self.gameTime =int(self.n * self.n * math.log(self.n))
        self.timeCounter.display(self.gameTime)

    def checkGameover(self):
        if self.graphicsView.gameOver():
            self.gameoverRecover()
            self.checkTime.stop()
    def countImg(self):
        floaderPath = 'image/'
        files = os.listdir(floaderPath)
        num = len(files)
        return num
    def showOri(self):
        img = QPixmap(self.graphicsView.path)
        scene = QGraphicsScene()
        self.OriginalWindow.graphicsView.setScene(scene)
        scene.addPixmap(img.scaled(self.OriginalWindow.graphicsView.size(),Qt.KeepAspectRatio, Qt.SmoothTransformation))
        self.dialogOriginal.show()

    def tryNew(self):
        cnt = self.countImg()
        self.dialog.setMinimumSize(0, 0)
        self.dialog.setMaximumSize(16777215, 16777215)
        a = random.randint(1, cnt)
        self.graphicsView.path = f'image/图片{a}.jpg'
        self.graphicsView.recover(self.graphicsView.path)
    def challenge(self):
        self.graphicsView.challengeMode = True
        self.graphicsView.imageCut(self.n)
        self.graphicsView.random_draw_img()
        self.sendTime = QTimer(self.dialog)
        self.sendTime.start(1000)
        self.sendTime.timeout.connect(self.countDown)
        self.forbid()

    def reCom(self):
        self.graphicsView.imageCut(self.n)
        self.graphicsView.random_draw_img()
        self.dialog.setFixedSize(self.dialog.size())
        self.checkTime = QTimer(self.dialog)
        self.checkTime.start(500)
        self.checkTime.timeout.connect(self.checkGameover)
    def pixNum(self):
        self.n= int(self.spinBox_num.value())
        self.gameTime =int(self.n * self.n * math.log(self.n))
        self.timeCounter.display(self.gameTime)
        self.graphicsView.recover(self.graphicsView.path)

    def selfOption(self):
        filePath, _ = QFileDialog.getOpenFileName(self.dialog, '请选择您要使用的图片', r'D:/Users/70887/Desktop', '*.jpg')
        if not filePath:
            return
        self.dialog.setMinimumSize(0, 0)
        self.dialog.setMaximumSize(16777215, 16777215)
        self.graphicsView.path = filePath
        self.graphicsView.recover(self.graphicsView.path)
        img = Image.open(filePath)
        cnt = self.countImg()
        img.save(f'image/图片{cnt+1}.jpg')
    def gameoverRecover(self):
        if self.graphicsView.gameOver():
            self.dialog.setMinimumSize(0, 0)
            self.dialog.setMaximumSize(16777215, 16777215)
            self.graphicsView.recover(self.graphicsView.path)
            return True
        if self.timeCounter.value() == 0:
            self.dialog.setMinimumSize(0, 0)
            self.dialog.setMaximumSize(16777215, 16777215)
            self.graphicsView.recover(self.graphicsView.path)
        return False
    def ShowHelpWindow(self):
        dialog = QDialog()
        helpWindow = HelpTips.Ui_Dialog()
        helpWindow.setupUi(dialog)
        dialog.show()
        dialog.exec_()
    def countDown(self):
        if not self.graphicsView.gameOver():
            if self.timeCounter.value() - 1 != 0:
                self.timeCounter.display(self.timeCounter.value()-1)
            else:
                self.timeCounter.display(self.timeCounter.value()-1)
                self.sendTime.stop()
                if self.graphicsView.challengeMode:
                    QMessageBox.information(self.dialog,'遗憾', '未能完成挑战T T')
                self.gameoverRecover()
                self.graphicsView.challengeMode = False
                self.unforbid()
                self.timeCounter.display(self.gameTime)
        else:
            self.sendTime.stop()
            if self.graphicsView.challengeMode:
                time = self.gameTime-self.timeCounter.value()
                QMessageBox.information(self.dialog, '恭喜', f'恭喜完成挑战!\n用时{time}秒!')
            self.unforbid()
            self.timeCounter.display(self.gameTime)
        if self.gameoverRecover():
            self.graphicsView.challengeMode = False
    def forbid(self):
        self.challengeMode.setEnabled(False)
        self.spinBox_num.setEnabled(False)
        self.recompose.setEnabled(False)
        self.try_newPic.setEnabled(False)
        self.selfChoose.setEnabled(False)
    def unforbid(self):
        self.challengeMode.setEnabled(True)
        self.spinBox_num.setEnabled(True)
        self.recompose.setEnabled(True)
        self.try_newPic.setEnabled(True)
        self.selfChoose.setEnabled(True)