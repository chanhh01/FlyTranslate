from PySide6.QtWidgets import QMainWindow
from python_ui_designs.welcome_page import Ui_welcome_page
from controller import login_controller, register_controller


class WelcomeController(QMainWindow, Ui_welcome_page):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Welcome Page")
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)
        self.loginPage = None
        self.registerPage = None
        self.btnLogin.clicked.connect(self.switch_to_login)
        self.btnRegister.clicked.connect(self.switch_to_register)

    def switch_to_login(self):
        self.loginPage = login_controller.LoginController()
        self.loginPage.show()
        self.close()

    def switch_to_register(self):
        self.registerPage = register_controller.RegisterController()
        self.registerPage.prevPage = self
        self.registerPage.show()
        self.close()
