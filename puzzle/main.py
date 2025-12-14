from PyQt5.QtWidgets import  *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from Show_code import *
def countImg():
    floaderPath = 'image/'
    files = os.listdir(floaderPath)
    num = len(files)
    return num

if __name__ == "__main__":
    app = QApplication([])
    num = countImg()
    ran = random.randint(1, num)
    path = f"image/图片{ran}.jpg"
    puzzle = ShowCode(path)
    puzzle.dialog.windowFlags()
    puzzle.dialog.show()
    sys.exit(app.exec())
