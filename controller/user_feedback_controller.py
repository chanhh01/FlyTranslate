from PySide6.QtWidgets import QMainWindow, QMessageBox
from python_ui_designs.user_feedback_page import Ui_user_feedback_page
from controller import welcome_controller, main_controller, runtime_setting_controller, \
    profile_setting_controller, user_faq_controller
from repository import feedback_repo, user_repo, messagebox_repo


class UserFeedbackController(QMainWindow, Ui_user_feedback_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("User Feedback Page")
        self.userId = 0
        self.userRole = 'normal_user'
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.mainPage = None
        self.profileSettingsPage = None
        self.faqPage = None
        self.runtimeSettingsPage = None
        self.feedbackDetail = None

        self.btnMainButton.clicked.connect(self.to_main_page)
        self.btnRunTimeSettings.clicked.connect(self.to_runtime_page)
        self.btnProfileSettings.clicked.connect(self.to_profile_page)
        self.btnFAQ.clicked.connect(self.to_faq_page)
        self.btnLogout.clicked.connect(self.logout_user)
        self.btnSubmitFeedback.clicked.connect(self.submit_feedback)
        self.btnClear.clicked.connect(self.clear_contents)

    def clear_contents(self):
        self.txtContent.clear()
        self.txtTitle.clear()

    def initialize_feedback_page(self):
        self.show()

    def submit_feedback(self):
        title = self.txtTitle.toPlainText()
        content = self.txtContent.toPlainText()

        if title.strip() != "" and content.strip() != "":
            if len(title) <= 255:
                result = messagebox_repo.messagebox("Wait!", "Are you sure you want to submit this feedback?", "question", "yesno")

                if result == QMessageBox.Yes:
                    res = feedback_repo.add_new_feedback(self.userId, title, content)

                    if res:
                        self.clear_contents()
            else:
                messagebox_repo.messagebox("Error!", "Title cannot be more than 255 characters!", "warning", "ok")
        else:
            messagebox_repo.messagebox("Error!", "Fields cannot be empty!", "warning", "ok")

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

    def to_faq_page(self):
        self.faqPage = user_faq_controller.UserFaqController()
        self.faqPage.userId = self.userId
        self.faqPage.lblUsername.setText(self.lblUsername.text())
        self.faqPage.userRole = self.userRole
        self.faqPage.initialize_faq()
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
