# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'minimized_operation_page.ui'
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
from Images_for_design import static_img_rc
from Images_for_design import interactable_image_source_rc

class Ui_minimized_operation_page(object):
    def setupUi(self, minimized_operation_page):
        if not minimized_operation_page.objectName():
            minimized_operation_page.setObjectName(u"minimized_operation_page")
        minimized_operation_page.resize(262, 97)
        self.centralwidget = QWidget(minimized_operation_page)
        self.centralwidget.setObjectName(u"centralwidget")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setGeometry(QRect(0, -90, 461, 191))
        self.label.setAutoFillBackground(False)
        self.label.setStyleSheet(u"background-image: url(:/backgournds/FlyTranslate-logo/background_image.png);")
        self.label.setScaledContents(True)
        self.btnCaptureImage = QPushButton(self.centralwidget)
        self.btnCaptureImage.setObjectName(u"btnCaptureImage")
        self.btnCaptureImage.setGeometry(QRect(5, 5, 51, 41))
        font = QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.btnCaptureImage.setFont(font)
        self.btnCaptureImage.setStyleSheet(u"image: url(:/capture/screenshot.png);")
        self.btnStopCapture = QPushButton(self.centralwidget)
        self.btnStopCapture.setObjectName(u"btnStopCapture")
        self.btnStopCapture.setGeometry(QRect(60, 5, 51, 41))
        self.btnStopCapture.setFont(font)
        self.btnStopCapture.setStyleSheet(u"image: url(:/stop_capture/no-stopping.png);")
        self.btnMaximizeWin = QPushButton(self.centralwidget)
        self.btnMaximizeWin.setObjectName(u"btnMaximizeWin")
        self.btnMaximizeWin.setGeometry(QRect(60, 50, 51, 41))
        self.btnMaximizeWin.setFont(font)
        self.btnMaximizeWin.setStyleSheet(u"image: url(:/maximize/maximize.png);")
        self.txtFontSize = QLineEdit(self.centralwidget)
        self.txtFontSize.setObjectName(u"txtFontSize")
        self.txtFontSize.setGeometry(QRect(159, 10, 51, 31))
        font1 = QFont()
        font1.setPointSize(11)
        font1.setBold(True)
        self.txtFontSize.setFont(font1)
        self.txtFontSize.setAlignment(Qt.AlignCenter)
        self.lblbtnIncrement = QLabel(self.centralwidget)
        self.lblbtnIncrement.setObjectName(u"lblbtnIncrement")
        self.lblbtnIncrement.setGeometry(QRect(210, 10, 41, 31))
        self.lblbtnIncrement.setStyleSheet(u"image: url(:/increment/plus.png);")
        self.lblbtnIncrement.setFrameShape(QFrame.Box)
        self.lblbtnDecrement = QLabel(self.centralwidget)
        self.lblbtnDecrement.setObjectName(u"lblbtnDecrement")
        self.lblbtnDecrement.setGeometry(QRect(119, 10, 41, 31))
        self.lblbtnDecrement.setStyleSheet(u"image: url(:/decrement/minus-sign.png);")
        self.lblbtnDecrement.setFrameShape(QFrame.Box)
        self.btnSetParagraph = QPushButton(self.centralwidget)
        self.btnSetParagraph.setObjectName(u"btnSetParagraph")
        self.btnSetParagraph.setGeometry(QRect(3, 50, 51, 41))
        self.btnSetParagraph.setFont(font)
        self.btnSetParagraph.setStyleSheet(u"image: url(:/individual sentence/text-font.png);")
        self.btnSetParagraph.setCheckable(True)
        self.btnCheckLog = QPushButton(self.centralwidget)
        self.btnCheckLog.setObjectName(u"btnCheckLog")
        self.btnCheckLog.setGeometry(QRect(118, 50, 51, 41))
        self.btnCheckLog.setFont(font)
        self.btnCheckLog.setStyleSheet(u"image: url(:/log/log.png);")
        self.lblStatus = QLabel(self.centralwidget)
        self.lblStatus.setObjectName(u"lblStatus")
        self.lblStatus.setGeometry(QRect(200, 50, 51, 41))
        self.lblStatus.setStyleSheet(u"image: url(:/completed/checked.png);")
        minimized_operation_page.setCentralWidget(self.centralwidget)

        self.retranslateUi(minimized_operation_page)

        QMetaObject.connectSlotsByName(minimized_operation_page)
    # setupUi

    def retranslateUi(self, minimized_operation_page):
        minimized_operation_page.setWindowTitle(QCoreApplication.translate("minimized_operation_page", u"MainWindow", None))
        self.label.setText("")
        self.btnCaptureImage.setText("")
        self.btnStopCapture.setText("")
        self.btnMaximizeWin.setText("")
        self.txtFontSize.setText("")
        self.lblbtnIncrement.setText("")
        self.lblbtnDecrement.setText("")
        self.btnSetParagraph.setText("")
        self.btnCheckLog.setText("")
        self.lblStatus.setText("")
    # retranslateUi

