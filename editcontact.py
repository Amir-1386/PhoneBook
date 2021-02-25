from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
from random import choice
import base64
import re
from choose_picture import App
from convert_image import convert


class EditContact_Window:
    def __init__(self, app, ls, index):
        self.key = 5
        self.app = app
        self.ls = ls
        self.index = index
        self.basedir = os.path.join(".", "photos")
        self.file = None
        self.regex = "(^[a-zA-Z0-9.-]+@[a-z-]+\.[a-z]{2,3}$)"
        file = open("data.txt", "a")
        file.close()
    
        self.set_window()


    def set_window(self):
        self.editcontact_window = QtWidgets.QDialog()
    
    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.editcontact_window
        
        Window.setObjectName("Window")
        Window.resize(510, 600)
        Window.setStyleSheet("background-color: rgb(30, 75, 135);")

        self.Name_title = QtWidgets.QTextBrowser(Window)
        self.Name_title.setGeometry(QtCore.QRect(250, 10, 255, 85))
        self.Name_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Name_title.setObjectName("Name_title")
        self.Name_title.setFont(self.font)
        self.Name_input = QtWidgets.QLineEdit(Window)
        self.Name_input.setGeometry(QtCore.QRect(30, 20, 190, 35))
        self.Name_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Name_input.setObjectName("Name_input")
        self.Name_input.setText(self.ls[0])
        self.Name_input.setFont(self.font)
        
        self.Number_title = QtWidgets.QTextBrowser(Window)
        self.Number_title.setGeometry(QtCore.QRect(240, 160, 265, 85))
        self.Number_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Number_title.setObjectName("Number_title")
        self.Number_title.setFont(self.font)
        self.Number_input = QtWidgets.QTextEdit(Window)
        self.Number_input.setGeometry(QtCore.QRect(20, 160, 220, 160))
        self.Number_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Number_input.setObjectName("Number_input")
        self.Number_input.setText("\n".join(self.ls[1]))
        self.Number_input.setFont(self.font)

        self.Email_title = QtWidgets.QTextBrowser(Window)
        self.Email_title.setGeometry(QtCore.QRect(240, 350, 265, 85))
        self.Email_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Email_title.setObjectName("Email_title")
        self.Email_title.setFont(self.font)
        self.Email_input = QtWidgets.QTextEdit(Window)
        self.Email_input.setGeometry(QtCore.QRect(20, 350, 220, 160))
        self.Email_input.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Email_input.setObjectName("Email_input")
        self.Email_input.setText("\n".join(self.ls[2]))
        self.Email_input.setFont(self.font)

        self.Photo_title = QtWidgets.QTextBrowser(Window)
        self.Photo_title.setGeometry(QtCore.QRect(210, 100, 300, 35))
        self.Photo_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Photo_title.setObjectName("Photo_title")
        self.Photo_title.setFont(self.font)
        self.Photo_input = QtWidgets.QPushButton(Window)
        self.Photo_input.setGeometry(QtCore.QRect(70, 100, 100, 25))
        self.Photo_input.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                        "color: rgb(0, 0, 0);")
        self.Photo_input.setObjectName("Photo_input")
        self.Photo_input.setFont(self.font)

        self.save = QtWidgets.QPushButton(Window)
        self.save.setGeometry(QtCore.QRect(50, 550, 90, 25))
        self.save.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(35, 170, 10);")
        self.save.setObjectName("save")
        self.save.setFont(self.font)
        self.cancel = QtWidgets.QPushButton(Window)
        self.cancel.setGeometry(QtCore.QRect(370, 550, 90, 25))
        self.cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(205, 0, 0);")
        self.cancel.setObjectName("cancel")
        self.cancel.setFont(self.font)
        
        self.retranslateUi(Window)
        self.Photo_input.clicked.connect(self.choose_picture)
        self.save.clicked.connect(self.save_contact)
        self.cancel.clicked.connect(self.cancel_addingcontact)
        QtCore.QMetaObject.connectSlotsByName(Window)


    def retranslateUi(self, Window):
        self._translate = _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "برنامه دفترچه تلفن"))
        self.Name_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">نام و نام خانوادگی : </p></body></html>"))
        self.Number_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">شماره : </p>\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(اگر می‌خواهید چند شماره وارد کنید هر شماره را در یک خط وارد کنید.)</p></body></html>"))
        self.Email_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ایمیل : </p>\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">(اگر می‌خواهید چند ایمیل وارد کنید هر ایمیل را در یک خط وارد کنید.)</p></body></html>"))
        self.Photo_input.setText(_translate("Window", "انتخاب تصویر"))
        self.Photo_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">عکس : " + os.path.basename(self.ls[3]) + "</p></body></html>"))
        self.save.setText(_translate("Window", "ذخیره"))
        self.cancel.setText(_translate("Window", "بازگشت"))


    def choose_picture(self):
        app = App()
        self.file = app.openFileNameDialog()
        if self.file:
            self.Photo_title.setHtml(self._translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">عکس : " + os.path.basename(self.file) + "</p></body></html>"))


    def save_contact(self):
        if self.Name_input.text():
            self.contact_ls = []
            my_ls = []
            
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
                        self.contact_ls.append(nls)
                        nls = []
                    i += 1
            
            my_ls.append(self.Name_input.text())

            nls = []
            items = self.Number_input.toPlainText().split("\n")
            for item in items:
                if item.isdigit():
                    nls.append(item)
            my_ls.append(sorted(set(nls)))

            nls = []
            items = self.Email_input.toPlainText().split("\n")
            for item in items:
                if re.match(self.regex, item):
                    nls.append(item)
            my_ls.append(sorted(set(nls)))

            if self.file and self.file != self.ls[3] and os.path.isfile(self.file):
                if self.ls[3] != os.path.join(self.basedir, "default.png"):
                    os.remove(self.ls[3])
                name, extension = os.path.splitext(os.path.basename(self.file))
                name += ".png"
                address = os.path.join(self.basedir, name)
                while os.path.isfile(address):
                    name = choice("abcdefghijklmnopqrstuvwxyz") + name
                    address = os.path.join(self.basedir, name)
                convert(self.file, address)

            else:
                address = self.ls[3]

            my_ls.append(address)

            self.ls = my_ls[:]
            self.contact_ls[self.index] = self.ls[:]
            self.contact_ls.sort()

            with open("data.txt", "wb") as file:
                for data in self.contact_ls:
                    i = 0
                    for j in data:
                        if i % 4 == 0 or i % 4 == 3:
                            item = j.encode()
                            for r in range(self.key):
                                item = base64.b64encode(item)
                            file.write(item)
                        elif i % 4 == 1 or i % 4 == 2:
                            nls = []
                            for k in j:
                                item = k.encode()
                                for r in range(self.key):
                                    item = base64.b64encode(item)
                                item = item.decode()
                                nls.append(item)
                            file.write(" ".join(nls).encode())
                        file.write(b"\n")
                        i += 1
                    file.write(b"\n")

            self.app.processEvents()
            self.app.closeAllWindows()

            self.showcontact_ui.showcontact_window.deleteLater()
            self.showcontact_ui.__init__(self.app, self.ls, self.index)
            self.showcontact_ui.setupUi(**self.kwargs)
            self.showcontact_ui.showcontact_window.show()


    def cancel_addingcontact(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.showcontact_ui.showcontact_window.deleteLater()
        self.showcontact_ui.__init__(self.app, self.ls, self.index)
        self.showcontact_ui.setupUi(**self.kwargs)
        self.showcontact_ui.showcontact_window.show()

