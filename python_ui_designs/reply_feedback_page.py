# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reply_feedback_page.ui'
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
from Images_for_design import background_imgs_rc

class Ui_reply_feedback_page(object):
    def setupUi(self, reply_feedback_page):
        if not reply_feedback_page.objectName():
            reply_feedback_page.setObjectName(u"reply_feedback_page")
        reply_feedback_page.resize(677, 590)
        self.centralwidget = QWidget(reply_feedback_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 681, 591))
        self.label_2.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label_2.setScaledContents(True)
        self.txtContent = QTextEdit(self.centralwidget)
        self.txtContent.setObjectName(u"txtContent")
        self.txtContent.setGeometry(QRect(40, 200, 601, 301))
        self.txtTitle = QTextEdit(self.centralwidget)
        self.txtTitle.setObjectName(u"txtTitle")
        self.txtTitle.setGeometry(QRect(40, 120, 601, 31))
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setGeometry(QRect(40, 90, 381, 16))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(11)
        font.setItalic(True)
        self.label_5.setFont(font)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setGeometry(QRect(40, 170, 161, 16))
        self.label_7.setFont(font)
        self.btnSubmitReply = QPushButton(self.centralwidget)
        self.btnSubmitReply.setObjectName(u"btnSubmitReply")
        self.btnSubmitReply.setGeometry(QRect(380, 520, 171, 41))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.btnSubmitReply.setFont(font1)
        self.btnClear = QPushButton(self.centralwidget)
        self.btnClear.setObjectName(u"btnClear")
        self.btnClear.setGeometry(QRect(130, 520, 171, 41))
        self.btnClear.setFont(font1)
        self.lblbtnBack = QLabel(self.centralwidget)
        self.lblbtnBack.setObjectName(u"lblbtnBack")
        self.lblbtnBack.setGeometry(QRect(40, 30, 301, 21))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(14)
        font2.setItalic(True)
        font2.setUnderline(True)
        self.lblbtnBack.setFont(font2)
        self.lblbtnBack.setFrameShape(QFrame.NoFrame)
        self.lblbtnBack.setTextFormat(Qt.PlainText)
        reply_feedback_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(reply_feedback_page)

        QMetaObject.connectSlotsByName(reply_feedback_page)
    # setupUi

    def retranslateUi(self, reply_feedback_page):
        reply_feedback_page.setWindowTitle(QCoreApplication.translate("reply_feedback_page", u"MainWindow", None))
        self.label_2.setText("")
        self.label_5.setText(QCoreApplication.translate("reply_feedback_page", u"Reply title: (no more than 255 characters)", None))
        self.label_7.setText(QCoreApplication.translate("reply_feedback_page", u"Reply Content:", None))
        self.btnSubmitReply.setText(QCoreApplication.translate("reply_feedback_page", u"Submit Reply", None))
        self.btnClear.setText(QCoreApplication.translate("reply_feedback_page", u"Clear Content", None))
        self.lblbtnBack.setText(QCoreApplication.translate("reply_feedback_page", u"<< Back to Feedback Detail", None))
    # retranslateUi

