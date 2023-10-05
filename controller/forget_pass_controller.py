from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.forget_pass_page import Ui_forgot_password
from repository import user_repo, email_repo, messagebox_repo
from controller import login_controller
import random


class ForgetPassController(QMainWindow, Ui_forgot_password):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Forgot Password Page")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.otp = 0
        self.loginPage = None
        self.btnSendOTP.clicked.connect(self.send_otp_to_target_email)
        self.btnVerifyOTP.clicked.connect(self.verify_otp)
        self.btnBack.clicked.connect(self.go_to_prev_page)
        self.btnConfirmReset.clicked.connect(self.reset_password)
        self.lblbtnViewOrHidePass.mousePressEvent = self.show_or_hide_password
        self.enable_password_components(False)
        self.enable_otp_components(False)

    def enable_otp_components(self, enable):
        self.txtOTP.setEnabled(enable)
        self.btnVerifyOTP.setEnabled(enable)

    def enable_password_components(self, enable):
        self.txtNewPass.setEnabled(enable)
        self.btnConfirmReset.setEnabled(enable)
        self.lblbtnViewOrHidePass.setEnabled(enable)

    def send_otp_to_target_email(self):
        email = self.txtEmail.text()

        if email.strip() != "":
            is_email_valid = user_repo.validate_email_format(email)
            is_email_exists = user_repo.check_if_email_exists(email)

            if is_email_valid:
                if is_email_exists:
                    self.enable_otp_components(True)
                    self.otp = ''.join([str(random.randint(0, 9)) for i in range(6)])
                    email_repo.send_otp_to_target_email(email, self.otp)

                    messagebox_repo.messagebox("OTP sent!", "Please check your registered email for OTP.", "info", "ok")
                else:
                    self.enable_otp_components(False)
                    messagebox_repo.messagebox("Email not registered.",
                                               "This email is not found in our system. Please register this email.",
                                               "warning", "ok")
            else:
                self.enable_otp_components(False)
                messagebox_repo.messagebox("Invalid email", "Email must be example@gmail.com format.", "warning", "ok")
        else:
            messagebox_repo.messagebox("Email field is empty", "Please fill in your email.", "warning", "ok")

    def verify_otp(self):
        input_otp = self.txtOTP.text()

        if self.otp == input_otp:
            self.txtEmail.setEnabled(False)
            self.enable_otp_components(False)
            self.btnSendOTP.setEnabled(False)
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
        self.loginPage = login_controller.LoginController()
        self.loginPage.show()
        self.close()

    def show_or_hide_password(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/view/view.png);":
                self.txtNewPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtNewPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")

    def reset_password(self):
        password = self.txtNewPass.text()
        email = self.txtEmail.text()

        if password.strip() == "":
            messagebox_repo.messagebox("Empty fields", "New password field cannot be left empty.", "warning", "ok")
        else:
            user_repo.reset_password(email, password)
            self.go_to_prev_page()
