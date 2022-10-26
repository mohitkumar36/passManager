import hashlib
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QDialogButtonBox, QDialog, QMainWindow, QVBoxLayout, QLabel
from PyQt5.QtCore import QCoreApplication, pyqtSlot

from dbconfig import dbconfig
from mainUI import Ui_MainPage


class Ui_Login(object):
    def openMain(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_MainPage()
        self.ui.setupUi(self.window)
        self.window.show()


    def setupUi(self, Login):
        Login.setObjectName("Login")
        Login.resize(306, 117)
        self.centralwidget = QtWidgets.QWidget(Login)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 31))
        self.label.setObjectName("label")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.passwordText.setGeometry(QtCore.QRect(120, 30, 161, 21))
        self.passwordText.setObjectName("passwordText")
        self.loginButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.on_click())
        self.loginButton.setGeometry(QtCore.QRect(110, 70, 75, 24))
        self.loginButton.setObjectName("loginButton")
        Login.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(Login)
        self.statusbar.setObjectName("statusbar")
        Login.setStatusBar(self.statusbar)

        self.retranslateUi(Login)
        QtCore.QMetaObject.connectSlotsByName(Login)

    def validateMasterPassword(self, masterPass):
      mp = masterPass

      hashed_mp = hashlib.sha256(mp.encode()).hexdigest()
      db = dbconfig()
      cursor = db.cursor()
      query = "SELECT * FROM pm.secrets"
      cursor.execute(query)
      result = cursor.fetchall()[0] # type: ignore
      if hashed_mp != result[0]:
         return False

      return [mp,result[1]]

    def on_click(self):
        masterPass = self.passwordText.text()
        if self.validateMasterPassword(masterPass):
            self.openMain()
        else:
            dlg = CustomDialog()
            dlg.exec()


    def retranslateUi(self, Login):
        _translate = QtCore.QCoreApplication.translate
        Login.setWindowTitle(_translate("Login", "WelcomeBack"))
        self.label.setText(_translate("Login", "Enter Password: "))
        self.loginButton.setText(_translate("Login", "Login"))

class CustomDialog(QDialog):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("ERROR")

        QBtn = QDialogButtonBox.Ok

        self.buttonBox = QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        

        self.layout = QVBoxLayout()
        message = QLabel("Wrong Password !!!")
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Login = QtWidgets.QMainWindow()
    ui = Ui_Login()
    ui.setupUi(Login)
    Login.show()
    sys.exit(app.exec_())
