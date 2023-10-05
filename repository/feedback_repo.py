import mysql_config
from repository import user_repo, messagebox_repo

conn = mysql_config.setup_mysql()


def retrieve_feedbacks(is_archived):
    try:
        cursor = conn.cursor()
        query = "SELECT report_id, user_id, title, content FROM report_feedback WHERE archived_or_replied = %s"
        val = (int(is_archived),)
        cursor.execute(query, val)

        res = cursor.fetchall()
        cursor.close()

        feedback_list = []

        if res is not None:
            usernames = [user_repo.retrieve_username_by_userid(int(row[1])) for row in res]

            for i, row in enumerate(res):
                feedback = {
                    "report_id": row[0],
                    "username": usernames[i],
                    "title": row[2],
                    "content": row[3]
                }
                feedback_list.append(feedback)

            return feedback_list
        else:
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve new feedbacks error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return None


def add_new_feedback(user_id, title, content):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO report_feedback (user_id, title, content, archived_or_replied) VALUES (%s, %s, %s, %s)"
        val = (int(user_id), title, content, 0)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()

        msg = "Your feedback may or may not be replied by us, but please " \
              "do check your email just in case we reply to you."
        messagebox_repo.messagebox("Feedback added!", msg, "info", "ok")
        return True
    except Exception as e:
        messagebox_repo.messagebox("Retrieve new feedbacks error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return False


def archive_or_unarchive_feedback(report_id, status):
    try:
        cursor = conn.cursor()
        query = "UPDATE report_feedback SET archived_or_replied = %s WHERE report_id = %s"
        val = (int(status), int(report_id))
        cursor.execute(query, val)

        conn.commit()
        cursor.close()

        return True
    except Exception as e:
        messagebox_repo.messagebox("Archive/Unarchive feedback error",
                                   f"{e}. Kindly report this to the developer.", "warning", "ok")
        return False
