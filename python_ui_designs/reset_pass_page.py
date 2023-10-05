# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'reset_pass_page.ui'
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
from Images_for_design import interactable_image_source_rc
from Images_for_design import background_imgs_rc

class Ui_reset_pass_page(object):
    def setupUi(self, reset_pass_page):
        if not reset_pass_page.objectName():
            reset_pass_page.setObjectName(u"reset_pass_page")
        reset_pass_page.resize(536, 349)
        self.centralwidget = QWidget(reset_pass_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(-10, -280, 571, 881))
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label.setScaledContents(True)
        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setGeometry(QRect(10, 10, 521, 331))
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
        self.lblbtnViewOrHidePass_2 = QLabel(self.centralwidget)
        self.lblbtnViewOrHidePass_2.setObjectName(u"lblbtnViewOrHidePass_2")
        self.lblbtnViewOrHidePass_2.setGeometry(QRect(420, 185, 41, 31))
        self.lblbtnViewOrHidePass_2.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblbtnViewOrHidePass_2.setStyleSheet(u"image: url(:/view/view.png);")
        self.lblbtnViewOrHidePass_2.setFrameShape(QFrame.Panel)
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setGeometry(QRect(80, 190, 131, 16))
        font1 = QFont()
        font1.setPointSize(10)
        font1.setBold(True)
        self.label_3.setFont(font1)
        self.btnBack = QPushButton(self.centralwidget)
        self.btnBack.setObjectName(u"btnBack")
        self.btnBack.setGeometry(QRect(140, 250, 101, 41))
        self.btnBack.setFont(font1)
        self.btnConfirmReset = QPushButton(self.centralwidget)
        self.btnConfirmReset.setObjectName(u"btnConfirmReset")
        self.btnConfirmReset.setGeometry(QRect(300, 250, 101, 41))
        self.btnConfirmReset.setFont(font1)
        self.lblbtnViewOrHidePass = QLabel(self.centralwidget)
        self.lblbtnViewOrHidePass.setObjectName(u"lblbtnViewOrHidePass")
        self.lblbtnViewOrHidePass.setGeometry(QRect(420, 130, 41, 31))
        self.lblbtnViewOrHidePass.setCursor(QCursor(Qt.PointingHandCursor))
        self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")
        self.lblbtnViewOrHidePass.setFrameShape(QFrame.Panel)
        self.txtOldPass = QLineEdit(self.centralwidget)
        self.txtOldPass.setObjectName(u"txtOldPass")
        self.txtOldPass.setGeometry(QRect(230, 130, 190, 31))
        self.txtOldPass.setEchoMode(QLineEdit.Password)
        self.txtNewPass = QLineEdit(self.centralwidget)
        self.txtNewPass.setObjectName(u"txtNewPass")
        self.txtNewPass.setGeometry(QRect(230, 185, 190, 31))
        self.txtNewPass.setEchoMode(QLineEdit.Password)
        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setGeometry(QRect(80, 140, 131, 16))
        self.label_2.setFont(font1)
        reset_pass_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(reset_pass_page)

        QMetaObject.connectSlotsByName(reset_pass_page)
    # setupUi

    def retranslateUi(self, reset_pass_page):
        reset_pass_page.setWindowTitle(QCoreApplication.translate("reset_pass_page", u"MainWindow", None))
        self.label.setText("")
        self.label_4.setText(QCoreApplication.translate("reset_pass_page", u"Reset Password", None))
        self.lblbtnViewOrHidePass_2.setText("")
        self.label_3.setText(QCoreApplication.translate("reset_pass_page", u"New Password:", None))
        self.btnBack.setText(QCoreApplication.translate("reset_pass_page", u"Back", None))
        self.btnConfirmReset.setText(QCoreApplication.translate("reset_pass_page", u"Reset", None))
        self.lblbtnViewOrHidePass.setText("")
        self.label_2.setText(QCoreApplication.translate("reset_pass_page", u"Old Password:", None))
    # retranslateUi

