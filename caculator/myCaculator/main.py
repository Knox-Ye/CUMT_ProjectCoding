import sys
import Caculator1
from PyQt5.QtWidgets import *
from PyQt5.QtGui import QIcon
import readInput
if __name__ == '__main__':
    app = QApplication(sys.argv)
    rIp = readInput.readInput()
    app.setWindowIcon(QIcon('CaculatorImage.png'))
    rIp.dialog.show()
    sys.exit(app.exec_())
