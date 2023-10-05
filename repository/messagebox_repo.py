from PySide6.QtWidgets import QMessageBox


def messagebox(title, text, icon, buttons):
    msg_box = QMessageBox()
    msg_box.setWindowTitle(title)
    msg_box.setText(text)

    if icon == "warning":
        msg_box.setIcon(QMessageBox.Warning)
    elif icon == "info":
        msg_box.setIcon(QMessageBox.Information)
    elif icon == "question":
        msg_box.setIcon(QMessageBox.Question)

    if buttons == "ok":
        msg_box.setStandardButtons(QMessageBox.Ok)
    elif buttons == "yesno":
        msg_box.setStandardButtons(QMessageBox.Yes | QMessageBox.No)

    result = msg_box.exec_()
    return result
