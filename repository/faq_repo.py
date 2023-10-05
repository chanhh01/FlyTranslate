import mysql_config
from repository import messagebox_repo

conn = mysql_config.setup_mysql()


def retrieve_all_faq_titles():
    try:
        cursor = conn.cursor()
        query = "SELECT faq_id, faq_title FROM faq"
        cursor.execute(query)

        res = cursor.fetchall()
        cursor.close()

        if len(res) > 0:
            faq_title_list = [f"{int(row[0])} :: {row[1]}" for row in res]
            return faq_title_list
        else:
            return None
    except Exception as e:
        messagebox_repo.messagebox("Retrieve FAQ titles error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return None


def retrieve_faq_content_based_on_id(faq_id):
    try:
        cursor = conn.cursor()
        query = "SELECT faq_content FROM faq WHERE faq_id = %s"
        val = (int(faq_id),)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is not None:
            faq_content = res[0]
            return faq_content
        else:
            messagebox_repo.messagebox("Retrieve FAQ content error",
                                       "FAQ content is not retrieved. Kindly report this to the administrators.",
                                       "warning", "ok")
            return None
    except Exception as e:
        messagebox_repo.messagebox("Retrieve FAQ content error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return None


def add_new_faq(faq_title, faq_content):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO faq (faq_title, faq_content) VALUES (%s, %s)"
        val = (faq_title, faq_content)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()
        messagebox_repo.messagebox("Success!", "New FAQ added!", "info", "ok")
        return True
    except Exception as e:
        messagebox_repo.messagebox("Add new FAQ error", f"{e}", "warning", "ok")
        return False


def edit_faq(faq_id, faq_title, faq_content):
    try:
        cursor = conn.cursor()
        query = "UPDATE faq SET faq_title = %s, faq_content = %s WHERE faq_id = %s"
        val = (faq_title, faq_content, int(faq_id))
        cursor.execute(query, val)

        conn.commit()
        cursor.close()
        messagebox_repo.messagebox("Success!", "Target FAQ is successfully edited!", "info", "ok")
        return True
    except Exception as e:
        messagebox_repo.messagebox("Add new FAQ error", f"{e}", "warning", "ok")
        return False


def remove_faq(faq_id):
    try:
        cursor = conn.cursor()
        query = "DELETE FROM faq WHERE faq_id = %s"
        val = (int(faq_id),)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()
        messagebox_repo.messagebox("Success!", "Target FAQ is removed!", "info", "ok")
        return True
    except Exception as e:
        messagebox_repo.messagebox("Remove FAQ error", f"{e}", "warning", "ok")
        return False
