from Caculator2 import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtGui import *
from math import *
class BMICaculate(Ui_Dialog):
    def __init__(self):
        self.dialog = QDialog()
        super().setupUi(self.dialog)
        self.line_height.returnPressed.connect(self.height_changed)
        self.line_weight.returnPressed.connect(self.weight_changed)
        self.line_height.textChanged.connect(self.height_changed)
        self.line_weight.textChanged.connect(self.weight_changed)
        self.Button_caculate.clicked.connect(self.caculate)
        self.Button_recaculate.clicked.connect(self.recaculate)
        self.selectMode.buttonClicked.connect(self.select_Mode)
    def height_changed(self):
        try:
            self.height = float(self.line_height.text())/100
            print(self.height)
        except:
            pass
    def weight_changed(self):
        try:
            self.weight = float(self.line_weight.text())
        except:
            pass
    def recaculate(self):
        self.line_height.clear()
        self.line_weight.clear()
        self.line_score.clear()
        self.line_res.clear()
    def select_Mode(self):
        self.mode = self.selectMode.checkedButton().text()
    def caculate(self):
        if not(self.weight and self.height and self.mode):
            return
        bmiScore= round(self.weight/self.height**2,1)
        print(bmiScore)
        self.line_score.setText(str(bmiScore))
        if(self.mode == "男"):
            if bmiScore <= 17.8:
                self.line_res.setText("低体重")
            elif bmiScore <= 23.9:
                self.line_res.setText("正常")
            elif bmiScore <= 27.9:
                self.line_res.setText("超重")
            else:
                self.line_res.setText("肥胖")
        elif self.mode == "女":
            if bmiScore <= 17.1:
                self.line_res.setText("低体重")
            elif bmiScore <= 23.9:
                self.line_res.setText("正常")
            elif bmiScore <= 27.9:
                self.line_res.setText("超重")
            else:
                self.line_res.setText("肥胖")

