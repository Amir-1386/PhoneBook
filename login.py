from PyQt5 import QtCore, QtGui, QtWidgets
import sys
import base64


class Login_Window:
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
        self.login_window = QtWidgets.QDialog()
    
    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.login_window
        
        Window.setObjectName("Window")
        Window.resize(400, 300)
        Window.setStyleSheet("background-color: rgb(30, 75, 135);")
        self.Password = QtWidgets.QLineEdit(Window)
        self.Password.setGeometry(QtCore.QRect(120, 120, 150, 40))
        self.Password.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Password.setEchoMode(QtWidgets.QLineEdit.Password)
        self.Password.setObjectName("Password")
        self.Password.setFont(self.font)
        self.LoginButton = QtWidgets.QPushButton(Window)
        self.LoginButton.setGeometry(QtCore.QRect(150, 200, 90, 30))
        self.LoginButton.setStyleSheet("color: rgb(255, 255, 255);\n"
                                        "background-color: rgb(35, 170, 10);")
        self.LoginButton.setObjectName("LoginButton")
        self.LoginButton.setFont(self.font)
        self.Text = QtWidgets.QTextBrowser(Window)
        self.Text.setGeometry(QtCore.QRect(60, 60, 270, 60))
        self.Text.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(30, 75, 135);"
                                "border: none;")
        self.Text.setObjectName("Text")
        self.Text.setFont(self.font)
        self.ChangePassword = QtWidgets.QPushButton(Window)
        self.ChangePassword.setGeometry(QtCore.QRect(150, 240, 90, 25))
        self.ChangePassword.setStyleSheet("color: rgb(255, 255, 255);\n"
                                            "border: none;")
        self.ChangePassword.setObjectName("ChangePassword")
        self.ChangePassword.setFont(self.font)

        self.retranslateUi(Window)
        self.LoginButton.clicked.connect(self.check_password)
        self.ChangePassword.clicked.connect(self.change_password)
        QtCore.QMetaObject.connectSlotsByName(Window)


    def retranslateUi(self, Window):
        _translate = QtCore.QCoreApplication.translate
        Window.setWindowTitle(_translate("Window", "برنامه دفترچه تلفن"))
        self.LoginButton.setText(_translate("Window", "ورود"))
        self.Text.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">لطفا رمز عبور خود را وارد کنید.</p></body></html>"))
        self.ChangePassword.setText(_translate("Window", "تغییر گذرواژه"))


    def check_password(self):
        with open("password.txt", "rb") as file:
            data = file.readline()
        for i in range(self.key):
            data = base64.b64decode(data)
        data = data.decode()
        
        if self.Password.text() == data:
            self.app.processEvents()
            self.app.closeAllWindows()

            self.app_ui.app_window.deleteLater()
            self.app_ui.__init__(self.app)
            self.app_ui.setupUi(**self.kwargs)
            self.app_ui.app_window.show()


    def change_password(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.change_password_ui.change_password_window.deleteLater()
        self.change_password_ui.__init__(self.app)
        self.change_password_ui.setupUi(**self.kwargs)
        self.change_password_ui.change_password_window.show()

