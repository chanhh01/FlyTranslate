# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'feedback_detail.ui'
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
from PySide6.QtWidgets import (QApplication, QFrame, QLabel, QPushButton,
    QSizePolicy, QTextEdit, QWidget)
from Images_for_design import background_imgs_rc

class Ui_feedback_details(object):
    def setupUi(self, feedback_details):
        if not feedback_details.objectName():
            feedback_details.setObjectName(u"feedback_details")
        feedback_details.resize(575, 531)
        self.label_2 = QLabel(feedback_details)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(0, 0, 581, 531))
        self.label_2.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label_2.setScaledContents(True)
        self.lblbtnBack = QLabel(feedback_details)
        self.lblbtnBack.setObjectName(u"lblbtnBack")
        self.lblbtnBack.setGeometry(QRect(20, 30, 241, 21))
        font = QFont()
        font.setFamilies([u"Rockwell"])
        font.setPointSize(14)
        font.setItalic(True)
        font.setUnderline(True)
        self.lblbtnBack.setFont(font)
        self.lblbtnBack.setFrameShape(QFrame.NoFrame)
        self.lblbtnBack.setTextFormat(Qt.PlainText)
        self.lblFeedbackUser = QLabel(feedback_details)
        self.lblFeedbackUser.setObjectName(u"lblFeedbackUser")
        self.lblFeedbackUser.setGeometry(QRect(30, 130, 471, 16))
        font1 = QFont()
        font1.setFamilies([u"Rockwell"])
        font1.setPointSize(11)
        font1.setItalic(True)
        self.lblFeedbackUser.setFont(font1)
        self.lblTitle = QLabel(feedback_details)
        self.lblTitle.setObjectName(u"lblTitle")
        self.lblTitle.setGeometry(QRect(30, 70, 511, 51))
        font2 = QFont()
        font2.setFamilies([u"Rockwell"])
        font2.setPointSize(12)
        font2.setBold(True)
        font2.setItalic(False)
        font2.setUnderline(False)
        self.lblTitle.setFont(font2)
        self.lblTitle.setWordWrap(True)
        self.txtContent = QTextEdit(feedback_details)
        self.txtContent.setObjectName(u"txtContent")
        self.txtContent.setGeometry(QRect(30, 160, 521, 301))
        self.txtContent.setReadOnly(True)
        self.btnReply = QPushButton(feedback_details)
        self.btnReply.setObjectName(u"btnReply")
        self.btnReply.setGeometry(QRect(410, 480, 141, 41))
        font3 = QFont()
        font3.setPointSize(9)
        font3.setBold(True)
        self.btnReply.setFont(font3)
        self.btnArchive = QPushButton(feedback_details)
        self.btnArchive.setObjectName(u"btnArchive")
        self.btnArchive.setGeometry(QRect(30, 480, 181, 41))
        self.btnArchive.setFont(font3)
        self.btnUnarchive = QPushButton(feedback_details)
        self.btnUnarchive.setObjectName(u"btnUnarchive")
        self.btnUnarchive.setGeometry(QRect(220, 480, 181, 41))
        self.btnUnarchive.setFont(font3)

        self.retranslateUi(feedback_details)

        QMetaObject.connectSlotsByName(feedback_details)
    # setupUi

    def retranslateUi(self, feedback_details):
        feedback_details.setWindowTitle(QCoreApplication.translate("feedback_details", u"Form", None))
        self.label_2.setText("")
        self.lblbtnBack.setText(QCoreApplication.translate("feedback_details", u"<< Back to Feedbacks", None))
        self.lblFeedbackUser.setText(QCoreApplication.translate("feedback_details", u"By: sampleusername", None))
        self.lblTitle.setText(QCoreApplication.translate("feedback_details", u"<html><head/><body><p>sample title sample titlesample title sample title sample title sample title sample title sample title sample title sample title sample title sample title sample title sample title</p></body></html>", None))
        self.txtContent.setHtml(QCoreApplication.translate("feedback_details", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:7.8pt; font-weight:400; font-style:normal;\">\n"
"<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p></body></html>", None))
        self.btnReply.setText(QCoreApplication.translate("feedback_details", u"Reply Feedback", None))
        self.btnArchive.setText(QCoreApplication.translate("feedback_details", u"Archive without reply", None))
        self.btnUnarchive.setText(QCoreApplication.translate("feedback_details", u"Unarchive feedback", None))
    # retranslateUi

