# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'welcome_page.ui'
##
## Created by: Qt User Interface Compiler version 6.5.2
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
from PySide6.QtWidgets import (QApplication, QLabel, QMainWindow, QPushButton,
    QSizePolicy, QWidget)
from Images_for_design import background_imgs_rc
from Images_for_design import static_img_rc

class Ui_welcome_page(object):
    def setupUi(self, welcome_page):
        if not welcome_page.objectName():
            welcome_page.setObjectName(u"welcome_page")
        welcome_page.resize(869, 628)
        self.centralwidget = QWidget(welcome_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-60, -270, 1001, 1011))
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/default.png);")
        self.btnLogin = QPushButton(self.centralwidget)
        self.btnLogin.setObjectName(u"btnLogin")
        self.btnLogin.setGeometry(QRect(50, 400, 361, 101))
        font = QFont()
        font.setPointSize(18)
        font.setBold(True)
        self.btnLogin.setFont(font)
        icon = QIcon()
        icon.addFile(u":/login/log-in (1).png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogin.setIcon(icon)
        self.btnLogin.setIconSize(QSize(64, 64))
        self.btnRegister = QPushButton(self.centralwidget)
        self.btnRegister.setObjectName(u"btnRegister")
        self.btnRegister.setGeometry(QRect(460, 400, 361, 101))
        font1 = QFont()
        font1.setPointSize(16)
        font1.setBold(True)
        self.btnRegister.setFont(font1)
        icon1 = QIcon()
        icon1.addFile(u":/register/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnRegister.setIcon(icon1)
        self.btnRegister.setIconSize(QSize(64, 64))
        welcome_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(welcome_page)

        QMetaObject.connectSlotsByName(welcome_page)
    # setupUi

    def retranslateUi(self, welcome_page):
        welcome_page.setWindowTitle(QCoreApplication.translate("welcome_page", u"MainWindow", None))
        self.label.setText(QCoreApplication.translate("welcome_page", u"TextLabel", None))
        self.btnLogin.setText(QCoreApplication.translate("welcome_page", u"		Log into existing \n"
"		account", None))
        self.btnRegister.setText(QCoreApplication.translate("welcome_page", u"		Register New \n"
"		Account", None))
    # retranslateUi

