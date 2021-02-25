import sys
from PyQt5.QtWidgets import QApplication, QWidget, QInputDialog, QLineEdit, QFileDialog
from PyQt5.QtGui import QIcon


class App(QWidget):
    def __init__(self):
        super().__init__()
        self.title = 'برنامه دفترچه تلفن'
        self.left = 10
        self.top = 10
        self.width = 640
        self.height = 480
        self.initUI()

    
    def initUI(self):
        self.setWindowTitle(self.title)
        self.setGeometry(self.left, self.top, self.width, self.height)

    
    def openFileNameDialog(self):
        options = QFileDialog.Options()
        options |= QFileDialog.DontUseNativeDialog
        fileName, _ = QFileDialog.getOpenFileName(self, "انتخاب تصویر", "","Picture Files (*.png *.jpg *.jpeg *.bmp *.svg)", options=options)
        if fileName:
            return fileName

