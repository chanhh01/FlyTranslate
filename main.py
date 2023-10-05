import sys
from controller.welcome_controller import WelcomeController
from controller.main_controller import MainController
from controller.minimized_operation_controller import MinimizedController
from mysql_config import setup_mysql
from PySide6.QtWidgets import QApplication
from repository import user_repo, settings_repo

if __name__ == "__main__":
    conn = setup_mysql()
    app = QApplication(sys.argv)

    session_exists, user_id = user_repo.check_for_session()

    # if session exists, skip login process
    if not session_exists:
        welcomePage = WelcomeController()
        welcomePage.show()
    else:
        # check if user has launch minimized window toggled
        res = settings_repo.check_if_user_checked_minimized_upon_login(user_id)
        username = user_repo.retrieve_username_by_userid(user_id)
        user_role = user_repo.retrieve_user_role_by_user_id(user_id)
        if res == 0:
            # navigate to main page with user_id
            mainPage = MainController()
            mainPage.lblUsername.setText(username)
            mainPage.userRole = user_role
            mainPage.userId = user_id
            mainPage.initialize_main_page()

        elif res == 1:
            # navigate to minimized window with user_id
            minimizedPage = MinimizedController()
            minimizedPage.userId = user_id
            minimizedPage.userRole = user_role
            minimizedPage.username = username
            minimizedPage.initialize_settings()

    sys.exit(app.exec())


