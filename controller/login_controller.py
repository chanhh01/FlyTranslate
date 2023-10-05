from PySide6.QtWidgets import QMainWindow, QLineEdit, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.login_page import Ui_login_page
from controller import welcome_controller, main_controller, minimized_operation_controller, \
    register_controller, forget_pass_controller
from repository import user_repo, settings_repo, messagebox_repo


class LoginController(QMainWindow, Ui_login_page):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Login Page")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)
        self.lblbtnViewOrHidePass.mousePressEvent = self.show_or_hide_pass
        self.lblbtnForgotPass.mousePressEvent = self.navigate_to_forget_password
        self.welcome = None
        self.registerPage = None
        self.min_operation_page = None
        self.forget_pass_page = None
        self.main_page = None
        self.btnBack.clicked.connect(self.prev_page)
        self.btnLoginAcc.clicked.connect(self.login_user)
        self.btnToRegister.clicked.connect(self.to_register_page)

    def show_or_hide_pass(self, event):
        if event.button() == Qt.LeftButton:
            if self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/view/view.png);":
                self.txtPass.setEchoMode(QLineEdit.Normal)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/hide/hide.png);")
            elif self.lblbtnViewOrHidePass.styleSheet() == u"image: url(:/hide/hide.png);":
                self.txtPass.setEchoMode(QLineEdit.Password)
                self.lblbtnViewOrHidePass.setStyleSheet(u"image: url(:/view/view.png);")

    def navigate_to_forget_password(self, event):
        if event.button() == Qt.LeftButton:
            self.forget_pass_page = forget_pass_controller.ForgetPassController()
            self.forget_pass_page.show()
            self.close()

    def prev_page(self):
        self.welcome = welcome_controller.WelcomeController()
        self.welcome.show()
        self.close()

    def to_register_page(self):
        self.registerPage = register_controller.RegisterController()
        self.registerPage.prevPage = self
        self.registerPage.show()
        self.close()

    def to_main_page(self, user_id):
        username = user_repo.retrieve_username_by_userid(user_id)
        user_role = user_repo.retrieve_user_role_by_user_id(user_id)
        self.main_page = main_controller.MainController()
        self.main_page.lblUsername.setText(username)
        self.main_page.userRole = user_role
        self.main_page.userId = user_id
        self.main_page.initialize_main_page()
        self.close()

    def to_minimized_page(self, user_id):
        username = user_repo.retrieve_username_by_userid(user_id)
        user_role = user_repo.retrieve_user_role_by_user_id(user_id)
        self.min_operation_page = minimized_operation_controller.MinimizedController()
        self.min_operation_page.userId = user_id
        self.min_operation_page.userRole = user_role
        self.min_operation_page.username = username
        self.min_operation_page.initialize_settings()
        self.close()

    def login_user(self):
        username_or_email = self.txtUsernameOrEmail.text()
        password = self.txtPass.text()

        if username_or_email.strip() == "" or password.strip() == "":
            messagebox_repo.messagebox("Empty fields", "Empty fields are not allowed", "warning", "ok")
        else:
            opt = False

            if self.cbRememberDevice.isChecked():
                opt = True

            user_id = user_repo.login_user(username_or_email, password, opt)

            if user_id is not None:
                res = settings_repo.check_if_user_checked_minimized_upon_login(user_id)

                if res == 1:
                    self.to_minimized_page(user_id)
                else:
                    self.to_main_page(user_id)
