from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.reset_pass_page import Ui_reset_pass_page
from repository import user_repo, messagebox_repo


class ResetPassController(QMainWindow, Ui_reset_pass_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Reset Password Page")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.email = None
        self.profilePage = None
        self.btnBack.clicked.connect(self.go_to_prev_page)
        self.btnConfirmReset.clicked.connect(self.reset_password)
        self.lblbtnViewOrHidePass.mousePressEvent = self.show_or_hide_old_password
        self.lblbtnViewOrHidePass_2.mousePressEvent = self.show_or_hide_new_password

    def show_or_hide_new_password(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass_2.styleSheet() == u"image: url(:/view/view.png);":
                self.txtNewPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass_2.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass_2.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtNewPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass_2.setStyleSheet(u"image: url(:/view/view.png);")

    def go_to_prev_page(self):
        self.profilePage.show()
        self.close()

    def show_or_hide_old_password(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/view/view.png);":
                self.txtOldPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtOldPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")

    def reset_password(self):
        old_password = self.txtOldPass.text()
        new_password = self.txtNewPass.text()

        if old_password.strip() == "" or new_password.strip() == "":
            messagebox_repo.messagebox("Empty fields", "Password fields cannot be left empty.", "warning", "ok")
        else:
            if old_password == new_password:
                messagebox_repo.messagebox("Same password", "Two passwords are the same, no modifications needed.",
                                           "info", "ok")
            else:
                res = user_repo.check_if_user_password_is_correct(self.email, old_password)

                if res:
                    user_repo.reset_password(self.email, new_password)
                    self.go_to_prev_page()
