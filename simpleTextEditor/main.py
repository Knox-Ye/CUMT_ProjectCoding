from editor import *
from PyQt5 import QtCore, QtGui, QtWidgets

if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    ex = Editor()
    ex.show()
    app.exec_()
    