from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.main_page import Ui_main_page
from controller import welcome_controller, minimized_operation_controller, \
    runtime_setting_controller, profile_setting_controller, admin_faq_controller, \
    user_faq_controller, admin_feedback_controller, user_feedback_controller
from repository import settings_repo, user_repo, messagebox_repo
from python_ui_designs import snipping_tool
from PIL import ImageGrab
import cv2
import numpy as np


class MainController(QMainWindow, Ui_main_page):
    crop_bound = (0, 0, 0, 0)

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Main Page")
        self.userId = 0
        self.userRole = 'normal_user'
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.runtimeSettingsPage = None
        self.profileSettingsPage = None
        self.faqPage = None
        self.feedbackPage = None
        self.minimizedPage = None

        self.isFullScreen = 0
        self.source_lang_name = None
        self.target_lang_name = None
        self.lblUsername.setText("SAMPLEUSERNAME")
        self.btnCropImage.clicked.connect(self.edit_crop_area)
        self.btnTestOutputImageSize.clicked.connect(self.preview_cropped_image)
        self.btnSaveConfig.clicked.connect(self.save_current_configuration)
        self.btnMinimize.clicked.connect(self.navigate_to_minimized_operation_page)
        self.btnRunTimeSettings.clicked.connect(self.to_runtime_page)
        self.btnProfileSettings.clicked.connect(self.to_profile_page)
        self.btnFAQ.clicked.connect(self.to_faq_page)
        self.btnFeedback.clicked.connect(self.to_feedback_page)
        self.lblbtnSwapLanguage.mousePressEvent = self.swap_source_and_target_language
        self.btnLogout.clicked.connect(self.logout_user)
        self.scanToolTip = "The crop area you drawn after turning off scan full screen will be used. " \
                           "Else, the system will still scan the entire screen. You may cancel the scan by hitting " \
                           "Esc key."
        self.langToolTip = "Source and target language can be swapped if you click on the icon between " \
                           "source and target language. Source language will not be considered if the " \
                           "setting 'Auto detect source language' is active."
        self.lblTipsScan.setToolTip(self.scanToolTip)
        self.lblTipsLang.setToolTip(self.langToolTip)
        self.snippingTool = snipping_tool.Snipping_tool(self)

    def edit_crop_area(self):
        self.close()
        self.snippingTool.start()

    def initialize_main_page(self):
        self.initialize_language_combobox()
        self.initialize_user_settings()
        self.show()

    def initialize_language_combobox(self):
        lang_list = settings_repo.retrieve_current_available_languages()

        if lang_list is not None:
            self.cbbSource.addItems(lang_list)
            self.cbbTarget.addItems(lang_list)

    def initialize_user_settings(self):
        self.isFullScreen, save_log, text_replacement = \
            settings_repo.retrieve_ocr_related_runtime_settings(self.userId)
        source_lang_id, target_lang_id = settings_repo.retrieve_user_source_and_target_language(self.userId)

        self.crop_bound = settings_repo.retrieve_user_crop_area(self.userId)

        if self.isFullScreen == 0:
            self.cbToggleScanFullScreen.setChecked(False)
        elif self.isFullScreen == 1:
            self.cbToggleScanFullScreen.setChecked(True)

        if source_lang_id is not None and target_lang_id is not None:
            self.source_lang_name = settings_repo.retrieve_lang_name_by_lang_id(source_lang_id)
            self.target_lang_name = settings_repo.retrieve_lang_name_by_lang_id(target_lang_id)

            if self.source_lang_name is not None and self.target_lang_name is not None:
                self.cbbSource.setCurrentText(self.source_lang_name)
                self.cbbTarget.setCurrentText(self.target_lang_name)

    def swap_source_and_target_language(self, event):
        if event.button() == Qt.LeftButton:
            temp_target = self.cbbSource.currentText()
            temp_source = self.cbbTarget.currentText()

            self.cbbSource.setCurrentText(temp_source)
            self.cbbTarget.setCurrentText(temp_target)

    def save_current_configuration(self):
        if self.cbToggleScanFullScreen.isChecked():
            self.isFullScreen = 1
        else:
            self.isFullScreen = 0

        update_crop_res = settings_repo.update_crop_area(self.userId, self.crop_bound)

        if update_crop_res:
            source_lang_name = self.cbbSource.currentText()
            target_lang_name = self.cbbTarget.currentText()

            if source_lang_name == target_lang_name:
                messagebox_repo.messagebox("Language selection error.",
                                         "Source and target language cannot be the same.", "warning", "ok")
            else:
                update_full_screen_res = settings_repo.update_full_screen_status(self.userId, self.isFullScreen)
                update_language_res = settings_repo.update_user_language(self.userId,
                                                                         source_lang_name, target_lang_name)

                if update_full_screen_res and update_language_res:
                    self.initialize_user_settings()
                    messagebox_repo.messagebox("Successful",
                                             "Current configuration saved successfully.", "info", "ok")

    def preview_cropped_image(self):
        if self.cbToggleScanFullScreen.isChecked():
            full_screen_crop = (0, 0, 1920, 1080)
            img = ImageGrab.grab(bbox=full_screen_crop)
            img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)
            cv2.namedWindow("Preview Display", cv2.WINDOW_NORMAL)
            cv2.imshow('Preview Display', img)
            cv2.waitKey(0)

            cv2.destroyAllWindows()
        else:
            if isinstance(self.crop_bound, tuple):
                if self.crop_bound[0] - self.crop_bound[2] != 0 and self.crop_bound[1] - self.crop_bound[3] != 0:
                    cv_win_width = self.crop_bound[2] - self.crop_bound[0]
                    cv_win_height = self.crop_bound[3] - self.crop_bound[1]

                    img = ImageGrab.grab(bbox=self.crop_bound)
                    img = cv2.cvtColor(np.array(img), cv2.COLOR_BGR2RGB)

                    cv2.namedWindow("Preview Display", cv2.WINDOW_NORMAL)
                    cv2.resizeWindow("Preview Display", int(cv_win_width), int(cv_win_height))
                    cv2.imshow('Preview Display', img)

                    cv2.waitKey(0)

                    cv2.destroyAllWindows()
                else:
                    messagebox_repo.messagebox("Preview Crop Display Error",
                                             "Crop area is empty, crop and area and save first!", "warning", "ok")
            else:
                messagebox_repo.messagebox("Preview Crop Display Error",
                                         "Crop area is invalid, please report this to admin!", "warning", "ok")

    def navigate_to_minimized_operation_page(self):
        self.minimizedPage = minimized_operation_controller.MinimizedController()
        self.minimizedPage.mainPage = self
        self.minimizedPage.userId = self.userId
        self.minimizedPage.userRole = self.userRole
        self.minimizedPage.username = self.lblUsername.text()
        self.minimizedPage.initialize_settings()
        self.close()

    def to_runtime_page(self):
        self.runtimeSettingsPage = runtime_setting_controller.RunTimeController()
        self.runtimeSettingsPage.userId = self.userId
        self.runtimeSettingsPage.lblUsername.setText(self.lblUsername.text())
        self.runtimeSettingsPage.userRole = self.userRole
        self.runtimeSettingsPage.initialize_page()
        self.close()

    def to_profile_page(self):
        email = user_repo.retrieve_email_by_user_id(self.userId)
        username = user_repo.retrieve_username_by_userid(self.userId)
        self.profileSettingsPage = profile_setting_controller.ProfileSettingController()
        self.profileSettingsPage.userId = self.userId
        self.profileSettingsPage.email = email
        self.profileSettingsPage.username = username
        self.profileSettingsPage.lblUsername.setText(self.lblUsername.text())
        self.profileSettingsPage.txtEmail.setText(email)
        self.profileSettingsPage.txtUsername.setText(username)
        self.profileSettingsPage.userRole = self.userRole
        self.profileSettingsPage.show()
        self.close()

    def to_faq_page(self):
        if self.userRole == "admin":
            self.faqPage = admin_faq_controller.AdminFaqController()
        else:
            self.faqPage = user_faq_controller.UserFaqController()

        self.faqPage.userId = self.userId
        self.faqPage.lblUsername.setText(self.lblUsername.text())
        self.faqPage.userRole = self.userRole
        self.faqPage.initialize_faq()
        self.close()

    def to_feedback_page(self):
        if self.userRole == "admin":
            self.feedbackPage = admin_feedback_controller.AdminFeedbackController()
        else:
            self.feedbackPage = user_feedback_controller.UserFeedbackController()

        self.feedbackPage.userId = self.userId
        self.feedbackPage.lblUsername.setText(self.lblUsername.text())
        self.feedbackPage.userRole = self.userRole
        self.feedbackPage.initialize_feedback_page()
        self.close()

    def logout_user(self):
        msg = "Are you sure you want to log out? If remember device " \
              "session is active then logging out will remove session."

        result = messagebox_repo.messagebox("Logout?", msg, "question", "yesno")

        if result == QMessageBox.Yes:
            session_exists, user_id = user_repo.check_for_session()

            # if session exists, delete session
            if session_exists:
                user_repo.remove_session()

            self.welcomePage = welcome_controller.WelcomeController()
            self.welcomePage.show()
            self.close()
