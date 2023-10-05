from PySide6.QtWidgets import QMainWindow, QMessageBox
from python_ui_designs.admin_faq_page import Ui_admin_faq_page
from controller import welcome_controller, main_controller, profile_setting_controller, \
     runtime_setting_controller, admin_feedback_controller
from repository import faq_repo, user_repo, messagebox_repo


class AdminFaqController(QMainWindow, Ui_admin_faq_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Admin FAQ Page")
        self.userId = 0
        self.userRole = "admin"
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.mainPage = None
        self.profileSettingsPage = None
        self.runtimeSettingsPage = None
        self.feedbackPage = None

        self.faq_id = 0
        self.title = None
        self.content = None
        self.cbbFAQ.currentIndexChanged.connect(self.populate_faq_content)
        self.btnMainButton.clicked.connect(self.to_main_page)
        self.btnRunTimeSettings.clicked.connect(self.to_runtime_page)
        self.btnProfileSettings.clicked.connect(self.to_profile_page)
        self.btnFeedback.clicked.connect(self.to_feedback_page)
        self.btnLogout.clicked.connect(self.logout_user)
        self.btnRemoveFaq.clicked.connect(self.remove_faq)
        self.btnEditFAQ.clicked.connect(self.edit_faq)
        self.btnAddNewFaq.clicked.connect(self.add_new_faq)

    def populate_faq_content(self):
        selected = self.cbbFAQ.currentText()

        if selected == "Add new FAQ....":
            self.txtFAQTitle.clear()
            self.txtFAQ.clear()
            self.btnAddNewFaq.setEnabled(True)
            self.btnRemoveFaq.setEnabled(False)
            self.btnEditFAQ.setEnabled(False)
        else:
            faq_id_str = selected.split(" :: ", 1)[0]

            if faq_id_str != '':
                faq_id = int(faq_id_str)
                faq_title = selected.split(" :: ", 1)[1]

                faq_content = faq_repo.retrieve_faq_content_based_on_id(faq_id)

                self.faq_id = faq_id
                self.title = faq_title
                self.content = faq_content
                self.txtFAQTitle.setText(faq_title)
                self.txtFAQ.setPlainText(faq_content)

                self.btnAddNewFaq.setEnabled(False)
                self.btnRemoveFaq.setEnabled(True)
                self.btnEditFAQ.setEnabled(True)

    def populate_faq_list(self):
        faq_lists = faq_repo.retrieve_all_faq_titles()
        self.cbbFAQ.clear()
        self.cbbFAQ.addItem("Add new FAQ....")

        if faq_lists is not None:
            self.cbbFAQ.addItems(faq_lists)
            self.cbbFAQ.setCurrentText("Add new FAQ....")

    def initialize_faq(self):
        self.populate_faq_list()
        self.show()

    def add_new_faq(self):
        faq_title = self.txtFAQTitle.toPlainText()
        faq_content = self.txtFAQ.toPlainText()

        if faq_title.strip() == "" and faq_content.strip() == "":
            messagebox_repo.messagebox("Empty fields.", "No empty fields are allowed!", "warning", "ok")
        else:
            if len(faq_title) <= 255:
                res = faq_repo.add_new_faq(faq_title, faq_content)

                if res:
                    self.populate_faq_list()
            else:
                messagebox_repo.messagebox("Error!", "Title cannot be more than 255 characters!", "warning", "ok")

    def edit_faq(self):
        faq_title = self.txtFAQTitle.toPlainText()
        faq_content = self.txtFAQ.toPlainText()

        if faq_title == self.title and faq_content == self.content:
            messagebox_repo.messagebox("No changes", "No modifications are detected, thus no edit is done.",
                                     "warning", "ok")
        else:
            if faq_title.strip() == "" and faq_content.strip() == "":
                messagebox_repo.messagebox("Empty fields.", "No empty fields are allowed!", "warning", "ok")
            else:
                if len(faq_title) <= 255:
                    res = faq_repo.edit_faq(self.faq_id, faq_title, faq_content)

                    if res:
                        self.populate_faq_list()
                else:
                    messagebox_repo.messagebox("Error!", "Title cannot be more than 255 characters!", "warning", "ok")

    def remove_faq(self):
        res = faq_repo.remove_faq(self.faq_id)

        if res:
            self.populate_faq_list()

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
        self.feedbackPage = admin_feedback_controller.AdminFeedbackController()
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
