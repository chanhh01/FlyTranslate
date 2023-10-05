from PySide6.QtWidgets import QMainWindow, QMessageBox
from PySide6.QtCore import Qt
from python_ui_designs.feedback_detail import Ui_feedback_details
from controller import admin_feedback_controller, reply_feedback_controller
from repository import feedback_repo, messagebox_repo


class FeedbackDetailController(QMainWindow, Ui_feedback_details):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowTitle("Feedback Detail Page")
        self.userId = 0
        self.userRole = 'admin'
        self.username = None
        win_height = self.size().height()
        win_width = self.size().width()
        self.setFixedSize(win_width, win_height)

        self.adminFeedbackPage = None
        self.prevPage = None
        self.replyFeedbackPage = None

        self.reportId = None
        self.feedback_username = None
        self.title = None
        self.content = None
        self.isArchived = 0
        self.isEdited = 0

        self.txtContent.setReadOnly(True)
        self.btnUnarchive.clicked.connect(self.unarchive_feedback)
        self.btnArchive.clicked.connect(self.archive_feedback)
        self.btnReply.clicked.connect(self.reply_feedback)
        self.lblbtnBack.mousePressEvent = self.back_to_prev_page

    def populate_fields(self):
        self.lblTitle.setText(self.title)
        self.lblFeedbackUser.setText("By: " + self.feedback_username)
        self.txtContent.setPlainText(self.content)

        if self.isArchived == 0:
            self.btnUnarchive.setEnabled(False)
            self.btnReply.setEnabled(True)
            self.btnArchive.setEnabled(True)
        else:
            self.btnUnarchive.setEnabled(True)
            self.btnReply.setEnabled(False)
            self.btnArchive.setEnabled(False)

    def initialize_detail(self):
        self.populate_fields()
        self.show()

    def archive_feedback(self):
        result = messagebox_repo.messagebox("Wait!", "Are you sure you want to archive this feedback?", "question", "yesno")

        if result == QMessageBox.Yes:
            res = feedback_repo.archive_or_unarchive_feedback(self.reportId, 1)

            if res:
                self.isEdited = 1
                self.isArchived = 1
                self.populate_fields()
                messagebox_repo.messagebox("Success!", "Feedback archived!", "info", "ok")

    def unarchive_feedback(self):
        result = messagebox_repo.messagebox("Wait!", "Are you sure you want to unarchive this feedback?", "question", "yesno")
        if result == QMessageBox.Yes:
            res = feedback_repo.archive_or_unarchive_feedback(self.reportId, 0)

            if res:
                self.isEdited = 1
                self.isArchived = 0
                self.populate_fields()
                messagebox_repo.messagebox("Success!", "Feedback unarchived!", "info", "ok")

    def back_to_prev_page(self, event):
        if event.button() == Qt.LeftButton:
            if self.isEdited == 0:
                self.prevPage.show()
                self.close()

            elif self.isEdited == 1:
                self.adminFeedbackPage = admin_feedback_controller.AdminFeedbackController()
                self.adminFeedbackPage.userId = self.userId
                self.adminFeedbackPage.lblUsername.setText(self.username)
                self.adminFeedbackPage.userRole = "admin"
                self.adminFeedbackPage.initialize_feedback_page()
                self.close()

    def reply_feedback(self):
        self.replyFeedbackPage = reply_feedback_controller.ReplyFeedbackController()
        self.replyFeedbackPage.prevPage = self
        self.replyFeedbackPage.userId = self.userId
        self.replyFeedbackPage.username = self.username
        self.replyFeedbackPage.userRole = "admin"
        self.replyFeedbackPage.reportId = self.reportId
        self.replyFeedbackPage.feedback_username = self.feedback_username
        reply_title = "Re: " + self.title
        self.replyFeedbackPage.txtTitle.setText(reply_title)
        self.replyFeedbackPage.originalContent = self.content
        self.replyFeedbackPage.show()
        self.close()

