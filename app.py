from PyQt5 import QtCore, QtGui, QtWidgets
from functools import partial
import sys
import base64


class App_Window:
    def __init__(self, app):
        self.app = app
        self.key = 5
        self.ls = []

        file = open("data.txt", "a")
        file.close()
        
        with open("data.txt", "rb") as file:
            i = 0
            nls = []
            for item in file:
                if i % 5 == 0 or i % 5 == 3:
                    data = item[:-1]
                    for j in range(self.key):
                        data = base64.b64decode(data)
                    data = data.decode()
                elif i % 5 == 1 or i % 5 == 2:
                    data = item[:-1].split()
                    for j in range(len(data)):
                        for k in range(self.key):
                            data[j] = base64.b64decode(data[j])
                        data[j] = data[j].decode()
                
                if i % 5 == 0:
                    nls.append(data)
                elif i % 5 == 1:
                    nls.append(data)
                elif i % 5 == 2:
                    nls.append(data)
                elif i % 5 == 3:
                    nls.append(data)
                elif i % 5 == 4:
                    self.ls.append(nls)
                    nls = []
                i += 1
        
        self.n = len(self.ls)
        self.Name = []
        self.Photo = []

        self.set_window()


    def set_window(self):
        self.app_window = QtWidgets.QDialog()

    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.app_window
        
        Window.setObjectName("Window")
        Window.resize(585, 585)
        Window.setStyleSheet("background-color: rgb(35, 75, 135);")
        
        self.Button = QtWidgets.QPushButton(Window)
        self.Button.setGeometry(QtCore.QRect(30, 30, 90, 30))
        self.Button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(35, 170, 10);")
        self.Button.setObjectName("Button")
        self.Button.setFont(self.font)
        
        self.scrollArea = QtWidgets.QScrollArea(Window)
        self.scrollArea.setGeometry(QtCore.QRect(170, 10, 370, (75 * self.n + 20) if (75 * self.n + 20) <= 545 else 545))
        self.scrollArea.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.scrollArea.setWidgetResizable(True)
        self.scrollArea.setObjectName("scrollArea")
        self.scrollAreaWidgetContents = QtWidgets.QWidget()
        self.scrollAreaWidgetContents.setGeometry(QtCore.QRect(0, 0, 370, 170))
        self.scrollAreaWidgetContents.setObjectName("scrollAreaWidgetContents")
        self.gridLayout = QtWidgets.QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout.setObjectName("gridLayout")

        for i in range(self.n):
            self.Photo.append(QtWidgets.QTextBrowser(self.scrollAreaWidgetContents))
            self.Photo[i].setStyleSheet("border: none;\n"
                                    "max-height: 75px;")
            self.Photo[i].setObjectName("Photo{}".format(i + 1))
            self.Photo[i].setFont(self.font)
            self.gridLayout.addWidget(self.Photo[i], i, 1, 1, 1)
            
            self.Name.append(QtWidgets.QPushButton(self.scrollAreaWidgetContents))
            
            self.Name[i].setStyleSheet("border: none;\n"
                                    "color: rgb(0, 0, 0);\n"
                                    "background-color: rgb(255, 255, 255);\n"
                                    "min-width: 250px;\n"
                                    "max-height: 75px;")
            self.Name[i].setObjectName("Name{}".format(i + 1))
            self.Name[i].setFont(self.font)

            self.Name[i].clicked.connect(partial(self.show_contact, self.ls[i], i))
            
            self.gridLayout.addWidget(self.Name[i], i, 0, 1, 1)
        
        
        self.scrollArea.setWidget(self.scrollAreaWidgetContents)

        self.retranslateUi(Window)
        self.Button.clicked.connect(self.add_contact)
        QtCore.QMetaObject.connectSlotsByName(Window)
    

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "برنامه دفترچه تلفن"))
        self.Button.setText(_translate("Window", "اضافه کردن"))

        for i in range(self.n):
            self.Name[i].setText(_translate("Window", self.ls[i][0]))
            photo = self.ls[i][3]
            self.Photo[i].setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-size:5pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                    "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"" + photo + "\" height=\"45\" /></p></body></html>"))


    def show_contact(self, ls, index):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.showcontact_ui.showcontact_window.deleteLater()
        self.showcontact_ui.__init__(self.app, ls, index)
        self.showcontact_ui.setupUi(**self.kwargs)
        self.showcontact_ui.showcontact_window.show()


    def add_contact(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.addcontact_ui.addcontact_window.deleteLater()
        self.addcontact_ui.__init__(self.app)
        self.addcontact_ui.setupUi(**self.kwargs)
        self.addcontact_ui.addcontact_window.show()

