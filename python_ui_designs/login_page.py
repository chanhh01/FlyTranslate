# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'login_page.ui'
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QFrame, QLabel,
    QLineEdit, QMainWindow, QPushButton, QSizePolicy,
    QWidget)
from Images_for_design import background_imgs_rc
from Images_for_design import interactable_image_source_rc
from Images_for_design import static_img_rc

class Ui_login_page(object):
    def setupUi(self, login_page):
        if not login_page.objectName():
            login_page.setObjectName(u"login_page")
        login_page.resize(536, 591)
        self.centralwidget = QWidget(login_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -280, 571, 881))
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label.setScaledContents(True)
        self.txtUsernameOrEmail = QLineEdit(self.centralwidget)
        self.txtUsernameOrEmail.setObjectName(u"txtUsernameOrEmail")
        self.txtUsernameOrEmail.setGeometry(QRect(160, 140, 231, 31))
        self.txtPass = QLineEdit(self.centralwidget)
        self.txtPass.setObjectName(u"txtPass")
        self.txtPass.setGeometry(QRect(160, 220, 191, 31))
        self.txtPass.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 110, 171, 16))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.label_2.setFont(font)
        self.cbRememberDevice = QCheckBox(self.centralwidget)
        self.cbRememberDevice.setObjectName(u"cbRememberDevice")
        self.cbRememberDevice.setGeometry(QRect(220, 270, 131, 21))
        font1 = QFont()
        font1.setPointSize(9)
        font1.setBold(True)
        self.cbRememberDevice.setFont(font1)
        self.cbRememberDevice.setCursor(QCursor(Qt.PointingHandCursor))
        self.cbRememberDevice.setIconSize(QSize(32, 32))
        self.btnLoginAcc = QPushButton(self.centralwidget)
        self.btnLoginAcc.setObjectName(u"btnLoginAcc")
        self.btnLoginAcc.setGeometry(QRect(320, 390, 101, 41))
        self.btnLoginAcc.setFont(font)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 190, 91, 16))
        self.label_3.setFont(font)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(140, 390, 101, 41))
        self.btnBack.setFont(font)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 521, 571))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(26)
        font2.setBold(True)
        font2.setItalic(True)
        self.label_4.setFont(font2)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.lblbtnViewOrHidePass = QLabel(self.centralwidget)
        self.lblbtnViewOrHidePass.setObjectName(u"lblbtnViewOrHidePass")
        self.lblbtnViewOrHidePass.setGeometry(QRect(350, 220, 41, 31))
        self.lblbtnViewOrHidePass.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")
        self.lblbtnViewOrHidePass.setFrameShape(QFrame.Panel)
        self.lblbtnForgotPass = QLabel(self.centralwidget)
        self.lblbtnForgotPass.setObjectName(u"lblbtnForgotPass")
        self.lblbtnForgotPass.setGeometry(QRect(160, 300, 231, 51))
        font3 = QFont()
        font3.setFamilies([u"Segoe UI Semibold"])
        font3.setPointSize(9)
        font3.setBold(True)
        font3.setItalic(False)
        font3.setUnderline(True)
        self.lblbtnForgotPass.setFont(font3)
        self.lblbtnForgotPass.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblbtnForgotPass.setFrameShape(QFrame.NoFrame)
        self.lblbtnForgotPass.setTextFormat(Qt.AutoText)
        self.lblbtnForgotPass.setAlignment(Qt.AlignCenter)
        self.lblbtnForgotPass.setWordWrap(False)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(10, 460, 521, 121))
        self.label_6.setFont(font)
        self.label_6.setFrameShape(QFrame.Box)
        self.label_6.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.btnToRegister = QPushButton(self.centralwidget)
        self.btnToRegister.setObjectName(u"btnToRegister")
        self.btnToRegister.setGeometry(QRect(150, 510, 261, 51))
        self.btnToRegister.setFont(font)
        icon = QIcon()
        icon.addFile(u":/register/edit.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnToRegister.setIcon(icon)
        self.btnToRegister.setIconSize(QSize(32, 32))
        login_page.setCentralWidget(self.centralwidget)
        self.label.raise_()
        self.label_4.raise_()
        self.label_3.raise_()
        self.txtPass.raise_()
        self.cbRememberDevice.raise_()
        self.label_2.raise_()
        self.txtUsernameOrEmail.raise_()
        self.btnBack.raise_()
        self.btnLoginAcc.raise_()
        self.lblbtnViewOrHidePass.raise_()
        self.lblbtnForgotPass.raise_()
        self.label_6.raise_()
        self.btnToRegister.raise_()

        self.retranslateUi(login_page)

        QMetaObject.connectSlotsByName(login_page)
    # setupUi

    def retranslateUi(self, login_page):
        login_page.setWindowTitle(QCoreApplication.translate("login_page", u"MainWindow", None))
        self.label.setText("")
        self.label_2.setText(QCoreApplication.translate("login_page", u"Username or Email:", None))
        self.cbRememberDevice.setText(QCoreApplication.translate("login_page", u"Remember Me", None))
        self.btnLoginAcc.setText(QCoreApplication.translate("login_page", u"Log In", None))
        self.label_3.setText(QCoreApplication.translate("login_page", u"Password:", None))
        self.btnBack.setText(QCoreApplication.translate("login_page", u"Back", None))
        self.label_4.setText(QCoreApplication.translate("login_page", u"Login to Your Account", None))
        self.lblbtnViewOrHidePass.setText("")
        self.lblbtnForgotPass.setText(QCoreApplication.translate("login_page", u"<html><head/><body><p>Forgot password?</p><p>--&gt;Retrieve password here!&lt;--</p></body></html>", None))
        self.label_6.setText(QCoreApplication.translate("login_page", u"If you do not have existing account:", None))
        self.btnToRegister.setText(QCoreApplication.translate("login_page", u"Register your account!", None))
    # retranslateUi

