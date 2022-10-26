from PyQt5 import QtCore, QtGui, QtWidgets
from add import addEntry, checkEntry
import hashlib

# from confirmUI import Ui_Confirm
from dbconfig import dbconfig


class Ui_EnterEntries(object):
    # def confirm(self):
    #     self.window = QtWidgets.QDialog()
    #     self.ui = Ui_Confirm()
    #     self.ui.setupUi(self.window)
    #     self.window.show()
    # window_closed = QtCore.pyqtSignal()

    def setupUi(self, EnterEntries):
        EnterEntries.setObjectName("EnterEntries")
        EnterEntries.resize(344, 259)
        self.centralwidget = QtWidgets.QWidget(EnterEntries)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 10, 61, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 40, 49, 16))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 70, 49, 16))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 100, 61, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 130, 61, 21))
        self.label_5.setObjectName("label_5")
        self.siteText = QtWidgets.QLineEdit(self.centralwidget)
        self.siteText.setGeometry(QtCore.QRect(90, 10, 241, 21))
        self.siteText.setObjectName("siteText")
        self.urlText = QtWidgets.QLineEdit(self.centralwidget)
        self.urlText.setGeometry(QtCore.QRect(60, 40, 271, 21))
        self.urlText.setObjectName("urlText")
        self.emailText = QtWidgets.QLineEdit(self.centralwidget)
        self.emailText.setGeometry(QtCore.QRect(70, 70, 261, 21))
        self.emailText.setObjectName("emailText")
        self.usernameText = QtWidgets.QLineEdit(self.centralwidget)
        self.usernameText.setGeometry(QtCore.QRect(90, 100, 241, 21))
        self.usernameText.setObjectName("usernameText")
        self.passwordText = QtWidgets.QLineEdit(self.centralwidget)
        self.passwordText.setGeometry(QtCore.QRect(90, 130, 241, 21))
        self.passwordText.setObjectName("passwordText")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(10, 160, 101, 16))
        self.label_6.setObjectName("label_6")
        self.masterPassText = QtWidgets.QLineEdit(self.centralwidget)
        self.masterPassText.setGeometry(QtCore.QRect(120, 160, 211, 21))
        self.masterPassText.setObjectName("masterPassText")

        self.passwordText.setEchoMode(QtWidgets.QLineEdit.Password)
        self.masterPassText.setEchoMode(QtWidgets.QLineEdit.Password)

        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.on_click())
        self.addButton.setGeometry(QtCore.QRect(130, 200, 75, 24))
        self.addButton.setObjectName("addButton")
        EnterEntries.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(EnterEntries)
        self.statusbar.setObjectName("statusbar")
        EnterEntries.setStatusBar(self.statusbar)
        

        self.retranslateUi(EnterEntries)
        QtCore.QMetaObject.connectSlotsByName(EnterEntries)

    # def closeEvent(self, event):
    #     self.window_closed.emit()
    #     event.accept()
    #     # event.ignore() # if you want the window to never be closed


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

    def resetTextBox(self):
        self.siteText.setText("")
        self.urlText.setText("")
        self.emailText.setText("")
        self.usernameText.setText("")
        self.passwordText.setText("")
        self.masterPassText.setText("")

    def on_click(self):
        new_site = self.siteText.text()
        new_url = self.urlText.text()
        new_email = self.emailText.text()
        new_username = self.usernameText.text()
        new_pass = self.passwordText.text()
        masterPass = self.masterPassText.text()

        res = self.validateMasterPassword(masterPass)

        if not new_site:
            dlg = CustomDialog("Enter sitename !!!")
            dlg.exec()
        elif not new_url:
            dlg = CustomDialog("Enter URL !!!")
            dlg.exec()
        elif not new_pass:
            dlg = CustomDialog("Enter password !!!")
            dlg.exec()
        elif not res:
            dlg = CustomDialog("Wrong MasterPassword")
            dlg.exec()
        elif addEntry(res[0], res[1], new_site, new_url, new_email, new_username, new_pass):
            dlg = CustomDialog("Entry Added :)")
            dlg.exec()
            self.resetTextBox()
        else:
            dlg = CustomDialog("Entry Already exists")
            dlg.exec()
            self.resetTextBox()
            
            

    def retranslateUi(self, EnterEntries):
        _translate = QtCore.QCoreApplication.translate
        EnterEntries.setWindowTitle(_translate("EnterEntries", "Enter Details"))
        self.label.setText(_translate("EnterEntries", "Sitename :"))
        self.label_2.setText(_translate("EnterEntries", "URL : "))
        self.label_3.setText(_translate("EnterEntries", "Email :"))
        self.label_4.setText(_translate("EnterEntries", "Username :"))
        self.label_5.setText(_translate("EnterEntries", "Password :"))
        self.addButton.setText(_translate("EnterEntries", "Add"))
        self.label_6.setText(_translate("EnterEntries", "Master Password :"))

class CustomDialog(QtWidgets.QDialog):
    def __init__(self, str):
        super().__init__()

        self.setWindowTitle("ERROR")

        QBtn = QtWidgets.QDialogButtonBox.Ok

        self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
        self.buttonBox.accepted.connect(self.accept)
        

        self.layout = QtWidgets.QVBoxLayout()
        message = QtWidgets.QLabel(str)
        self.layout.addWidget(message)
        self.layout.addWidget(self.buttonBox)
        self.setLayout(self.layout)

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    EnterEntries = QtWidgets.QMainWindow()
    ui = Ui_EnterEntries()
    ui.setupUi(EnterEntries)
    EnterEntries.show()
    sys.exit(app.exec_())
