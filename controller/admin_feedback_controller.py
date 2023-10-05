from PySide6.QtWidgets import QMainWindow, QTableWidgetItem, QMessageBox
from python_ui_designs.admin_feedback_page import Ui_admin_feedback_page
from controller import welcome_controller, main_controller, runtime_setting_controller, \
    profile_setting_controller, admin_faq_controller, feedback_detail_controller
from repository import feedback_repo, user_repo, messagebox_repo


class AdminFeedbackController(QMainWindow, Ui_admin_feedback_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Admin Feedback Page")
        self.userId = 0
        self.userRole = 'admin'
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
        self.tbFeedbackList.itemClicked.connect(self.select_new_feedback)
        self.tbArchivedFeedback.itemClicked.connect(self.select_archived_feedback)

    def populate_tables(self):
        new_feedback_list = feedback_repo.retrieve_feedbacks(0)
        archived_feedback_list = feedback_repo.retrieve_feedbacks(1)

        self.tbFeedbackList.setRowCount(0)
        self.tbArchivedFeedback.setRowCount(0)

        if new_feedback_list is not None and len(new_feedback_list) > 0:
            for f in new_feedback_list:
                row = self.tbFeedbackList.rowCount()
                self.tbFeedbackList.insertRow(row)

                # Set data in each cell of the row
                self.tbFeedbackList.setItem(row, 0, QTableWidgetItem(str(f["report_id"])))
                self.tbFeedbackList.setItem(row, 1, QTableWidgetItem(f["username"]))
                self.tbFeedbackList.setItem(row, 2, QTableWidgetItem(f["title"]))
                self.tbFeedbackList.setItem(row, 3, QTableWidgetItem(f["content"]))

            self.tbFeedbackList.resizeColumnsToContents()

        if archived_feedback_list is not None and len(archived_feedback_list) > 0:
            for a in archived_feedback_list:
                row = self.tbArchivedFeedback.rowCount()
                self.tbArchivedFeedback.insertRow(row)

                # Set data in each cell of the row
                self.tbArchivedFeedback.setItem(row, 0, QTableWidgetItem(str(a["report_id"])))
                self.tbArchivedFeedback.setItem(row, 1, QTableWidgetItem(a["username"]))
                self.tbArchivedFeedback.setItem(row, 2, QTableWidgetItem(a["title"]))
                self.tbArchivedFeedback.setItem(row, 3, QTableWidgetItem(a["content"]))

            self.tbArchivedFeedback.resizeColumnsToContents()

    def initialize_feedback_page(self):
        self.tbFeedbackList.setColumnCount(4)
        self.tbFeedbackList.setHorizontalHeaderLabels(["ID", "Username", "Feedback Title", "Feedback Content"])
        self.tbArchivedFeedback.setColumnCount(4)
        self.tbArchivedFeedback.setHorizontalHeaderLabels(["ID", "Username", "Feedback Title", "Feedback Content"])
        self.populate_tables()
        self.show()

    def select_new_feedback(self, item):
        row = item.row()

        self.feedbackDetail = feedback_detail_controller.FeedbackDetailController()
        self.feedbackDetail.reportId = self.tbFeedbackList.item(row, 0).text()
        self.feedbackDetail.title = self.tbFeedbackList.item(row, 2).text()
        self.feedbackDetail.feedback_username = self.tbFeedbackList.item(row, 1).text()
        self.feedbackDetail.content = self.tbFeedbackList.item(row, 3).text()
        self.feedbackDetail.username = self.lblUsername.text()
        self.feedbackDetail.userId = self.userId
        self.feedbackDetail.userRole = "admin"
        self.feedbackDetail.prevPage = self
        self.feedbackDetail.isArchived = 0
        self.feedbackDetail.initialize_detail()
        self.close()

    def select_archived_feedback(self, item):
        row = item.row()

        self.feedbackDetail = feedback_detail_controller.FeedbackDetailController()
        self.feedbackDetail.reportId = self.tbArchivedFeedback.item(row, 0).text()
        self.feedbackDetail.title = self.tbArchivedFeedback.item(row, 2).text()
        self.feedbackDetail.feedback_username = self.tbArchivedFeedback.item(row, 1).text()
        self.feedbackDetail.content = self.tbArchivedFeedback.item(row, 3).text()
        self.feedbackDetail.username = self.lblUsername.text()
        self.feedbackDetail.userId = self.userId
        self.feedbackDetail.userRole = "admin"
        self.feedbackDetail.prevPage = self
        self.feedbackDetail.isArchived = 1
        self.feedbackDetail.initialize_detail()
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
        self.faqPage = admin_faq_controller.AdminFaqController()
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
