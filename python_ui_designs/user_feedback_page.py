# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'user_feedback_page.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QMainWindow,
    QPushButton, QSizePolicy, QTextEdit, QWidget)
from Images_for_design import static_img_rc
from Images_for_design import background_imgs_rc

class Ui_user_feedback_page(object):
    def setupUi(self, user_feedback_page):
        if not user_feedback_page.objectName():
            user_feedback_page.setObjectName(u"user_feedback_page")
        user_feedback_page.resize(794, 586)
        self.centralwidget = QWidget(user_feedback_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setGeometry(QRect(153, 0, 641, 591))
        self.frame_2.setFrameShape(QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Raised)
        self.label_4 = QLabel(self.frame_2)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(20, 20, 131, 16))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(11)
        font.setItalic(True)
        self.label_4.setFont(font)
        self.lblUsername = QLabel(self.frame_2)
        self.lblUsername.setObjectName(u"lblUsername")
        self.lblUsername.setGeometry(QRect(20, 40, 431, 21))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(14)
        font1.setBold(True)
        font1.setItalic(True)
        self.lblUsername.setFont(font1)
        self.label_2 = QLabel(self.frame_2)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 811, 591))
        self.label_2.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label_2.setScaledContents(True)
        self.label_5 = QLabel(self.frame_2)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(20, 100, 381, 16))
        self.label_5.setFont(font)
        self.txtTitle = QTextEdit(self.frame_2)
        self.txtTitle.setObjectName(u"txtTitle")
        self.txtTitle.setGeometry(QRect(20, 130, 601, 31))
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 180, 161, 16))
        self.label_7.setFont(font)
        self.txtContent = QTextEdit(self.frame_2)
        self.txtContent.setObjectName(u"txtContent")
        self.txtContent.setGeometry(QRect(20, 210, 601, 301))
        self.btnSubmitFeedback = QPushButton(self.frame_2)
        self.btnSubmitFeedback.setObjectName(u"btnSubmitFeedback")
        self.btnSubmitFeedback.setGeometry(QRect(360, 530, 171, 41))
        font2 = QFont()
        font2.setPointSize(10)
        font2.setBold(True)
        self.btnSubmitFeedback.setFont(font2)
        self.btnClear = QPushButton(self.frame_2)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(110, 530, 171, 41))
        self.btnClear.setFont(font2)
        self.label_2.raise_()
        self.label_4.raise_()
        self.lblUsername.raise_()
        self.label_5.raise_()
        self.txtTitle.raise_()
        self.label_7.raise_()
        self.txtContent.raise_()
        self.btnSubmitFeedback.raise_()
        self.btnClear.raise_()
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
        self.btnMainButton.setFont(font2)
        self.btnMainButton.setAutoFillBackground(True)
        self.btnMainButton.setCheckable(True)
        self.btnMainButton.setChecked(False)
        self.btnRunTimeSettings = QPushButton(self.frame)
        self.btnRunTimeSettings.setObjectName(u"btnRunTimeSettings")
        self.btnRunTimeSettings.setGeometry(QRect(0, 140, 151, 51))
        self.btnRunTimeSettings.setFont(font2)
        self.btnRunTimeSettings.setAutoFillBackground(True)
        self.btnRunTimeSettings.setCheckable(True)
        self.btnRunTimeSettings.setChecked(False)
        self.btnProfileSettings = QPushButton(self.frame)
        self.btnProfileSettings.setObjectName(u"btnProfileSettings")
        self.btnProfileSettings.setGeometry(QRect(0, 190, 151, 51))
        self.btnProfileSettings.setFont(font2)
        self.btnProfileSettings.setAutoFillBackground(True)
        self.btnProfileSettings.setCheckable(True)
        self.btnProfileSettings.setChecked(False)
        self.btnFAQ = QPushButton(self.frame)
        self.btnFAQ.setObjectName(u"btnFAQ")
        self.btnFAQ.setGeometry(QRect(0, 240, 151, 51))
        self.btnFAQ.setFont(font2)
        self.btnFAQ.setAutoFillBackground(True)
        self.btnFAQ.setCheckable(True)
        self.btnFAQ.setChecked(False)
        self.btnLogout = QPushButton(self.frame)
        self.btnLogout.setObjectName(u"btnLogout")
        self.btnLogout.setGeometry(QRect(0, 535, 151, 51))
        self.btnLogout.setFont(font2)
        self.btnLogout.setAutoFillBackground(True)
        icon = QIcon()
        icon.addFile(u":/logout/logout.png", QSize(), QIcon.Normal, QIcon.Off)
        self.btnLogout.setIcon(icon)
        self.btnLogout.setCheckable(False)
        self.btnLogout.setChecked(False)
        self.btnFeedback = QPushButton(self.frame)
        self.btnFeedback.setObjectName(u"btnFeedback")
        self.btnFeedback.setGeometry(QRect(0, 290, 151, 51))
        self.btnFeedback.setFont(font2)
        self.btnFeedback.setAutoFillBackground(True)
        self.btnFeedback.setCheckable(True)
        self.btnFeedback.setChecked(True)
        user_feedback_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(user_feedback_page)

        QMetaObject.connectSlotsByName(user_feedback_page)
    # setupUi

    def retranslateUi(self, user_feedback_page):
        user_feedback_page.setWindowTitle(QCoreApplication.translate("user_feedback_page", u"MainWindow", None))
        self.label_4.setText(QCoreApplication.translate("user_feedback_page", u"Welcome Back,", None))
        self.lblUsername.setText(QCoreApplication.translate("user_feedback_page", u"SAMPLEUSERNAME!!", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("user_feedback_page", u"Feedback title: (no more than 255 characters)", None))
        self.label_7.setText(QCoreApplication.translate("user_feedback_page", u"Feedback Content:", None))
        self.btnSubmitFeedback.setText(QCoreApplication.translate("user_feedback_page", u"Submit Feedback", None))
        self.btnClear.setText(QCoreApplication.translate("user_feedback_page", u"Clear Content", None))
        self.label.setText("")
        self.label_6.setText("")
        self.btnMainButton.setText(QCoreApplication.translate("user_feedback_page", u"Main Page", None))
        self.btnRunTimeSettings.setText(QCoreApplication.translate("user_feedback_page", u"Runtime Setting", None))
        self.btnProfileSettings.setText(QCoreApplication.translate("user_feedback_page", u"Profile Setting", None))
        self.btnFAQ.setText(QCoreApplication.translate("user_feedback_page", u"FAQ", None))
        self.btnLogout.setText(QCoreApplication.translate("user_feedback_page", u"  Log out", None))
        self.btnFeedback.setText(QCoreApplication.translate("user_feedback_page", u"Feedbacks", None))
    # retranslateUi

