# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'addUI.ui'
##
## Created by: Qt User Interface Compiler version 6.2.4
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QLabel, QLineEdit, QMainWindow,
    QPushButton, QSizePolicy, QStatusBar, QWidget)

class Ui_EnterEntries(object):
    def setupUi(self, EnterEntries):
        if not EnterEntries.objectName():
            EnterEntries.setObjectName(u"EnterEntries")
        EnterEntries.resize(344, 259)
        self.centralwidget = QWidget(EnterEntries)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 10, 61, 21))
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(20, 40, 49, 16))
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(20, 70, 49, 16))
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 100, 61, 21))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 130, 61, 21))
        self.addButton = QPushButton(self.centralwidget)
        self.addButton.setObjectName(u"addButton")
        self.addButton.setGeometry(QRect(130, 200, 75, 24))
        self.siteText = QLineEdit(self.centralwidget)
        self.siteText.setObjectName(u"siteText")
        self.siteText.setGeometry(QRect(90, 10, 241, 21))
        self.urlText = QLineEdit(self.centralwidget)
        self.urlText.setObjectName(u"urlText")
        self.urlText.setGeometry(QRect(60, 40, 271, 21))
        self.emailText = QLineEdit(self.centralwidget)
        self.emailText.setObjectName(u"emailText")
        self.emailText.setGeometry(QRect(70, 70, 261, 21))
        self.usernameText = QLineEdit(self.centralwidget)
        self.usernameText.setObjectName(u"usernameText")
        self.usernameText.setGeometry(QRect(90, 100, 241, 21))
        self.passwordText = QLineEdit(self.centralwidget)
        self.passwordText.setObjectName(u"passwordText")
        self.passwordText.setGeometry(QRect(90, 130, 241, 21))
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 160, 101, 16))
        self.masterPassText = QLineEdit(self.centralwidget)
        self.masterPassText.setObjectName(u"masterPassText")
        self.masterPassText.setGeometry(QRect(120, 160, 211, 21))
        EnterEntries.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(EnterEntries)
        self.statusbar.setObjectName(u"statusbar")
        EnterEntries.setStatusBar(self.statusbar)

        self.retranslateUi(EnterEntries)

        QMetaObject.connectSlotsByName(EnterEntries)
    # setupUi

    def retranslateUi(self, EnterEntries):
        EnterEntries.setWindowTitle(QCoreApplication.translate("EnterEntries", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("EnterEntries", u"Sitename :", None))
        self.label_2.setText(QCoreApplication.translate("EnterEntries", u"URL : ", None))
        self.label_3.setText(QCoreApplication.translate("EnterEntries", u"Email :", None))
        self.label_4.setText(QCoreApplication.translate("EnterEntries", u"Username :", None))
        self.label_5.setText(QCoreApplication.translate("EnterEntries", u"Password :", None))
        self.addButton.setText(QCoreApplication.translate("EnterEntries", u"Add", None))
        self.label_6.setText(QCoreApplication.translate("EnterEntries", u"Master Password :", None))
    # retranslateUi

