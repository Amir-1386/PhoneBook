from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys


class ShowContact_Window:
    def __init__(self, app, ls, index):
        self.key = 5
        self.app = app
        self.ls = ls
        self.index = index
    
        self.set_window()


    def set_window(self):
        self.showcontact_window = QtWidgets.QDialog()
    
    
    def setupUi(self, **kwargs):
        self.kwargs = kwargs
        for key, value in kwargs.items():
            setattr(self, key, value)
        
        self.window = Window = self.showcontact_window
        
        Window.setObjectName("Window")
        Window.resize(510, 600)
        Window.setStyleSheet("background-color: rgb(30, 75, 135);")

        self.Name_title = QtWidgets.QTextBrowser(Window)
        self.Name_title.setGeometry(QtCore.QRect(250, 10, 255, 75))
        self.Name_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Name_title.setObjectName("Name_title")
        self.Name_title.setFont(self.font)
        self.Name = QtWidgets.QTextBrowser(Window)
        self.Name.setGeometry(QtCore.QRect(30, 20, 190, 35))
        self.Name.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Name.setObjectName("Name")
        self.Name.setFont(self.font)
        
        self.Number_title = QtWidgets.QTextBrowser(Window)
        self.Number_title.setGeometry(QtCore.QRect(240, 160, 265, 75))
        self.Number_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Number_title.setObjectName("Number_title")
        self.Number_title.setFont(self.font)
        self.Number = QtWidgets.QTextBrowser(Window)
        self.Number.setGeometry(QtCore.QRect(20, 160, 220, 160))
        self.Number.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Number.setObjectName("Number")
        self.Number.setFont(self.font)

        self.Email_title = QtWidgets.QTextBrowser(Window)
        self.Email_title.setGeometry(QtCore.QRect(240, 350, 265, 75))
        self.Email_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Email_title.setObjectName("Email_title")
        self.Email_title.setFont(self.font)
        self.Email = QtWidgets.QTextBrowser(Window)
        self.Email.setGeometry(QtCore.QRect(20, 350, 220, 160))
        self.Email.setStyleSheet("background-color: rgb(255, 255, 255);")
        self.Email.setObjectName("Email")
        self.Email.setFont(self.font)

        self.Photo_title = QtWidgets.QTextBrowser(Window)
        self.Photo_title.setGeometry(QtCore.QRect(210, 100, 300, 35))
        self.Photo_title.setStyleSheet("border: none;\n"
                                        "color: rgb(255, 255, 255);")
        self.Photo_title.setObjectName("Photo_title")
        self.Photo_title.setFont(self.font)
        self.Photo = QtWidgets.QTextBrowser(Window)
        self.Photo.setGeometry(QtCore.QRect(90, 60, 85, 85))
        self.Photo.setStyleSheet("border: none;\n"
                                "color: rgb(0, 0, 0);")
        self.Photo.setObjectName("Photo")
        self.Photo.setFont(self.font)

        self.delete = QtWidgets.QPushButton(Window)
        self.delete.setGeometry(QtCore.QRect(230, 550, 50, 25))
        self.delete.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(0, 0, 0);")
        self.delete.setObjectName("delete")
        self.delete.setFont(self.font)
        self.edit = QtWidgets.QPushButton(Window)
        self.edit.setGeometry(QtCore.QRect(50, 550, 90, 25))
        self.edit.setStyleSheet("color: rgb(255, 255, 255);\n"
                                "background-color: rgb(35, 170, 10);")
        self.edit.setObjectName("edit")
        self.edit.setFont(self.font)
        self.cancel = QtWidgets.QPushButton(Window)
        self.cancel.setGeometry(QtCore.QRect(370, 550, 90, 25))
        self.cancel.setStyleSheet("color: rgb(255, 255, 255);\n"
                                    "background-color: rgb(205, 0, 0);")
        self.cancel.setObjectName("cancel")
        self.cancel.setFont(self.font)
        
        self.retranslateUi(Window)
        self.delete.clicked.connect(self.delete_contact)
        self.edit.clicked.connect(self.edit_contact)
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
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">شماره : </p></body></html>"))
        self.Email_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">ایمیل : </p></body></html>"))
        self.Photo_title.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                        "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                        "p, li { white-space: pre-wrap; }\n"
                                                        "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                        "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">عکس : " + os.path.basename(self.ls[3]) + "</p></body></html>"))


        self.Name.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + self.ls[0] + "</p></body></html>"))
        self.Number.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + "<br/>".join(self.ls[1]) + "</p></body></html>"))
        self.Email.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">" + "<br/>".join(self.ls[2]) + "</p></body></html>"))

        self.Photo.setHtml(_translate("Window", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                    "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                    "p, li { white-space: pre-wrap; }\n"
                                                    "</style></head><body style=\" font-size:11pt; font-weight:400; font-style:normal;\">\n"
                                                    "<p align=\"center\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                    "<p align=\"center\" dir=\'rtl\' style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><img src=\"" + self.ls[3] + "\" height=\"50\" /></p></body></html>"))

        
        self.delete.setText(_translate("Window", "حذف"))
        self.edit.setText(_translate("Window", "ویرایش"))
        self.cancel.setText(_translate("Window", "بازگشت"))


    def delete_contact(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.deletecontact_ui.deletecontact_window.deleteLater()
        self.deletecontact_ui.__init__(self.app, self.ls, self.index)
        self.deletecontact_ui.setupUi(**self.kwargs)
        self.deletecontact_ui.deletecontact_window.show()


    def edit_contact(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.editcontact_ui.editcontact_window.deleteLater()
        self.editcontact_ui.__init__(self.app, self.ls, self.index)
        self.editcontact_ui.setupUi(**self.kwargs)
        self.editcontact_ui.editcontact_window.show()


    def cancel_addingcontact(self):
        self.app.processEvents()
        self.app.closeAllWindows()

        self.app_ui.app_window.deleteLater()
        self.app_ui.__init__(self.app)
        self.app_ui.setupUi(**self.kwargs)
        self.app_ui.app_window.show()

