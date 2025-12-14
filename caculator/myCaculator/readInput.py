from Caculator1 import Ui_Dialog
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from math import *
class readInput(Ui_Dialog):
    def __init__(self):
        self.res=''
        self.dialog = QDialog()
        self.setupUi(self.dialog)
        self.Button_0.clicked.connect(self.btn0_pressed)
        self.Button_1.clicked.connect(self.btn1_pressed)
        self.Button_2.clicked.connect(self.btn2_pressed)
        self.Button_3.clicked.connect(self.btn3_pressed)
        self.Button_4.clicked.connect(self.btn4_pressed)
        self.Button_5.clicked.connect(self.btn5_pressed)
        self.Button_6.clicked.connect(self.btn6_pressed)
        self.Button_7.clicked.connect(self.btn7_pressed)
        self.Button_8.clicked.connect(self.btn8_pressed)
        self.Button_9.clicked.connect(self.btn9_pressed)
        self.Button_plus.clicked.connect(self.btnPlus_pressed)
        self.Button_minus.clicked.connect(self.btnMinus_pressed)
        self.Button_multi.clicked.connect(self.btnMulti_pressed)
        self.Button_devide.clicked.connect(self.btnDevide_pressed)
        self.Button_point.clicked.connect(self.btnPoint_pressed)
        self.Button_clear.clicked.connect(self.btnClear_pressed)
        self.Button_power.clicked.connect(self.btnPower_pressed)
        self.Button_sqrt.clicked.connect(self.btnSqrt_pressed)
        self.Button_reci.clicked.connect(self.btnReci_pressed)
        self.Button_mod.clicked.connect(self.btnMod_pressed)
        self.Button_LBracket.clicked.connect(self.btnLBracket_pressed)
        self.Button_RBracket.clicked.connect(self.btnRBracket_pressed)
        self.Button_back.clicked.connect(self.btnBack_pressed)
        self.Button_equal.clicked.connect(self.btneq_pressed)
        self.cursor = self.outWindow.textCursor()
        self.cursor.movePosition(QTextCursor.End)
        self.outWindow.setTextCursor(self.cursor)
        self.line_height.returnPressed.connect(self.height_changed)
        self.line_weight.returnPressed.connect(self.weight_changed)
        self.line_height.textChanged.connect(self.height_changed)
        self.line_weight.textChanged.connect(self.weight_changed)
        self.Button_caculate.clicked.connect(self.caculate)
        self.Button_recaculate.clicked.connect(self.recaculate)
        self.selectMode.buttonClicked.connect(self.select_Mode)
    def btn0_pressed(self):
        self.outWindow.insertPlainText(self.Button_0.text())
    def btn1_pressed(self):
        self.outWindow.insertPlainText(self.Button_1.text())
    def btn2_pressed(self):
        self.outWindow.insertPlainText(self.Button_2.text())
    def btn3_pressed(self):
        self.outWindow.insertPlainText(self.Button_3.text())
    def btn4_pressed(self):
        self.outWindow.insertPlainText(self.Button_4.text())
    def btn5_pressed(self):
        self.outWindow.insertPlainText(self.Button_5.text())
    def btn6_pressed(self):
        self.outWindow.insertPlainText(self.Button_6.text())
    def btn7_pressed(self):
        self.outWindow.insertPlainText(self.Button_7.text())
    def btn8_pressed(self):
        self.outWindow.insertPlainText(self.Button_8.text())
    def btn9_pressed(self):
        self.outWindow.insertPlainText(self.Button_9.text())
    def btnPoint_pressed(self):
        self.outWindow.insertPlainText(self.Button_point.text())
    def btnClear_pressed(self):
        self.outWindow.clear()
        self.ansWindow.clear()
    def btnPlus_pressed(self):
        self.outWindow.insertPlainText(self.Button_plus.text())
    def btnMinus_pressed(self):
        self.outWindow.insertPlainText(self.Button_minus.text())
    def btnMulti_pressed(self):
        self.outWindow.insertPlainText(self.Button_multi.text())
    def btnDevide_pressed(self):
        self.outWindow.insertPlainText(self.Button_devide.text())
    def btnPower_pressed(self):
        self.outWindow.insertPlainText(self.Button_power.text())
    def btnSqrt_pressed(self):
        self.outWindow.insertPlainText(self.Button_sqrt.text())
    def btnMod_pressed(self):
        self.outWindow.insertPlainText(self.Button_mod.text())
    def btnLBracket_pressed(self):
        self.outWindow.insertPlainText(self.Button_LBracket.text())
    def btnRBracket_pressed(self):
        self.outWindow.insertPlainText(self.Button_RBracket.text())
    def btnBack_pressed(self):
        str=self.outWindow.toPlainText()
        str=str[:-1]
        self.outWindow.setPlainText(str)
        self.outWindow.moveCursor(QTextCursor.End)
    def btnReci_pressed(self):
        if self.outWindow.toPlainText() == '':
            return
        self.res=self.outWindow.toPlainText()
        while (self.Button_power.text() in self.res):
            self.res = self.res.replace(self.Button_power.text(), '**')
        while (self.Button_sqrt.text() in self.res):
            k = self.res.find(self.Button_sqrt.text())
            if self.res[k + 1] != '(':
                self.res = self.res[:k + 1] + "(" + self.res[k + 1:]
                for i in range(k + 2, len(self.res)):
                    if i == len(self.res) - 1 and '0' <= self.res[i] <= '9':
                        self.res = self.res + ')'
                    if not ('0' <= self.res[i] <= '9'):
                        self.res = self.res[:i] + ")" + self.res[i:]
                        break
            self.res = self.res.replace(self.Button_sqrt.text(), 'sqrt')
            # print(self.res)
        ans=round(1/eval(self.res),6)
        self.ansWindow.setPlainText(str(ans))
        self.outWindow.setPlainText(str(eval(self.res)))
        # self.res=str(ans)
        self.cursor.movePosition(QTextCursor.End)
        self.outWindow.setTextCursor(self.cursor)
    def btneq_pressed(self):
        try:
            if self.outWindow.toPlainText() == '':
                return
            res = self.outWindow.toPlainText()
            while(self.Button_power.text() in res):
                res=res.replace(self.Button_power.text(),'**')
            while (self.Button_sqrt.text() in res):
                k=res.find(self.Button_sqrt.text())
                if res[k+1] != '(':
                    res=res[:k+1]+"("+res[k+1:]
                    for i in range(k+2,len(res)):
                        if i == len(res) - 1 and '0' <= res[i] <= '9':
                            res = res + ')'
                        if not('0'<=res[i]<='9'):
                            res=res[:i]+")"+res[i:]
                            break
                res = res.replace(self.Button_sqrt.text(), 'sqrt')
                # print(self.res)

            # print(self.res,res)
            if self.ansWindow.toPlainText() != '' and res == self.res:
                self.outWindow.setPlainText(self.ansWindow.toPlainText())
                self.outWindow.moveCursor(QTextCursor.End)
                self.ansWindow.clear()
                return
            self.res=self.outWindow.toPlainText()
            while(self.Button_power.text() in self.res):
                self.res=self.res.replace(self.Button_power.text(),'**')
            while (self.Button_sqrt.text() in self.res):
                k=self.res.find(self.Button_sqrt.text())
                if self.res[k+1] != '(':
                    self.res=self.res[:k+1]+"("+self.res[k+1:]
                    for i in range(k+2,len(self.res)):
                        if i == len(self.res) - 1 and '0' <= self.res[i] <= '9':
                            self.res = self.res + ')'
                        if not('0'<=self.res[i]<='9'):
                            self.res=self.res[:i]+")"+self.res[i:]
                            break
                self.res = self.res.replace(self.Button_sqrt.text(), 'sqrt')
                # print(self.res)

            ans=round(eval(self.res),6)
            # self.res=str(ans)
            self.ansWindow.setPlainText(str(ans))
            self.cursor.movePosition(QTextCursor.End)
            self.outWindow.setTextCursor(self.cursor)
        except:
            error = QMessageBox()
            error.critical(self.dialog,'错误','请合法输入')

    def height_changed(self):
        try:
            self.height = float(self.line_height.text())/100
            # print(self.height)
        except:
            pass
    def weight_changed(self):
        try:
            self.weight = float(self.line_weight.text())
        except:
            pass
    def recaculate(self):
        self.line_height.clear()
        self.height=0
        self.line_weight.clear()
        self.weight=0
        self.line_score.clear()
        self.line_res.clear()
    def select_Mode(self):
        try:
            self.mode = self.selectMode.checkedButton().text()
        except:
            pass
    def caculate(self):

        try:
            if not(self.weight and self.height and self.mode !=''):
                return
            bmiScore= round(self.weight/self.height**2,1)
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
        except:
            pass

