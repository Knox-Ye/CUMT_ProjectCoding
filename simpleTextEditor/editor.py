import sys
import os
import panel
import textedit
from PyQt5.QtCore import Qt
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QWidget, QApplication, QColorDialog, QFontDialog, QTextEdit, QFileDialog, QMessageBox
from PyQt5.QtCore import QFile, QFileInfo
from PyQt5.QtGui import QPalette, QTextCursor

class Editor(QtWidgets.QMainWindow, panel.Ui_MainWindow):
    def __init__(self, parent=None):
        super(Editor, self).__init__(parent)
        self.setupUi(self)
        self.setWindowTitle("Notepad")
        self.actionOpen.triggered.connect(self.fileOpen)
        self.actionNew.triggered.connect(self.fileNew)
        self.actionSave.triggered.connect(self.fileSave)
        self.actionClose.triggered.connect(self.closeEvent)
        self.actionPile.triggered.connect(self.filePile)
        self.actionHorizontal.triggered.connect(self.fileHorizontal)
        self.actionVertical.triggered.connect(self.fileVertical)
        self.actionDelete.triggered.connect(self.fileUndo)
        self.actionRecover.triggered.connect(self.fileRedo)
        self.actionCopy.triggered.connect(self.fileCopy)
        self.actionCut.triggered.connect(self.fileCut)
        self.actionPaste.triggered.connect(self.filePaste)
        self.actionBold.triggered.connect(self.fileBold)
        self.actionItalic.triggered.connect(self.fileItalic)
        self.actionUnderline.triggered.connect(self.fileUnderline)
        self.fontComboBox.currentFontChanged.connect(self.fileChangeFont)
        self.actionSearch.triggered.connect(self.fileSearch)
        self.fontSize = 9
        self.timer = QtCore.QTimer(self)
        self.FontSizeBig.clicked.connect(self.Bigger)
        self.FontSizeSmall.clicked.connect(self.Smaller)
        self.FontSize_spin.setValue(self.fontSize)
        self.FontSize_spin.valueChanged.connect(self.fontSizeChange)
    def fontSizeChange(self):
        try:
            self.fontSize = self.FontSize_spin.value()
            self.FontSize_spin.setValue(self.fontSize)
            sub = self.mdiArea.activeSubWindow().widget()
            font = sub.currentFont()
            font.setPointSize(self.fontSize)
            sub.setFont(font)
        except:
            pass
    def Bigger(self):
        try:
            sub = self.mdiArea.activeSubWindow().widget()
            font = sub.currentFont()
            self.fontSize +=1
            self.FontSize_spin.setValue(self.fontSize)
            font.setPointSize(self.fontSize)
            sub.setFont(font)
        except:
            pass
    def Smaller(self):
        try:
            if self.fontSize !=1:
                sub = self.mdiArea.activeSubWindow().widget()
                font = sub.currentFont()
                self.fontSize -=1
                self.FontSize_spin.setValue(self.fontSize)
                font.setPointSize(self.fontSize)
                sub.setFont(font)
                self.timer.start(100)
        except:
            pass
    def fileHorizontal(self):
        try:
            self.mdiArea.tileSubWindows()
        except:
            pass
    def fileVertical(self):
        try:
            wList = self.mdiArea.subWindowList()
            size = len(wList)
            if size > 0:
                total_width = self.mdiArea.width()
                total_height = self.mdiArea.height()
                window_height = total_height // size
                for i, w in enumerate(wList):
                    rect = QtCore.QRect(0, i * window_height, total_width, window_height)
                    w.setGeometry(rect)
        except:
            pass
    def fileChangeFont(self, font):
        try:
            self.mdiArea.activeSubWindow().widget().setCurrentFont(font)
        except:
            pass

    def fileSearch(self):
        try:
            pattern, okPressed = QtWidgets.QInputDialog.getText(self,
                                                                "查找", "查找字符串:", QtWidgets.QLineEdit.Normal, "")
            if okPressed and pattern != '':
                sub = self.mdiArea.activeSubWindow().widget()
                sub.moveCursor(QTextCursor.StartOfLine, QTextCursor.MoveAnchor)
                if sub.find(pattern):
                    palette = sub.palette()
                    palette.setColor(QPalette.Highlight, palette.color(QPalette.Active, QPalette.Highlight))
                    sub.setPalette(palette)
        except:
            pass
    def fileBold(self):
        try:
            sub = self.mdiArea.activeSubWindow().widget()
            tmpFormat = sub.currentCharFormat()
            if tmpFormat.fontWeight() == QtGui.QFont.Bold:
                tmpFormat.setFontWeight(QtGui.QFont.Normal)
            else:
                tmpFormat.setFontWeight(QtGui.QFont.Bold)
            sub.mergeCurrentCharFormat(tmpFormat)
        except:
            pass

    def fileItalic(self):
        try:
            tmpTextBox = self.mdiArea.activeSubWindow().widget()
            tmpTextBox.setFontItalic(not tmpTextBox.fontItalic())
        except:
            pass
    def fileUnderline(self):
        try:
            tmpTextBox = self.mdiArea.activeSubWindow().widget()
            tmpTextBox.setFontUnderline(not tmpTextBox.fontUnderline())
        except:
            pass

    def fileCopy(self):
        try:
            self.mdiArea.activeSubWindow().widget().copy()
        except:
            pass

    def fileCut(self):
        try:
            self.mdiArea.activeSubWindow().widget().cut()
        except:
            pass

    def filePaste(self):
        try:
            self.mdiArea.activeSubWindow().widget().paste()
        except:
            pass

    def fileRedo(self):
        try:
            self.mdiArea.activeSubWindow().widget().redo()
        except:
            pass

    def fileUndo(self):
        try:
            self.mdiArea.activeSubWindow().widget().undo()
        except:
            pass

    def filePile(self):
        try:
            if len(self.mdiArea.subWindowList()) > 1:
                self.mdiArea.cascadeSubWindows()
        except:
            pass

    def fileSave(self):
        try:
            tmpTextEdit = self.mdiArea.activeSubWindow()
            tmpTextEdit = tmpTextEdit.widget()
            if tmpTextEdit is None or not isinstance(tmpTextEdit, QTextEdit):
                return True
            tmpTextEdit.save()
        except:
            pass

    def fileOpen(self):
        try:
            filename, filetype = QFileDialog.getOpenFileName(self, "打开文件", "C:",
                                                             "Text files (*.txt)")
            if filename:
                for window in self.mdiArea.subWindowList():
                    textEdit = window.widget()
                    if textEdit.filename == filename:
                        self.mdiArea.setActiveSubWindow(window)
                        break
                else:
                    self.loadFile(filename)
        except:
            pass

    def fileNew(self):
        try:
            tmpTextEdit = textedit.TextEdit()
            self.mdiArea.addSubWindow(tmpTextEdit)
            tmpTextEdit.show()
        except:
            pass

    def loadFile(self, filename):
        try:
            tmpTextEdit = textedit.TextEdit(filename)
            tmpTextEdit.load()
            self.mdiArea.addSubWindow(tmpTextEdit)
            tmpTextEdit.show()
        except:
            pass
    def closeEvent(self, event):
        try:
            unSaveFile = 0
            for window in self.mdiArea.subWindowList():
                textEdit = window.widget()
                if textEdit.isModified():
                    unSaveFile += 1
            if unSaveFile != 0:
                dlg = QMessageBox.warning(self, "NoteEdit", f"{unSaveFile}个文档尚未保存，是否关闭？",
                                          QMessageBox.Yes | QMessageBox.No)
                if dlg == QMessageBox.Yes:
                    QtCore.QCoreApplication.quit()
                elif dlg == QMessageBox.No:
                    event.ignore()
        except:
            pass
