# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'runtime_setting_page.ui'
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
    QMainWindow, QPushButton, QSizePolicy, QWidget)
from Images_for_design import interactable_image_source_rc
from Images_for_design import background_imgs_rc
from Images_for_design import static_img_rc

class Ui_runtime_setting_page(object):
    def setupUi(self, runtime_setting_page):
        if not runtime_setting_page.objectName():
            runtime_setting_page.setObjectName(u"runtime_setting_page")
        runtime_setting_page.resize(794, 586)
        self.centralwidget = QWidget(runtime_setting_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        self.frame.setGeometry(QRect(0, 0, 151, 591))
        self.frame.setFrameShape(QFrame.StyledPanel)
        self.frame.setFrameShadow(QFrame.Raised)
        self.label = QLabel(self.frame)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, 80, 151, 511))
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label_6 = QLabel(self.frame)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setGeometry(QRect(0, -20, 151, 111))
        self.label_6.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/logo_only_2.png);")
        self.label_6.setScaledContents(True)
        self.btnMainButton = QPushButton(self.frame)
        self.btnMainButton.setObjectName(u"btnMainButton")
        self.btnMainButton.setGeometry(QRect(0, 90, 151, 51))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnMainButton.setFont(font)
        self.btnMainButton.setAutoFillBackground(True)
        self.btnMainButton.setCheckable(True)
        self.btnMainButton.setChecked(False)
        self.btnRunTimeSettings = QPushButton(self.frame)
        self.btnRunTimeSettings.setObjectName(u"btnRunTimeSettings")
        self.btnRunTimeSettings.setGeometry(QRect(0, 140, 151, 51))
        self.btnRunTimeSettings.setFont(font)
        self.btnRunTimeSettings.setAutoFillBackground(True)
        self.btnRunTimeSettings.setCheckable(True)
        self.btnRunTimeSettings.setChecked(True)
        self.btnProfileSettings = QPushButton(self.frame)
        self.btnProfileSettings.setObjectName(u"btnProfileSettings")
        self.btnProfileSettings.setGeometry(QRect(0, 190, 151, 51))
        self.btnProfileSettings.setFont(font)
        self.btnProfileSettings.setAutoFillBackground(True)
        self.btnProfileSettings.setCheckable(True)
        self.btnProfileSettings.setChecked(False)
        self.btnFAQ = QPushButton(self.frame)
        self.btnFAQ.setObjectName(u"btnFAQ")
        self.btnFAQ.setGeometry(QRect(0, 240, 151, 51))
        self.btnFAQ.setFont(font)
        self.btnFAQ.setAutoFillBackground(True)
        self.btnFAQ.setCheckable(True)
        self.btnFAQ.setChecked(False)
        self.btnLogout = QPushButton(self.frame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setGeometry(QRect(0, 535, 151, 51))
        self.btnLogout.setFont(font)
        self.btnLogout.setAutoFillBackground(True)
        icon = QIcon()
        icon.addFile(u":/logout/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon)
        self.btnLogout.setCheckable(False)
        self.btnLogout.setChecked(False)
        self.btnFeedback = QPushButton(self.frame)
        self.btnFeedback.setObjectName(u"btnFeedback")
        self.btnFeedback.setGeometry(QRect(0, 290, 151, 51))
        self.btnFeedback.setFont(font)
        self.btnFeedback.setAutoFillBackground(True)
        self.btnFeedback.setCheckable(True)
        self.btnFeedback.setChecked(False)
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(153, 0, 641, 591))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 131, 16))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.label_4.setFont(font1)
        self.lblUsername = QLabel(self.frame_2)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(20, 40, 431, 21))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(14)
        font2.setBold(True)
        font2.setItalic(True)
        self.lblUsername.setFont(font2)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 811, 591))
        self.label_2.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label_2.setScaledContents(True)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(30, 160, 201, 21))
        self.label_7.setFont(font)
        self.cbSaveLog = QCheckBox(self.frame_2)
        self.cbSaveLog.setObjectName(u"cbSaveLog")
        self.cbSaveLog.setGeometry(QRect(510, 155, 61, 41))
        self.cbSaveLog.setAutoFillBackground(False)
        self.cbSaveLog.setStyleSheet(u"QCheckBox::indicator:unchecked{\n"
"	image: url(:/not-toggled/off-button.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/toggled/on-button.png);\n"
"}")
        self.cbSaveLog.setChecked(False)
        self.cbSaveLog.setTristate(False)
        self.cbMinimizeOnLaunch = QCheckBox(self.frame_2)
        self.cbMinimizeOnLaunch.setObjectName(u"cbMinimizeOnLaunch")
        self.cbMinimizeOnLaunch.setGeometry(QRect(510, 225, 61, 41))
        self.cbMinimizeOnLaunch.setAutoFillBackground(False)
        self.cbMinimizeOnLaunch.setStyleSheet(u"QCheckBox::indicator:unchecked{\n"
"	image: url(:/not-toggled/off-button.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/toggled/on-button.png);\n"
"}")
        self.cbMinimizeOnLaunch.setChecked(False)
        self.cbMinimizeOnLaunch.setTristate(False)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(30, 230, 401, 31))
        self.label_8.setFont(font)
        self.label_11 = QLabel(self.frame_2)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setGeometry(QRect(10, 200, 621, 16))
        font3 = QFont()
        font3.setStrikeOut(True)
        self.label_11.setFont(font3)
        self.label_13 = QLabel(self.frame_2)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setGeometry(QRect(10, 130, 621, 16))
        self.label_13.setFont(font3)
        self.cbReplaceText = QCheckBox(self.frame_2)
        self.cbReplaceText.setObjectName(u"cbReplaceText")
        self.cbReplaceText.setGeometry(QRect(510, 85, 61, 41))
        self.cbReplaceText.setAutoFillBackground(False)
        self.cbReplaceText.setStyleSheet(u"QCheckBox::indicator:unchecked{\n"
"	image: url(:/not-toggled/off-button.png);\n"
"}\n"
"\n"
"QCheckBox::indicator:checked{\n"
"	image: url(:/toggled/on-button.png);\n"
"}")
        self.cbReplaceText.setChecked(False)
        self.cbReplaceText.setTristate(False)
        self.label_17 = QLabel(self.frame_2)
        self.label_17.setObjectName(u"label_17")
        self.label_17.setGeometry(QRect(30, 90, 381, 21))
        self.label_17.setFont(font)
        self.btnSaveSettings = QPushButton(self.frame_2)
        self.btnSaveSettings.setObjectName(u"btnSaveSettings")
        self.btnSaveSettings.setGeometry(QRect(260, 510, 131, 41))
        font4 = QFont()
        font4.setPointSize(9)
        font4.setBold(True)
        self.btnSaveSettings.setFont(font4)
        self.btnSaveSettings.setCheckable(False)
        self.lblTipsMinimized = QLabel(self.frame_2)
        self.lblTipsMinimized.setObjectName(u"lblTipsMinimized")
        self.lblTipsMinimized.setGeometry(QRect(590, 228, 31, 31))
        self.lblTipsMinimized.setStyleSheet(u"image: url(:/tips/information.png);")
        self.lblTipsTextReplace = QLabel(self.frame_2)
        self.lblTipsTextReplace.setObjectName(u"lblTipsTextReplace")
        self.lblTipsTextReplace.setGeometry(QRect(590, 88, 31, 31))
        self.lblTipsTextReplace.setStyleSheet(u"image: url(:/tips/information.png);")
        self.label_2.raise_()
        self.label_4.raise_()
        self.lblUsername.raise_()
        self.label_7.raise_()
        self.cbSaveLog.raise_()
        self.cbMinimizeOnLaunch.raise_()
        self.label_8.raise_()
        self.label_11.raise_()
        self.label_13.raise_()
        self.cbReplaceText.raise_()
        self.label_17.raise_()
        self.btnSaveSettings.raise_()
        self.lblTipsMinimized.raise_()
        self.lblTipsTextReplace.raise_()
        runtime_setting_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(runtime_setting_page)

        QMetaObject.connectSlotsByName(runtime_setting_page)
    # setupUi

    def retranslateUi(self, runtime_setting_page):
        runtime_setting_page.setWindowTitle(QCoreApplication.translate("runtime_setting_page", u"MainWindow", None))
        self.label.setText("")
        self.label_6.setText("")
        self.btnMainButton.setText(QCoreApplication.translate("runtime_setting_page", u"Main Page", None))
        self.btnRunTimeSettings.setText(QCoreApplication.translate("runtime_setting_page", u"Runtime Setting", None))
        self.btnProfileSettings.setText(QCoreApplication.translate("runtime_setting_page", u"Profile Setting", None))
        self.btnFAQ.setText(QCoreApplication.translate("runtime_setting_page", u"FAQ", None))
        self.btnLogout.setText(QCoreApplication.translate("runtime_setting_page", u"  Log out", None))
        self.btnFeedback.setText(QCoreApplication.translate("runtime_setting_page", u"Feedback", None))
        self.label_4.setText(QCoreApplication.translate("runtime_setting_page", u"Welcome Back,", None))
        self.lblUsername.setText(QCoreApplication.translate("runtime_setting_page", u"SAMPLEUSERNAME!!", None))
        self.label_2.setText("")
        self.label_7.setText(QCoreApplication.translate("runtime_setting_page", u"Save translation logs", None))
        self.cbSaveLog.setText("")
        self.cbMinimizeOnLaunch.setText("")
        self.label_8.setText(QCoreApplication.translate("runtime_setting_page", u"<html><head/><body><p>Launch minimized operation window upon login</p></body></html>", None))
        self.label_11.setText(QCoreApplication.translate("runtime_setting_page", u"----------------------------------------------------------------------------------------------------------------------------", None))
        self.label_13.setText(QCoreApplication.translate("runtime_setting_page", u"----------------------------------------------------------------------------------------------------------------------------", None))
        self.cbReplaceText.setText("")
        self.label_17.setText(QCoreApplication.translate("runtime_setting_page", u"Erase original text and replace output text", None))
        self.btnSaveSettings.setText(QCoreApplication.translate("runtime_setting_page", u"Save settings", None))
        self.lblTipsMinimized.setText("")
        self.lblTipsTextReplace.setText("")
    # retranslateUi

