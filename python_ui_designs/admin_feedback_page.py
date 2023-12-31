# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'admin_feedback_page.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QApplication, QFrame, QHeaderView,
    QLabel, QMainWindow, QPushButton, QSizePolicy,
    QTableWidget, QTableWidgetItem, QWidget)
from Images_for_design import static_img_rc
from Images_for_design import background_imgs_rc

class Ui_admin_feedback_page(object):
    def setupUi(self, admin_feedback_page):
        if not admin_feedback_page.objectName():
            admin_feedback_page.setObjectName(u"admin_feedback_page")
        admin_feedback_page.resize(794, 586)
        self.centralwidget = QWidget(admin_feedback_page)
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
        self.btnRunTimeSettings.setChecked(False)
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
        self.btnFeedback.setChecked(True)
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
        self.tbFeedbackList = QTableWidget(self.frame_2)
        self.tbFeedbackList.setObjectName(u"tbFeedbackList")
        self.tbFeedbackList.setGeometry(QRect(20, 120, 611, 191))
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.tbFeedbackList.sizePolicy().hasHeightForWidth())
        self.tbFeedbackList.setSizePolicy(sizePolicy)
        self.tbFeedbackList.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_7 = QLabel(self.frame_2)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(20, 90, 161, 16))
        self.label_7.setFont(font1)
        self.tbArchivedFeedback = QTableWidget(self.frame_2)
        self.tbArchivedFeedback.setObjectName(u"tbArchivedFeedback")
        self.tbArchivedFeedback.setGeometry(QRect(20, 360, 611, 211))
        sizePolicy.setHeightForWidth(self.tbArchivedFeedback.sizePolicy().hasHeightForWidth())
        self.tbArchivedFeedback.setSizePolicy(sizePolicy)
        self.tbArchivedFeedback.setEditTriggers(QAbstractItemView.NoEditTriggers)
        self.label_8 = QLabel(self.frame_2)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setGeometry(QRect(20, 330, 191, 16))
        self.label_8.setFont(font1)
        self.label_2.raise_()
        self.label_4.raise_()
        self.lblUsername.raise_()
        self.tbFeedbackList.raise_()
        self.label_7.raise_()
        self.tbArchivedFeedback.raise_()
        self.label_8.raise_()
        admin_feedback_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(admin_feedback_page)

        QMetaObject.connectSlotsByName(admin_feedback_page)
    # setupUi

    def retranslateUi(self, admin_feedback_page):
        admin_feedback_page.setWindowTitle(QCoreApplication.translate("admin_feedback_page", u"MainWindow", None))
        self.label.setText("")
        self.label_6.setText("")
        self.btnMainButton.setText(QCoreApplication.translate("admin_feedback_page", u"Main Page", None))
        self.btnRunTimeSettings.setText(QCoreApplication.translate("admin_feedback_page", u"Runtime Setting", None))
        self.btnProfileSettings.setText(QCoreApplication.translate("admin_feedback_page", u"Profile Setting", None))
        self.btnFAQ.setText(QCoreApplication.translate("admin_feedback_page", u"FAQ", None))
        self.btnLogout.setText(QCoreApplication.translate("admin_feedback_page", u"  Log out", None))
        self.btnFeedback.setText(QCoreApplication.translate("admin_feedback_page", u"Feedbacks", None))
        self.label_4.setText(QCoreApplication.translate("admin_feedback_page", u"Welcome Back,", None))
        self.lblUsername.setText(QCoreApplication.translate("admin_feedback_page", u"SAMPLEUSERNAME!!", None))
        self.label_2.setText("")
        self.label_7.setText(QCoreApplication.translate("admin_feedback_page", u"New Feedbacks:", None))
        self.label_8.setText(QCoreApplication.translate("admin_feedback_page", u"Archived feedbacks:", None))
    # retranslateUi

