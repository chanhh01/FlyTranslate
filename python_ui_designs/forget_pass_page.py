# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'forget_pass_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from Images_for_design import background_imgs_rc
from Images_for_design import interactable_image_source_rc

class Ui_forgot_password(object):
    def setupUi(self, forgot_password):
        if not forgot_password.objectName():
            forgot_password.setObjectName(u"forgot_password")
        forgot_password.resize(536, 591)
        self.centralwidget = QWidget(forgot_password)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -280, 571, 881))
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 521, 571))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(26)
        font.setBold(True)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.label_4.setLayoutDirection(Qt.LeftToRight)
        self.label_4.setFrameShape(QFrame.Box)
        self.label_4.setAlignment(Qt.AlignHCenter|Qt.AlignTop)
        self.label_4.setWordWrap(False)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(160, 90, 171, 21))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_2.setFont(font1)
        self.txtEmail = QLineEdit(self.centralwidget)
        self.txtEmail.setObjectName(u"txtEmail")
        self.txtEmail.setGeometry(QRect(160, 120, 221, 31))
        self.txtEmail.setEchoMode(QLineEdit.Normal)
        self.lblbtnViewOrHidePass = QLabel(self.centralwidget)
        self.lblbtnViewOrHidePass.setObjectName(u"lblbtnViewOrHidePass")
        self.lblbtnViewOrHidePass.setGeometry(QRect(350, 410, 41, 31))
        self.lblbtnViewOrHidePass.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")
        self.lblbtnViewOrHidePass.setFrameShape(QFrame.Panel)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(160, 380, 171, 16))
        self.label_3.setFont(font1)
        self.txtNewPass = QLineEdit(self.centralwidget)
        self.txtNewPass.setObjectName(u"txtNewPass")
        self.txtNewPass.setGeometry(QRect(160, 410, 190, 31))
        self.txtNewPass.setEchoMode(QLineEdit.Password)
        self.btnConfirmReset = QPushButton(self.centralwidget)
        self.btnConfirmReset.setObjectName(u"btnConfirmReset")
        self.btnConfirmReset.setGeometry(QRect(320, 470, 101, 41))
        self.btnConfirmReset.setFont(font1)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(110, 470, 101, 41))
        self.btnBack.setFont(font1)
        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setGeometry(QRect(20, 350, 511, 16))
        font2 = QFont()
        font2.setStrikeOut(True)
        self.label_9.setFont(font2)
        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setGeometry(QRect(20, 220, 511, 16))
        self.label_10.setFont(font2)
        self.btnSendOTP = QPushButton(self.centralwidget)
        self.btnSendOTP.setObjectName(u"btnSendOTP")
        self.btnSendOTP.setGeometry(QRect(210, 170, 111, 41))
        self.btnSendOTP.setFont(font1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(190, 260, 51, 16))
        self.label_7.setFont(font1)
        self.btnVerifyOTP = QPushButton(self.centralwidget)
        self.btnVerifyOTP.setObjectName(u"btnVerifyOTP")
        self.btnVerifyOTP.setGeometry(QRect(210, 300, 111, 41))
        self.btnVerifyOTP.setFont(font1)
        self.txtOTP = QLineEdit(self.centralwidget)
        self.txtOTP.setObjectName(u"txtOTP")
        self.txtOTP.setGeometry(QRect(240, 250, 101, 31))
        forgot_password.setCentralWidget(self.centralwidget)

        self.retranslateUi(forgot_password)

        QMetaObject.connectSlotsByName(forgot_password)
    # setupUi

    def retranslateUi(self, forgot_password):
        forgot_password.setWindowTitle(QCoreApplication.translate("forgot_password", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("forgot_password", u"Reset Password", None))
        self.label_2.setText(QCoreApplication.translate("forgot_password", u"Enter your email:", None))
        self.lblbtnViewOrHidePass.setText("")
        self.label_3.setText(QCoreApplication.translate("forgot_password", u"New Password:", None))
        self.btnConfirmReset.setText(QCoreApplication.translate("forgot_password", u"Reset", None))
        self.btnBack.setText(QCoreApplication.translate("forgot_password", u"Back", None))
        self.label_9.setText(QCoreApplication.translate("forgot_password", u"----------------------------------------------------------------------------------------------------", None))
        self.label_10.setText(QCoreApplication.translate("forgot_password", u"----------------------------------------------------------------------------------------------------", None))
        self.btnSendOTP.setText(QCoreApplication.translate("forgot_password", u"Send OTP", None))
        self.label_7.setText(QCoreApplication.translate("forgot_password", u"OTP:", None))
        self.btnVerifyOTP.setText(QCoreApplication.translate("forgot_password", u"Verify OTP", None))
    # retranslateUi

