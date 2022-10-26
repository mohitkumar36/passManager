import sys
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QPushButton, QAction, QLineEdit, QMessageBox
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

from utils.loginUI import Login
from utils.retrieve import retrieveEntries


def start():
    app = QApplication(sys.argv)
    Login()
    sys.exit(app.exec_())