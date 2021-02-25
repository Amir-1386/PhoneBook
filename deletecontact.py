from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
import base64


class DeleteContact_Window:
    def __init__(self, app, ls, index):
        self.key = 5
        self.app = app
        self.ls = ls
        self.index = index
        self.basedir = os.path.join(".", "photos")
        file = open("data.txt", "a")
        file.close()
    
        self.set_window()


    def set_window(self):
        self.deletecontact_window = QtWidgets.QDialog()

    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.deletecontact_window
        
        Window.setObjectName("Window")
        Window.resize(400, 160)
        Window.setStyleSheet("background-color: rgb(30, 75, 135);")
        
        self.Text = QtWidgets.QTextBrowser(Window)
        self.Text.setGeometry(QtCore.QRect(40, 30, 310, 60))
        self.Text.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "border: none;")
        self.Text.setObjectName("Text")
        self.Text.setFont(self.font)
        
        self.no = QtWidgets.QPushButton(Window)
        self.no.setGeometry(QtCore.QRect(260, 110, 90, 25))
        self.no.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(205, 0, 0);")
        self.no.setObjectName("no")
        self.no.setFont(self.font)
        self.yes = QtWidgets.QPushButton(Window)
        self.yes.setGeometry(QtCore.QRect(40, 110, 90, 25))
        self.yes.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(35, 170, 10);")
        self.yes.setObjectName("yes")
        self.yes.setFont(self.font)

        self.yes.clicked.connect(self.delete_contact)
        self.no.clicked.connect(self.cancel_deleting)

        self.retranslateUi(Window)
        QtCore.QMetaObject.connectSlotsByName(Window)
    

    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "برنامه دفترچه تلفن"))
        self.Text.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">آیا از حذف مخاطب «" + self.ls[0] + "» اطمینان دارید؟</p></body></html>"))
        self.no.setText(_translate("Window", "خیر"))
        self.yes.setText(_translate("Window", "بله"))


    def delete_contact(self):
        self.contact_ls = []
        
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

        self.contact_ls.pop(self.index)

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

        if os.path.isfile(self.ls[3]) and self.ls[3] != os.path.join(self.basedir, "default.png"):
            os.remove(self.ls[3])

        self.app.processEvents()
        self.app.closeAllWindows()

        self.app_ui.app_window.deleteLater()
        self.app_ui.__init__(self.app)
        self.app_ui.setupUi(**self.kwargs)
        self.app_ui.app_window.show()


    def cancel_deleting(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.showcontact_ui.showcontact_window.deleteLater()
        self.showcontact_ui.__init__(self.app, self.ls, self.index)
        self.showcontact_ui.setupUi(**self.kwargs)
        self.showcontact_ui.showcontact_window.show()

