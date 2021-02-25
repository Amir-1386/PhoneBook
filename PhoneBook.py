from PyQt5 import QtCore, QtGui, QtWidgets
import os, sys
import base64
from login import Login_Window
from change_password import ChangePassword_Window
from app import App_Window
from addcontact import AddContact_Window
from showcontact import ShowContact_Window
from editcontact import EditContact_Window
from deletecontact import DeleteContact_Window


app = QtWidgets.QApplication(sys.argv)

login_ui = Login_Window(app)
change_password_ui = ChangePassword_Window(app)
app_ui = App_Window(app)
addcontact_ui = AddContact_Window(app)
showcontact_ui = ShowContact_Window(app, ['', [], [], ''], 0)
editcontact_ui = EditContact_Window(app, ['', [], [], ''], 0)
deletecontact_ui = DeleteContact_Window(app, ['', [], [], ''], 0)

font_id = QtGui.QFontDatabase.addApplicationFont(os.path.join(".", "fonts", "Vazir.ttf"))
font = QtGui.QFont("Vazir")

kwargs = {
    "login_ui" : login_ui,
    "change_password_ui" : change_password_ui,
    "app_ui" : app_ui,
    "addcontact_ui" : addcontact_ui,
    "showcontact_ui" : showcontact_ui,
    "editcontact_ui" : editcontact_ui,
    "deletecontact_ui" : deletecontact_ui,
    "font" : font,
}

login_ui.setupUi(**kwargs)
change_password_ui.setupUi(**kwargs)
app_ui.setupUi(**kwargs)
addcontact_ui.setupUi(**kwargs)
showcontact_ui.setupUi(**kwargs)
editcontact_ui.setupUi(**kwargs)
deletecontact_ui.setupUi(**kwargs)

login_ui.login_window.show()

sys.exit(app.exec_())
