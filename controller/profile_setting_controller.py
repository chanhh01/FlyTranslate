from PySide6.QtWidgets import QMainWindow, QMessageBox
from python_ui_designs.profile_setting_page import Ui_profile_page
from controller import welcome_controller, main_controller, runtime_setting_controller, \
    user_faq_controller, admin_faq_controller, admin_feedback_controller, \
    user_feedback_controller, reset_pass_controller
from repository import user_repo, email_repo, messagebox_repo
import random


class ProfileSettingController(QMainWindow, Ui_profile_page):
    def __init__(self):

        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Profile Settings Page")
        self.userId = 0
        self.userRole = 'normal_user'
        self.lblUsername.setText("SAMPLEUSERNAME")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.welcomePage = None
        self.mainPage = None
        self.runtimeSettingsPage = None
        self.faqPage = None
        self.feedbackPage = None
        self.resetPassPage = None

        self.otp = 0
        self.targetEmail = None
        self.email = None
        self.username = None
        self.grpbxlOTP.setVisible(False)
        self.btnMainButton.clicked.connect(self.to_main_page)
        self.btnRunTimeSettings.clicked.connect(self.to_runtime_page)
        self.btnFAQ.clicked.connect(self.to_faq_page)
        self.btnFeedback.clicked.connect(self.to_feedback_page)
        self.btnLogout.clicked.connect(self.logout_user)
        self.btnResetPassword.clicked.connect(self.go_to_reset_pass_page)
        self.btnConfirmEdit.clicked.connect(self.edit_profile)
        self.btnResendOTP.clicked.connect(self.send_otp_to_email)
        self.btnVerifyOTP.clicked.connect(self.verify_otp_for_email)

    def send_otp_to_email(self):
        self.otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
        email_repo.send_otp_to_target_email(self.targetEmail, self.otp)
        messagebox_repo.messagebox("OTP sent!",
                                 f"Please check inbox of {self.targetEmail} for OTP.",
                                 "info", "ok")

    def verify_otp_for_email(self):
        input_otp = self.txtOTP.text()

        if self.otp == input_otp:
            if self.targetEmail == self.email:
                messagebox_repo.messagebox("Old email verified!",
                                           "Now proceed to new email verification.",
                                           "info", "ok")
                self.txtOTP.clear()
                self.targetEmail = self.txtEmail.text().strip()
                self.send_otp_to_email()

            elif self.targetEmail == self.txtEmail.text().strip():
                self.txtOTP.clear()
                self.process_new_email_edit(self.targetEmail)
        else:
            messagebox_repo.messagebox("OTP incorrect",
                                       "The input OTP is incorrect. Please check again on your registered email.",
                                       "warning", "ok")

    def enable_input_fields(self, enable):
        self.txtEmail.setEnabled(enable)
        self.txtUsername.setEnabled(enable)
        self.btnConfirmEdit.setEnabled(enable)

    def process_new_email_edit(self, email):
        res = user_repo.update_user_email(self.userId, email)
        self.enable_input_fields(True)
        self.grpbxlOTP.setVisible(False)

        if res:
            messagebox_repo.messagebox("Success!",
                                       "Your email is successfully updated!",
                                       "info", "ok")
            self.email = email
            self.txtEmail.setText(email)
        else:
            self.targetEmail = self.email
            self.txtEmail.setText(self.email)

    def process_old_email_edit(self):
        self.grpbxlOTP.setVisible(True)
        self.targetEmail = self.email
        self.send_otp_to_email()

    def edit_profile(self):
        email = self.txtEmail.text()
        username = self.txtUsername.text()

        if email == self.email and username == self.username:
            messagebox_repo.messagebox("Warning!",
                                       "No modifications are detected.",
                                       "warning", "ok")
        else:
            result = messagebox_repo.messagebox("Wait!",
                                                "Modification detected, confirm edit?",
                                                "question", "yesno")
            if result == QMessageBox.Yes:
                if email.strip() == "" or username.strip() == "":
                    self.txtEmail.setText(self.email)
                    self.txtUsername.setText(self.username)
                    messagebox_repo.messagebox("Empty fields",
                                               "Empty fields detected. No empty fields allowed.",
                                               "warning", "ok")
                else:
                    self.enable_input_fields(False)

                    if username != self.username:
                        if user_repo.update_user_username(self.userId, username):
                            self.username = username
                            self.lblUsername.setText(username)
                            self.txtUsername.setText(username)

                            messagebox_repo.messagebox("Success!",
                                                       "Your username is successfully updated!",
                                                       "info", "ok")

                            if email == self.email:
                                self.enable_input_fields(True)
                            else:
                                if user_repo.validate_email_format(email):
                                    if not user_repo.check_if_email_exists(email):
                                        self.process_old_email_edit()
                                    else:
                                        messagebox_repo.messagebox("Duplicate email",
                                                                   f"Email of '{email}' exists in system. Try another email.",
                                                                   "warning", "ok")
                                        self.txtEmail.setText(self.email)
                                        self.enable_input_fields(True)
                                else:
                                    self.txtEmail.setText(self.email)
                                    self.enable_input_fields(True)
                        else:
                            self.txtUsername.setText(self.username)
                            self.enable_input_fields(True)
                    else:
                        if user_repo.validate_email_format(email):
                            if not user_repo.check_if_email_exists(email):
                                self.process_old_email_edit()
                            else:
                                messagebox_repo.messagebox("Duplicate email",
                                                           f"Email of '{email}' exists in system. Try another email.",
                                                           "warning", "ok")
                                self.txtEmail.setText(self.email)
                                self.enable_input_fields(True)
                        else:
                            self.txtEmail.setText(self.email)
                            self.enable_input_fields(True)

    def go_to_reset_pass_page(self):
        self.resetPassPage = reset_pass_controller.ResetPassController()
        self.resetPassPage.profilePage = self
        self.resetPassPage.email = user_repo.retrieve_email_by_user_id(self.userId)
        self.resetPassPage.show()
        self.close()

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
