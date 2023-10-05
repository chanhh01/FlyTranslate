from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.reply_feedback_page import Ui_reply_feedback_page
from controller import admin_feedback_controller
from repository import feedback_repo, user_repo, email_repo, messagebox_repo


class ReplyFeedbackController(QMainWindow, Ui_reply_feedback_page):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Feedback Reply Page")
        self.userId = 0
        self.userRole = 'admin'
        self.username = None
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.adminFeedbackPage = None
        self.prevPage = None

        self.feedback_username = None
        self.reportId = None
        self.originalContent = None

        self.btnSubmitReply.clicked.connect(self.submit_reply)
        self.btnClear.clicked.connect(self.clear_contents)
        self.lblbtnBack.mousePressEvent = self.go_to_prev_page

    def clear_contents(self):
        self.txtContent.clear()

    def go_to_admin_feedback_page(self):
        self.adminFeedbackPage = admin_feedback_controller.AdminFeedbackController()
        self.adminFeedbackPage.userId = self.userId
        self.adminFeedbackPage.lblUsername.setText(self.username)
        self.adminFeedbackPage.userRole = "admin"
        self.adminFeedbackPage.initialize_feedback_page()
        self.close()

    def go_to_prev_page(self, event):
        if event.button() == Qt.LeftButton:
            self.prevPage.show()
            self.close()

    def submit_reply(self):
        title = self.txtTitle.toPlainText()
        content = self.txtContent.toPlainText()

        if title.strip() != "" and content.strip() != "":
            if len(title) <= 255:

                result = messagebox_repo.messagebox("Wait!", "Are you sure you want to reply to this feedback?",
                                         "question", "yesno")

                if result == QMessageBox.Yes:
                    email = user_repo.retrieve_email_by_username(self.feedback_username)

                    if email is not None:
                        email_content = f"""
                        Your feedback:
                        '{self.originalContent}'
                        
                        
                        Reply:
                        {content}
                        """
                        res = email_repo.reply_feedback_by_email(email, title, email_content)

                        if res:
                            messagebox_repo.messagebox("Success!", "Reply successfully sent!", "info", "ok")

                            res_archive = feedback_repo.archive_or_unarchive_feedback(self.reportId, 1)

                            if res_archive:
                                self.go_to_admin_feedback_page()

            else:
                messagebox_repo.messagebox("Error!", "Title cannot be more than 255 characters!", "warning", "ok")
        else:
            messagebox_repo.messagebox("Error!", "Fields cannot be empty!", "warning", "ok")
