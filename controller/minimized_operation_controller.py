from PySide6.QtWidgets import QMainWindow
from PySide6.QtCore import Qt
from python_ui_designs.minimized_operation_page import Ui_minimized_operation_page
from controller import main_controller
from repository import settings_repo, easyocr_repo, messagebox_repo
from PIL import ImageGrab
import cv2
import os
import numpy as np
import threading
import subprocess


class MinimizedController(QMainWindow, Ui_minimized_operation_page):
    crop_bound = (0, 0, 0, 0)

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)
        self.userId = 0
        self.userRole = 'normal_user'
        self.setWindowTitle(".")
        self.username = "SAMPLEUSERNAME"
        self.mainPage = None

        self.stop_threads = False
        self.paragraph = False
        self.threadedLoop = None

        self.isFullScreen = 0
        self.save_log = 0
        self.text_replacement = 0

        self.source_lang_code = 'en'
        self.target_lang_code = None

        self.btnMaximizeWin.clicked.connect(self.quit_minimize)
        self.btnMaximizeWin.setToolTip("Click this button to return to main page.")

        self.btnCaptureImage.clicked.connect(self.scan_image)
        self.captureImgTips = "Click this button to scan and translate text on screen. " \
                              "It may take a little while, please be patient."
        self.btnCaptureImage.setToolTip(self.captureImgTips)

        self.btnStopCapture.clicked.connect(self.end_loop)
        self.btnStopCapture.setToolTip("Click this button to kill the display window and stop scanning.")

        self.lblbtnDecrement.mousePressEvent = self.decrement_font_size
        self.lblbtnDecrement.setToolTip("-1 font size. Minimum is 1")

        self.lblbtnIncrement.mousePressEvent = self.increment_font_size
        self.lblbtnIncrement.setToolTip("+1 font size. Maximum is 50.")

        self.btnSetParagraph.clicked.connect(self.set_sentence_or_paragraph)
        self.paragraphTip = "Seeing this means the program will extract the text by sentence/phrase instead of paragraph." \
                            "Click on this button to change to extract entire paragraph instead."
        self.btnSetParagraph.setToolTip(self.paragraphTip)

        self.btnCheckLog.clicked.connect(self.open_log_directory)
        self.btnCheckLog.setToolTip("Click this to open the log directory in your explorer.")

        self.txtFontSize.setText("25")
        self.txtFontSize.setReadOnly(True)

    def quit_minimize(self):
        if self.mainPage is None:
            self.mainPage = main_controller.MainController()
            self.mainPage.userId = self.userId
            self.mainPage.userRole = self.userRole
            self.mainPage.lblUsername.setText(self.username)
            self.mainPage.initialize_main_page()
            self.close()
        else:
            self.mainPage.show()
            self.close()

    def initialize_settings(self):
        source_lang_id, target_lang_id = settings_repo.retrieve_user_source_and_target_language(self.userId)
        self.isFullScreen, self.save_log, self.text_replacement = \
            settings_repo.retrieve_ocr_related_runtime_settings(self.userId)

        if source_lang_id is not None and target_lang_id is not None:
            self.source_lang_code = 'en'
            self.target_lang_code = settings_repo.retrieve_lang_code_by_lang_id(target_lang_id)
            self.source_lang_code = settings_repo.retrieve_lang_code_by_lang_id(source_lang_id)

            easyocr_repo.initialize_OCR_Reader(self.source_lang_code)

            self.crop_bound = settings_repo.retrieve_user_crop_area(self.userId)
            self.show()
            self.move(0, 0)
        else:
            self.quit_minimize()

    def set_sentence_or_paragraph(self):
        if self.btnSetParagraph.styleSheet() == u"image: url(:/horizontal/menu.png);":
            self.paragraph = False
            self.btnSetParagraph.setStyleSheet(u"image: url(:/individual sentence/text-font.png);")
            tooltip = "Seeing this means the program will extract the text by sentence/phrase instead of paragraph." \
                      "Click on this button to change to extract entire paragraph instead."
            self.btnSetParagraph.setToolTip(tooltip)

        elif self.btnSetParagraph.styleSheet() == u"image: url(:/individual sentence/text-font.png);":
            self.paragraph = True
            tooltip = "Seeing this means the program will extract the text by paragraph instead of sentence/phrase." \
                      "Click on this button to change to extract sentence or phrase instead."
            self.btnSetParagraph.setStyleSheet(u"image: url(:/horizontal/menu.png);")
            self.btnSetParagraph.setToolTip(tooltip)

    def change_status(self, status):
        if status == 'pending':
            self.lblStatus.setStyleSheet(u"image: url(:/pending/work-in-progress.png);")
            tip = "Your result is pending, you can freely navigate on your screen and wait for the result"
            self.lblStatus.setToolTip(tip)
        elif status == 'idle':
            self.lblStatus.setStyleSheet(u"image: url(:/completed/checked.png);")
            tip = "FlyTranslate is idling / Scan and translate process is completed."
            self.lblStatus.setToolTip(tip)

    def open_log_directory(self):
        parent_path = os.getcwd()
        folder_path = os.path.abspath(os.path.join(parent_path, 'log_files'))

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        subprocess.Popen(['explorer.exe', folder_path])

    def increment_font_size(self, event):
        if event.button() == Qt.LeftButton:
            font_size = int(self.txtFontSize.text())
            font_size += 1

            if font_size <= 50:
                self.txtFontSize.setText(str(font_size))

    def decrement_font_size(self, event):
        if event.button() == Qt.LeftButton:
            font_size = int(self.txtFontSize.text())
            font_size -= 1

            if font_size > 0:
                self.txtFontSize.setText(str(font_size))

    def end_loop(self):
        self.stop_threads = True
        if self.threadedLoop is not None:
            self.threadedLoop.join()
        self.btnStopCapture.setEnabled(False)
        self.btnMaximizeWin.setEnabled(True)

    def background_OCR(self, stop):
        font_size = int(self.txtFontSize.text())
        if self.isFullScreen == 1:
            full_screen_crop = (0, 0, 1920, 1080)
            img = ImageGrab.grab(bbox=full_screen_crop)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

            res = img
            self.change_status('pending')

            try:
                if self.text_replacement == 0:
                    res = easyocr_repo.startOCR(img, self.source_lang_code, self.target_lang_code,
                                                'overlay', font_size, self.save_log, self.paragraph)
                elif self.text_replacement == 1:
                    res = easyocr_repo.startOCR(img, self.source_lang_code, self.target_lang_code,
                                                'rewrite', font_size, self.save_log, self.paragraph)
            except Exception as e:
                messagebox_repo.messagebox("Error", f"{e}", "warning", "ok")

            self.change_status('idle')

            while True:

                if stop():
                    break

                cv2.namedWindow("final_result", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("final_result", 1920, 1080)
                cv2.imshow('final_result', res)
                cv2.waitKey(250)

            cv2.destroyAllWindows()
        else:
            img = ImageGrab.grab(bbox=self.crop_bound)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

            res = img
            self.change_status('pending')

            try:
                if self.text_replacement == 0:
                    res = easyocr_repo.startOCR(img, self.source_lang_code, self.target_lang_code,
                                                'overlay', font_size, self.save_log, self.paragraph)
                elif self.text_replacement == 1:
                    res = easyocr_repo.startOCR(img, self.source_lang_code, self.target_lang_code,
                                                'rewrite', font_size, self.save_log, self.paragraph)
            except Exception as e:
                messagebox_repo.messagebox("Error", f"{e}", "warning", "ok")

            cv_win_width = self.crop_bound[2] - self.crop_bound[0]
            cv_win_height = self.crop_bound[3] - self.crop_bound[1]

            self.change_status('idle')

            while True:

                if stop():
                    break

                cv2.namedWindow("final_result", cv2.WINDOW_NORMAL)
                cv2.resizeWindow("final_result", int(cv_win_width), int(cv_win_height))
                cv2.imshow('final_result', res)
                cv2.waitKey(250)

            cv2.destroyAllWindows()

    def start_thread(self):
        self.threadedLoop = threading.Thread(name='background',
                                             target=self.background_OCR,
                                             args=(lambda: self.stop_threads,))
        self.stop_threads = False
        self.btnStopCapture.setEnabled(True)
        self.btnMaximizeWin.setEnabled(False)
        self.threadedLoop.start()

    def scan_image(self):
        if not self.stop_threads:
            self.end_loop()

        if self.isFullScreen == 1:
            self.start_thread()
        else:
            if isinstance(self.crop_bound, tuple):
                if self.crop_bound[0] - self.crop_bound[2] != 0 and self.crop_bound[1] - self.crop_bound[3] != 0:
                    self.start_thread()
                else:
                    messagebox_repo.messagebox("Capture Image Error",
                                               "Crop area is empty, crop an area first or turn on full screen scan!",
                                               "warning", "ok")
            else:
                messagebox_repo.messagebox("Capture Image Error",
                                           "Something went wrong, please report this to admin!", "warning", "ok")
