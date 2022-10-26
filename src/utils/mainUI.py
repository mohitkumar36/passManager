import hashlib
from wsgiref import validate
from PyQt5 import QtCore, QtGui, QtWidgets

from addUI import Ui_EnterEntries
from aesutil import decrypt
from dbconfig import dbconfig
from generateUI import Ui_generatePass
from retrieve import computeMasterKey, retrieveEntries


class Ui_MainPage(object):
    def add(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_EnterEntries()
        self.ui.setupUi(self.window)
        self.window.show()

    def geneUI(self):
        self.window = QtWidgets.QDialog()
        self.ui = Ui_generatePass()
        self.ui.setupUi(self.window)
        self.window.show()

    def setupUi(self, MainPage):
        MainPage.setObjectName("MainPage")
        MainPage.resize(670, 424)
        self.centralwidget = QtWidgets.QWidget(MainPage)
        self.centralwidget.setObjectName("centralwidget")
        MainPage.setCentralWidget(self.centralwidget)

        self.df = retrieveEntries()

        self.tableWidget = QtWidgets.QTableWidget()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

        self.vbox = QtWidgets.QVBoxLayout()
        self.vbox.addWidget(self.tableWidget)
        self.centralwidget.setLayout(self.vbox)

        self.menubar = QtWidgets.QMenuBar(MainPage)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 599, 22))
        self.menubar.setObjectName("menubar")
        self.menuAdd_Entries = QtWidgets.QMenu(self.menubar)
        self.menuAdd_Entries.setObjectName("menuAdd_Entries")
        MainPage.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainPage)
        self.statusbar.setObjectName("statusbar")
        MainPage.setStatusBar(self.statusbar)
        self.actionAdd_Entries = QtWidgets.QAction(MainPage)
        self.actionAdd_Entries.setObjectName("actionAdd_Entries")
        self.actionGenerate_Password = QtWidgets.QAction(MainPage)
        self.actionGenerate_Password.setObjectName("actionGenerate_Password")
        self.menuAdd_Entries.addAction(self.actionAdd_Entries)
        self.actionAdd_Entries.triggered.connect(lambda : self.add())
        
        self.menuAdd_Entries.addAction(self.actionGenerate_Password)
        self.actionGenerate_Password.triggered.connect(lambda : self.geneUI())

        self.menubar.addAction(self.menuAdd_Entries.menuAction())

        self.addButton = QtWidgets.QPushButton(self.centralwidget, clicked = lambda : self.getPass())
        self.addButton.setGeometry(QtCore.QRect(555, 335, 100, 24))
        
        self.addButton.setObjectName("addButton")

        self.retranslateUi(MainPage)
        QtCore.QMetaObject.connectSlotsByName(MainPage)
        self.loadData()
        # QtCore.QTimer.singleShot(10000, self.setupUi(MainPage))


    def getPass(self):
        r = self.tableWidget.currentRow()
        # print(r)
        # print(self.df[r])

        # dlg = CustomDialog("Enter MasterPassword : ")
        # arrPass = dlg.verify()
        # print(arrPass)
        # dlg.exec()
        arrPass = []
        flag = True
        while flag:
            strPass, ok = QtWidgets.QInputDialog.getText(self.centralwidget, 'To Copy', 'Enter MasterPassword:', QtWidgets.QLineEdit.Password)
            if ok:
                arrPass = self.validateMasterPassword(strPass)
                if not arrPass:
                    dlg = CustomDialog("Incorrect MasterPassword !!!")
                    dlg.exec()
                else:
                    flag = False
            else:
                flag = False
        
        if arrPass:
            mk = computeMasterKey(arrPass[0], arrPass[1])
            decrypted = decrypt(key = mk, source=self.df[r][4], keyType="bytes")
            QtWidgets.QApplication.clipboard().setText(decrypted.decode())

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

    def loadData(self):

        self.tableWidget.setRowCount(len(self.df))
        self.tableWidget.setColumnCount(5)
        titles = ["Site Name", "URL", "Email", "Username", "Password"]
        # for i, v in enumerate(titles):
        #     tableWidget.setHorizontalHeaderItem(i, QtWidgets.QTableWidgetItem(v))
        self.tableWidget.setHorizontalHeaderLabels(titles)

        for r in range(len(self.df)):
            for c in range(5):
                if c == 4:
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem("{hidden}"))
                else:
                    self.tableWidget.setItem(r, c, QtWidgets.QTableWidgetItem(self.df[r][c]))


    def retranslateUi(self, MainPage):
        _translate = QtCore.QCoreApplication.translate
        MainPage.setWindowTitle(_translate("MainPage", "Your Entries"))
        self.menuAdd_Entries.setTitle(_translate("MainPage", "Edit"))
        self.actionAdd_Entries.setText(_translate("MainPage", "Add Entries"))
        self.actionGenerate_Password.setText(_translate("MainPage", "Generate Password"))
        self.addButton.setText(_translate("MainPage", "Copy Password"))


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

# class CustomDialog(QtWidgets.QDialog):
#     def __init__(self, str):
#         super().__init__()

#         self.setWindowTitle("To Copy")
#         self.strPass = ''

#         QBtn = QtWidgets.QDialogButtonBox.Ok
#         self.masterpass = QtWidgets.QLineEdit(self)
#         self.masterpass.setGeometry(QtCore.QRect(160, 20, 200, 21))
#         # self.usernameText = QtWidgets.QLineEdit(self.centralwidget)
#         # self.usernameText.setGeometry(QtCore.QRect(90, 100, 241, 21))
#         # self.usernameText.setObjectName("usernameText")

#         self.buttonBox = QtWidgets.QDialogButtonBox(QBtn)
#         self.buttonBox.accepted.connect(self.accept)

#         # self.setGeometry(0, 0, 200, 400)
#         self.resize(370, 100)
        

#         self.layout = QtWidgets.QVBoxLayout()
#         message = QtWidgets.QLabel(str)
#         self.layout.addWidget(message)
#         self.layout.addWidget(self.buttonBox)
#         self.setLayout(self.layout)
    
#     def verify(self):
#         self.strPass = self.masterpass.text()
#         return

# class acceptMaster(QtWidgets.QInputDialog()):
#     def __init__(self) -> None:
#         super().__init__()
        



if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainPage = QtWidgets.QMainWindow()
    ui = Ui_MainPage()
    ui.setupUi(MainPage)
    MainPage.show()
    sys.exit(app.exec_())
