from PyQt5 import QtCore, QtGui, QtWidgets


from generate import generatePassword


class Ui_generatePass(object):
    def setupUi(self, generatePass):
        generatePass.setObjectName("generatePass")
        generatePass.resize(233, 109)
        self.label = QtWidgets.QLabel(generatePass)
        self.label.setGeometry(QtCore.QRect(10, 10, 171, 41))
        self.label.setObjectName("label")
        self.lengthPass = QtWidgets.QLineEdit(generatePass)
        self.lengthPass.setGeometry(QtCore.QRect(180, 20, 41, 21))
        self.lengthPass.setObjectName("lengthPass")
        self.copyButton = QtWidgets.QPushButton(generatePass, clicked = lambda: self.on_click() or generatePass.accept())
        #self.copyButton.accepted.connect(Dialog.accept)
        #self.copyButton.clicked.connect(self, lambda : QtWidgets.QDialog.accept())
        self.copyButton.setGeometry(QtCore.QRect(60, 60, 111, 24))
        self.copyButton.setObjectName("copyButton")

        self.retranslateUi(generatePass)
        QtCore.QMetaObject.connectSlotsByName(generatePass)

    def on_click(self):
        try:
            len = int(self.lengthPass.text())
            QtWidgets.QApplication.clipboard().setText(generatePassword(len))
            # self.close()
            
        except:
            dlg = CustomDialog("Invalid Length !!!")
            dlg.exec()

   

    def retranslateUi(self, generatePass):
        _translate = QtCore.QCoreApplication.translate
        generatePass.setWindowTitle(_translate("generatePass", "Get your password"))
        self.label.setText(_translate("generatePass", "Enter the length of password :"))
        self.copyButton.setText(_translate("generatePass", "Copy to clipboard"))

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
    generatePass = QtWidgets.QDialog()
    ui = Ui_generatePass()
    ui.setupUi(generatePass)
    generatePass.show()
    sys.exit(app.exec_())
