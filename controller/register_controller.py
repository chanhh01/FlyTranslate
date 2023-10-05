from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.register_page import Ui_register_page
from controller import login_controller, welcome_controller
from repository import user_repo, settings_repo, email_repo, messagebox_repo
import random


class RegisterController(QMainWindow, Ui_register_page):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Register Page")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.loginPage = None
        self.welcomePage = None
        self.prevPage = None
        self.otp = 0
        self.btnSendOTP.clicked.connect(self.send_otp_to_target_email)
        self.btnBack.clicked.connect(self.go_to_prev_page)
        self.btnRegisterAcc.clicked.connect(self.register_user)
        self.btnVerifyOTP.clicked.connect(self.verify_otp)
        self.lblbtnViewOrHidePass.mousePressEvent = self.show_or_hide_password
        self.lblbtnViewOrHidePass_2.mousePressEvent = self.show_or_hide_confirm_password
        self.otpTip = "One Time Pin (OTP) is a 6-digit number pin that will be sent to your email for verification"
        self.lblTipsOTP.setToolTip(self.otpTip)
        self.enable_otp_components(False)
        self.enable_password_components(False)

    def enable_otp_components(self, enable):
        self.txtOTP.setEnabled(enable)
        self.btnVerifyOTP.setEnabled(enable)
        self.lblTipsOTP.setEnabled(enable)

    def enable_password_components(self, enable):
        self.txtPass.setEnabled(enable)
        self.txtConfirmPass.setEnabled(enable)
        self.btnRegisterAcc.setEnabled(enable)
        self.lblbtnViewOrHidePass.setEnabled(enable)
        self.lblbtnViewOrHidePass_2.setEnabled(enable)

    def send_otp_to_target_email(self):
        email = self.txtEmail.text()

        if email.strip() != "":
            is_email_valid = user_repo.validate_email_format(email)
            is_email_exists = user_repo.check_if_email_exists(email)

            if is_email_valid:
                if not is_email_exists:
                    self.enable_otp_components(True)
                    self.otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                    email_repo.send_otp_to_target_email(email, self.otp)
                    messagebox_repo.messagebox("OTP sent!",
                                             "Please check your registered email for OTP.",
                                             "info", "ok")
                else:
                    messagebox_repo.messagebox("Duplicate email",
                                             f"Email of '{email}' exists in system. Try another email.",
                                             "warning", "ok")
            else:
                self.enable_otp_components(False)
                messagebox_repo.messagebox("Invalid email",
                                         "Email must be example@gmail.com format.",
                                         "warning", "ok")
        else:
            messagebox_repo.messagebox("Email field is empty",
                                     "Please fill in your email.",
                                     "warning", "ok")

    def verify_otp(self):
        input_otp = self.txtOTP.text()

        if self.otp == input_otp:
            self.txtEmail.setEnabled(False)
            self.btnSendOTP.setEnabled(False)
            self.enable_otp_components(False)
            self.enable_password_components(True)
            messagebox_repo.messagebox("Email verified",
                                       "You may now fill in your password credentials.",
                                       "info", "ok")
        else:
            messagebox_repo.messagebox("OTP incorrect",
                                       "The input OTP is incorrect. Please check again on your registered email.",
                                       "warning", "ok")
            self.enable_password_components(False)

    def go_to_prev_page(self):
        self.prevPage.show()
        self.close()

    def show_or_hide_password(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/view/view.png);":
                self.txtPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")

    def show_or_hide_confirm_password(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass_2.styleSheet() == u"image: url(:/view/view.png);":
                self.txtConfirmPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass_2.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass_2.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtConfirmPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass_2.setStyleSheet(u"image: url(:/view/view.png);")

    def register_user(self):
        username = self.txtUsername.text()
        email = self.txtEmail.text()
        password = self.txtPass.text()
        confirm_pass = self.txtConfirmPass.text()

        if username.strip() == "" or password.strip() == "" or confirm_pass.strip() == "":
            messagebox_repo.messagebox("There are empty fields", "Empty fields are not allowed.", "warning", "ok")
        else:
            is_username_exists = user_repo.check_if_username_exists(username)

            if not is_username_exists:
                if password == confirm_pass:
                    user_id = user_repo.register_user(username, email, password)

                    if user_id is not None:
                        settings_repo.register_new_user_setting(user_id)
                        self.loginPage = login_controller.LoginController()
                        self.loginPage.show()
                        self.close()
                    else:
                        self.welcomePage = welcome_controller.WelcomeController()
                        self.welcomePage.show()
                        self.close()
                else:
                    messagebox_repo.messagebox("Passwords do not match.",
                                             "Please ensure you write you have confirmed the correct password.",
                                             "warning", "ok")
