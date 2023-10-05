from PySide6.QtWidgets import QMainWindow, QMessageBox
from python_ui_designs.user_faq_page import Ui_user_faq_page
from controller import welcome_controller, main_controller, profile_setting_controller, \
     runtime_setting_controller, user_feedback_controller
from repository import faq_repo, user_repo, messagebox_repo


class UserFaqController(QMainWindow, Ui_user_faq_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User FAQ Page")
        self.userId = 0
        self.userRole = 'normal_user'
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.mainPage = None
        self.profileSettingsPage = None
        self.runtimeSettingsPage = None
        self.feedbackPage = None

        self.txtFAQ.setReadOnly(True)
        self.cbbFAQ.currentIndexChanged.connect(self.populate_faq_content)
        self.btnMainButton.clicked.connect(self.to_main_page)
        self.btnRunTimeSettings.clicked.connect(self.to_runtime_page)
        self.btnProfileSettings.clicked.connect(self.to_profile_page)
        self.btnFeedback.clicked.connect(self.to_feedback_page)
        self.btnLogout.clicked.connect(self.logout_user)

    def populate_faq_content(self):
        selected = self.cbbFAQ.currentText()
        faq_id = int(selected.split(" :: ", 1)[0])
        faq_content = faq_repo.retrieve_faq_content_based_on_id(faq_id)
        self.txtFAQ.setPlainText(faq_content)

    def initialize_faq(self):
        faq_lists = faq_repo.retrieve_all_faq_titles()

        if faq_lists is not None:
            self.cbbFAQ.addItems(faq_lists)
            self.cbbFAQ.setCurrentIndex(0)
            self.populate_faq_content()

        self.show()

    def to_main_page(self):
        self.mainPage = main_controller.MainController()
        self.mainPage.lblUsername.setText(self.lblUsername.text())
        self.mainPage.userRole = self.userRole
        self.mainPage.userId = self.userId
        self.mainPage.initialize_main_page()
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

    def to_feedback_page(self):
        self.feedbackPage = user_feedback_controller.UserFeedbackController()
        self.feedbackPage.userId = self.userId
        self.feedbackPage.lblUsername.setText(self.lblUsername.text())
        self.feedbackPage.userRole = self.userRole
        self.feedbackPage.show()
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
