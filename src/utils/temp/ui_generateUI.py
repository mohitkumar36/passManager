# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'generateUI.ui'
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
from PySide6.QtWidgets import (QApplication, QDialog, QLabel, QLineEdit,
    QPushButton, QSizePolicy, QWidget)

class Ui_generatePass(object):
    def setupUi(self, generatePass):
        if not generatePass.objectName():
            generatePass.setObjectName(u"generatePass")
        generatePass.resize(233, 109)
        self.label = QLabel(generatePass)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(10, 10, 171, 41))
        self.lengthPass = QLineEdit(generatePass)
        self.lengthPass.setObjectName(u"lengthPass")
        self.lengthPass.setGeometry(QRect(180, 20, 41, 21))
        self.copyButton = QPushButton(generatePass)
        self.copyButton.setObjectName(u"copyButton")
        self.copyButton.setGeometry(QRect(60, 60, 111, 24))

        self.retranslateUi(generatePass)

        QMetaObject.connectSlotsByName(generatePass)
    # setupUi

    def retranslateUi(self, generatePass):
        generatePass.setWindowTitle(QCoreApplication.translate("generatePass", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("generatePass", u"Enter the length of password :", None))
        self.copyButton.setText(QCoreApplication.translate("generatePass", u"Copy to clipboard", None))
    # retranslateUi

