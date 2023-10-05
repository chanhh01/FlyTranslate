from PySide6.QtWidgets import QMainWindow, QMessageBox
from python_ui_designs.runtime_setting_page import Ui_runtime_setting_page
from controller import welcome_controller, main_controller, profile_setting_controller, \
    admin_faq_controller, user_faq_controller, admin_feedback_controller, user_feedback_controller
from repository import settings_repo, user_repo, messagebox_repo


class RunTimeController(QMainWindow, Ui_runtime_setting_page):
    crop_bound = (0, 0, 0, 0)

    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Runtime Settings Page")
        self.userId = 0
        self.userRole = 'normal_user'
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.mainPage = None
        self.profileSettingsPage = None
        self.faqPage = None
        self.feedbackPage = None

        self.minimize_upon_login = 0
        self.save_log = 0
        self.text_replacement = 0

        self.btnSaveSettings.clicked.connect(self.save_runtime_configurations)
        self.btnMainButton.clicked.connect(self.to_main_page)
        self.btnProfileSettings.clicked.connect(self.to_profile_page)
        self.btnFAQ.clicked.connect(self.to_faq_page)
        self.btnFeedback.clicked.connect(self.to_feedback_page)
        self.btnLogout.clicked.connect(self.logout_user)
        self.lblUsername.setText("SAMPLEUSERNAME")
        self.minimizeTip = "Minimized operation contains capture image button which is " \
                           "the core operation of this system. If active, you can go straight " \
                           "to minimized page to start translate your screen immediately."
        self.lblTipsMinimized.setToolTip(self.minimizeTip)
        self.replaceTextTip = "If off, translated text will overlay on top of original text. If on," \
                              " the translated text will replace the erased original text."
        self.lblTipsTextReplace.setToolTip(self.replaceTextTip)

    def initialize_page(self):
        isFullScreen, self.save_log, self.text_replacement = \
            settings_repo.retrieve_ocr_related_runtime_settings(self.userId)
        self.minimize_upon_login = settings_repo.check_if_user_checked_minimized_upon_login(self.userId)

        if self.text_replacement == 0:
            self.cbReplaceText.setChecked(False)
        else:
            self.cbReplaceText.setChecked(True)

        if self.save_log == 0:
            self.cbSaveLog.setChecked(False)
        else:
            self.cbSaveLog.setChecked(True)

        if self.minimize_upon_login == 0:
            self.cbMinimizeOnLaunch.setChecked(False)
        else:
            self.cbMinimizeOnLaunch.setChecked(True)

        self.show()

    def save_runtime_configurations(self):
        text_replacement = 0
        save_log = 0
        minimized_upon_login = 0

        if self.cbReplaceText.isChecked():
            text_replacement = 1

        if self.cbSaveLog.isChecked():
            save_log = 1

        if self.cbMinimizeOnLaunch.isChecked():
            minimized_upon_login = 1

        settings_repo.update_runtime_settings(self.userId, text_replacement,
                                              save_log, minimized_upon_login)

    def to_main_page(self):
        self.mainPage = main_controller.MainController()
        self.mainPage.lblUsername.setText(self.lblUsername.text())
        self.mainPage.userRole = self.userRole
        self.mainPage.userId = self.userId
        self.mainPage.initialize_main_page()
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
