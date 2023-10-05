import tkinter as tk

from PySide6.QtCore import Qt
from PySide6 import QtWidgets, QtCore, QtGui


class Snipping_tool(QtWidgets.QWidget):
    is_snipping = False
    background = True

    def __init__(self, parent):
        super().__init__()
        self.main_page = parent
        self.setWindowFlags(Qt.FramelessWindowHint)

        root = tk.Tk()
        screen_width = root.winfo_screenwidth()
        screen_height = root.winfo_screenheight()
        self.setGeometry(0, 0, screen_width, screen_height)

        # ^^ the above code is done to prevent the crop window from not
        # showing full screen on second crop attempts and onwards.
        # Set geometry ensures the crop window is always shown full screen

        self.begin = QtCore.QPoint()
        self.end = QtCore.QPoint()

    def start(self):
        self.setWindowFlags(Qt.FramelessWindowHint)
        Snipping_tool.background = False
        Snipping_tool.is_snipping = True
        self.setWindowOpacity(0.3)
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CursorShape.CrossCursor))
        print('Capture the screen...')
        print('Press esc key if you want to quit...')
        self.showFullScreen()

    def paintEvent(self, event):
        if Snipping_tool.is_snipping:
            brush_color = (128, 128, 255, 100)
            lw = 3
            opacity = 0.3
        else:
            # reset points, so the rectangle won't show up again.
            self.begin = QtCore.QPoint()
            self.end = QtCore.QPoint()
            brush_color = (0, 0, 0, 0)
            lw = 0
            opacity = 0

        self.setWindowOpacity(opacity)
        qp = QtGui.QPainter(self)
        qp.setPen(QtGui.QPen(QtGui.QColor('black'), lw))
        # *brush_color is used to unpack the brush color tuple to be passed into QtGUI.QColor()
        qp.setBrush(QtGui.QColor(*brush_color))
        rect = QtCore.QRectF(self.begin, self.end)
        qp.drawRect(rect)

    def keyPressEvent(self, event):
        if event.key() == QtCore.Qt.Key_Escape:
            self.close()
            event.accept()
            QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
            self.main_page.show()

    def mousePressEvent(self, event):
        self.begin = event.pos()
        self.end = self.begin
        self.update()

    def mouseMoveEvent(self, event):
        self.end = event.pos()
        self.update()

    def mouseReleaseEvent(self, event):
        Snipping_tool.is_snipping = False
        QtWidgets.QApplication.restoreOverrideCursor()
        x1 = min(self.begin.x(), self.end.x())*1.25
        y1 = min(self.begin.y(), self.end.y())*1.25
        x2 = max(self.begin.x(), self.end.x())*1.25
        y2 = max(self.begin.y(), self.end.y())*1.25

        # ^^ the reason why it is multiplied by 1.25 is because this device scaled display at 125%.

        self.repaint()
        QtWidgets.QApplication.setOverrideCursor(QtGui.QCursor(QtCore.Qt.CursorShape.ArrowCursor))
        QtWidgets.QApplication.processEvents()  # update bounding box in paint event

        print("x1: " + str(x1) +
              " y1: " + str(y1) +
              " x2: " + str(x2) +
              " y2: " + str(y2))

        self.main_page.crop_bound = (x1, y1, x2, y2)
        self.main_page.show()
        self.close()
