from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import base64


class ChangePassword_Window:
    def __init__(self, app):
        self.key = 5
        self.app = app
        file = open("password.txt", "a")
        file.close()
        
        with open("password.txt", "rb") as file:
            data = file.readline()
        for i in range(self.key):
            data = base64.b64decode(data)
        data = data.decode()
        
        if not data:
            password = "1234".encode()
            for i in range(self.key):
                password = base64.b64encode(password)
            with open("password.txt", "wb") as file:
                file.write(password)
    
        self.set_window()


    def set_window(self):
        self.change_password_window = QtWidgets.QDialog()

    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.change_password_window
        
        Window.setObjectName("Window")
        Window.resize(400, 300)
        Window.setStyleSheet("background-color: rgb(30, 75, 135);")
        self.OldPassword = QtWidgets.QLineEdit(Window)
        self.OldPassword.setGeometry(QtCore.QRect(80, 50, 150, 40))
        self.OldPassword.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.OldPassword.setEchoMode(QtWidgets.QLineEdit.Password)
        self.OldPassword.setObjectName("OldPassword")
        self.OldPassword.setFont(self.font)

        self.Button = QtWidgets.QPushButton(Window)
        self.Button.setGeometry(QtCore.QRect(110, 210, 90, 30))
        self.Button.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(35, 170, 10);")
        self.Button.setObjectName("Button")
        self.Button.setFont(self.font)
        self.Cancel = QtWidgets.QPushButton(Window)
        self.Cancel.setGeometry(QtCore.QRect(240, 210, 90, 30))
        self.Cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(205, 0, 0);")
        self.Cancel.setObjectName("Cancel")
        self.Cancel.setFont(self.font)
        
        self.Text = QtWidgets.QTextBrowser(Window)
        self.Text.setGeometry(QtCore.QRect(240, 50, 150, 40))
        self.Text.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(30, 75, 135);\n"
                                "border: none;")
        self.Text.setObjectName("Text")
        self.Text.setFont(self.font)

        self.NewPassword1 = QtWidgets.QLineEdit(Window)
        self.NewPassword1.setGeometry(QtCore.QRect(80, 100, 150, 40))
        self.NewPassword1.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NewPassword1.setText("")
        self.NewPassword1.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassword1.setObjectName("NewPassword1")
        self.NewPassword1.setFont(self.font)
        self.NewPassword2 = QtWidgets.QLineEdit(Window)
        self.NewPassword2.setGeometry(QtCore.QRect(80, 150, 150, 40))
        self.NewPassword2.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.NewPassword2.setText("")
        self.NewPassword2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.NewPassword2.setObjectName("NewPassword2")
        self.NewPassword2.setFont(self.font)

        self.Text_2 = QtWidgets.QTextBrowser(Window)
        self.Text_2.setGeometry(QtCore.QRect(240, 100, 150, 40))
        self.Text_2.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(30, 75, 135);\n"
                                "border: none;")
        self.Text_2.setObjectName("Text_2")
        self.Text_2.setFont(self.font)
        self.Text_3 = QtWidgets.QTextBrowser(Window)
        self.Text_3.setGeometry(QtCore.QRect(240, 150, 150, 40))
        self.Text_3.setStyleSheet("background-color: rgb(255, 255, 255);\n"
                                "color: rgb(255, 255, 255);\n"
                                "background-color: rgb(30, 75, 135);\n"
                                "border: none;")
        self.Text_3.setObjectName("Text_3")
        self.Text_3.setFont(self.font)

        self.OldPassword.raise_()
        self.Button.raise_()
        self.Text.raise_()
        self.NewPassword1.raise_()
        self.Text_2.raise_()
        self.Text_3.raise_()
        self.NewPassword2.raise_()

        self.retranslateUi(Window)
        self.Button.clicked.connect(self.change_password)
        self.Cancel.clicked.connect(self.cancel)
        QtCore.QMetaObject.connectSlotsByName(Window)


    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "برنامه دفترچه تلفن"))
        self.Button.setText(_translate("Window", "تغییر"))
        self.Cancel.setText(_translate("Window", "انصراف"))
        self.Text.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">رمز عبور قبلی : </p></body></html>"))
        self.Text_2.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">رمز عبور جدید : </p></body></html>"))
        self.Text_3.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">تکرار رمز عبور جدید : </p></body></html>"))


    def change_password(self):
        if self.OldPassword.text() and self.NewPassword1.text() and self.NewPassword2.text():            
            with open("password.txt", "rb") as file:
                data = file.readline()
            for i in range(self.key):
                data = base64.b64decode(data)
            data = data.decode()
            
            if self.OldPassword.text() == data:
                if self.NewPassword1.text() == self.NewPassword2.text():
                    data = self.NewPassword1.text().encode()
                    for i in range(self.key):
                        data = base64.b64encode(data)
                    with open("password.txt", "wb") as file:
                        file.write(data)

                    self.app.processEvents()
                    self.app.closeAllWindows()

                    self.login_ui.login_window.deleteLater()
                    self.login_ui.__init__(self.app)
                    self.login_ui.setupUi(**self.kwargs)
                    self.login_ui.login_window.show()


    def cancel(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.login_ui.login_window.deleteLater()
        self.login_ui.__init__(self.app)
        self.login_ui.setupUi(**self.kwargs)
        self.login_ui.login_window.show()

