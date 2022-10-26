# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'confirm.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QPushButton,
    QSizePolicy, QWidget)

class Ui_Confirm(object):
    def setupUi(self, Confirm):
        if not Confirm.objectName():
            Confirm.setObjectName(u"Confirm")
        Confirm.resize(159, 104)
        self.label = QLabel(Confirm)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(20, 20, 131, 31))
        font = QFont()
        font.setFamilies([u"Arial"])
        font.setPointSize(12)
        self.label.setFont(font)
        self.okButton = QPushButton(Confirm)
        self.okButton.setObjectName(u"okButton")
        self.okButton.setGeometry(QRect(40, 60, 75, 24))

        self.retranslateUi(Confirm)

        QMetaObject.connectSlotsByName(Confirm)
    # setupUi

    def retranslateUi(self, Confirm):
        Confirm.setWindowTitle(QCoreApplication.translate("Confirm", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Confirm", u"Entry Added :)", None))
        self.okButton.setText(QCoreApplication.translate("Confirm", u"OK", None))
    # retranslateUi

