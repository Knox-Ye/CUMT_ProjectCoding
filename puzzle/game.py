
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *
import random
class game(QGraphicsView):

    def __init__(self, path, parent=None):
        super().__init__(parent)
        self.path = path
        self.originalHeight = self.height()
        self.originalWidth = self.width()
        self.scene = QGraphicsScene(self)
        self.setScene(self.scene)
        self.img = QPixmap(path)
        self.img_item = QGraphicsPixmapItem(self.img)
        self.scene.addItem(self.img_item)
        self.pix = None
        self.pix_selected = None
        self.challengeMode = False

    def recover(self,path):
        self.image_clear()
        self.path = path
        self.img = QPixmap(self.path)
        self.img_item = QGraphicsPixmapItem(self.img)
        self.block_h = None
        self.block_w = None
        self.scene.addItem(self.img_item)
        self.pix = None
        self.pix_selected = None
        scaled_img = self.img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_item.setPixmap(scaled_img)

    def imageCut(self, n):
        self.img = self.img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.scene.removeItem(self.img_item)
        self.ImgHeight = self.img.height()
        self.ImgWidth = self.img.width()
        self.n = n
        if n == 0:
            return
        self.block_h, self.block_w = self.ImgHeight // self.n, self.ImgWidth // self.n
        self.block_img = []
        for i in range(n):
            for j in range(n):
                x1, y1 = i * self.block_w, j * self.block_h
                rect = QRect(x1, y1, self.block_w, self.block_h)
                block_pic = self.img.copy(rect)
                self.block_img.append([block_pic, j, i])  # size of pic and the coordinate

    def random_draw_img(self):
        self.image_clear()
        random.shuffle(self.block_img)
        for i in range(len(self.block_img)):
            img = self.block_img[i][0]
            piece = QGraphicsPixmapItem(img)
            piece.setFlag(QGraphicsPixmapItem.ItemIsSelectable)
            x = i % self.n * self.block_w
            y = i // self.n * self.block_h
            piece.setPos(x, y)
            self.scene.addItem(piece)

    def image_clear(self):
        try:
            for i in range(self.n):
                for j in range(self.n):
                    x1, y1 = int(self.block_w/2 + i * self.block_w), int(self.block_h/2 + j * self.block_h)
                    ob = QPoint(x1, y1)
                    item = self.itemAt(ob)
                    self.scene.removeItem(item)
        except:
            x1, y1 = int(self.ImgWidth/2), int(self.ImgHeight/2)
            ob = QPoint(x1, y1)
            item = self.itemAt(ob)
            self.scene.removeItem(item)
    def gameOver(self):
        flag = True
        for i in range(self.n * self.n):
            if self.block_img[i][1] != i//self.n or self.block_img[i][2] != i%self.n:
                flag = False
        return flag
    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        scene_pos = event.pos()
        item = self.itemAt(scene_pos)
        if item:
            if not self.pix_selected:
                self.pix_selected = item
            else:
                if item != self.pix_selected:
                    pos1 = self.pix_selected.pos()
                    pos2 = item.pos()
                    self.pix_selected.setPos(pos2)
                    item.setPos(pos1)
                    x1, y1 = int(pos1.x()//self.block_w), int(pos1.y()//self.block_h)
                    x2, y2 = int(pos2.x()//self.block_w), int(pos2.y()//self.block_h)
                    self.block_img[x1 + y1*self.n], self.block_img[x2 + y2*self.n] = (
                        self.block_img[x2 + y2*self.n], self.block_img[x1 + y1*self.n]
                    )
                    if self.gameOver():
                        if not self.challengeMode:
                            QMessageBox.information(self, 'GOOD JOB!', '恭喜完成拼图')
                        self.pix_selected = None
                        return
                self.pix_selected = None

    def resizeEvent(self, event):
        super().resizeEvent(event)
        scaled_img = self.img.scaled(self.size(), Qt.KeepAspectRatio, Qt.SmoothTransformation)
        self.img_item.setPixmap(scaled_img)
        self.ImgHeight = scaled_img.height()
        self.ImgWidth = scaled_img.width()