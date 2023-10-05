import mysql_config
from repository import messagebox_repo

conn = mysql_config.setup_mysql()


def retrieve_full_runtime_settings_by_user_id(user_id):
    try:
        cursor = conn.cursor()
        query = "SELECT source_lang, target_lang, x1_coord, y1_coord, x2_coord, y2_coord, " \
                "full_screen, save_log, text_replacement_bool, minimize_upon_login FROM user_settings " \
                "WHERE user_id = %s"
        val = (int(user_id),)
        cursor.execute(query, val)

        settings = cursor.fetchone()
        cursor.close()

        if len(settings) > 0:
            return settings
        else:
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve settings error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return None


def check_if_user_checked_minimized_upon_login(user_id):
    try:
        settings = retrieve_full_runtime_settings_by_user_id(user_id)

        if settings is not None:
            res = int(settings[9])
            return res
        else:
            return 0

    except Exception as e:
        messagebox_repo.messagebox("Settings check error", f"{e}", "warning", "ok")
        return 0


def register_new_user_setting(user_id):
    try:
        cursor = conn.cursor()
        query = "INSERT INTO user_settings (user_id, source_lang, target_lang, x1_coord, y1_coord, x2_coord, y2_coord," \
                " full_screen, save_log, text_replacement_bool, minimize_upon_login) VALUES " \
                "(%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        val = (int(user_id), 37, 182, 0, 0, 0, 0, 1, 0, 0, 0)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()
    except Exception as e:
        messagebox_repo.messagebox("Setting registration error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")


def retrieve_ocr_related_runtime_settings(user_id):
    try:
        settings = retrieve_full_runtime_settings_by_user_id(user_id)

        if settings is not None:
            full_screen = int(settings[6])
            save_log = int(settings[7])
            text_replacement = int(settings[8])

            return full_screen, save_log, text_replacement
        else:
            return 1, 0, 1
    except Exception as e:
        messagebox_repo.messagebox("OCR setting retrieve error",
                                   f"{e}. Kindly report this to the administrators.", "warning", "ok")
        return 1, 0, 1


def retrieve_user_crop_area(user_id):
    try:
        settings = retrieve_full_runtime_settings_by_user_id(user_id)

        if settings is not None:
            x1 = int(settings[2])
            y1 = int(settings[3])
            x2 = int(settings[4])
            y2 = int(settings[5])

            crop_bound = (x1, y1, x2, y2)

            return crop_bound
        else:
            return ()

    except Exception as e:
        messagebox_repo.messagebox("Retrieve crop boundary error", f"{e}", "warning", "ok")
        return ()


def update_full_screen_status(user_id, status):
    try:
        cursor = conn.cursor()
        query = "UPDATE user_settings SET full_screen = %s WHERE user_id = %s"
        val = (int(status), int(user_id))
        cursor.execute(query, val)

        conn.commit()
        cursor.close()

        return True
    except Exception as e:
        messagebox_repo.messagebox("Update full screen status error", f"{e}", "warning", "ok")
        return False


def update_crop_area(user_id, crop_bound):
    try:
        x1 = int(crop_bound[0])
        y1 = int(crop_bound[1])
        x2 = int(crop_bound[2])
        y2 = int(crop_bound[3])

        if x2 - x1 != 0 and y2 - y1 != 0:
            cursor = conn.cursor()
            query = "UPDATE user_settings SET x1_coord = %s, y1_coord = %s, " \
                    "x2_coord = %s, y2_coord = %s WHERE user_id = %s"
            val = (x1, y1, x2, y2, int(user_id))
            cursor.execute(query, val)
            conn.commit()

            cursor.close()
            return True
        else:
            messagebox_repo.messagebox("Update crop boundary error",
                                       "The cropped boundary is empty! Please try again after cropping screen area!",
                                       "warning", "ok")
            return False
    except Exception as e:
        messagebox_repo.messagebox("Update crop boundary error", f"{e}", "warning", "ok")
        return False


def update_runtime_settings(user_id, text_replacement, to_save_log, to_minimize_upon_login):
    try:
        cursor = conn.cursor()
        query = "UPDATE user_settings SET save_log = %s, " \
                "text_replacement_bool = %s, minimize_upon_login = %s WHERE user_id = %s"
        val = (int(to_save_log), int(text_replacement),
               int(to_minimize_upon_login), int(user_id))
        cursor.execute(query, val)
        conn.commit()

        cursor.close()

        messagebox_repo.messagebox("Update success!",
                                   "New settings configurations are saved.", "info", "ok")
    except Exception as e:
        messagebox_repo.messagebox("Update runtime settings error", f"{e}", "warning", "ok")


def retrieve_current_available_languages():
    try:
        cursor = conn.cursor()
        query = "SELECT lang_name FROM languages WHERE lang_code_for_ocr IS NOT NULL"
        cursor.execute(query)

        res = cursor.fetchall()
        cursor.close()

        if len(res) > 0:
            lang_code_list = [row[0] for row in res]
            return lang_code_list
        else:
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve languages error", f"{e}", "warning", "ok")
        return None


def retrieve_user_source_and_target_language(user_id):
    try:
        settings = retrieve_full_runtime_settings_by_user_id(user_id)

        if settings is not None:
            source_lang_id = settings[0]
            target_lang_id = settings[1]

            if source_lang_id is not None and target_lang_id is not None:
                return source_lang_id, target_lang_id

    except Exception as e:
        messagebox_repo.messagebox("Retrieve user language error", f"{e}", "warning", "ok")
        return None, None


def retrieve_lang_name_by_lang_id(lang_id):
    try:
        cursor = conn.cursor()
        query = "SELECT lang_name FROM languages WHERE lang_id = %s"
        val = (int(lang_id),)
        cursor.execute(query, val)

        lang_name = cursor.fetchone()

        cursor.close()

        if lang_name is not None:
            return lang_name[0]
        else:
            messagebox_repo.messagebox("Retrieve language name error",
                                       "The language name for the language you chosen does not exists.", "warning", "ok")
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve language name error", f"{e}", "warning", "ok")
        return None


def retrieve_lang_code_by_lang_id(lang_id):
    try:
        cursor = conn.cursor()
        query = "SELECT lang_code FROM languages WHERE lang_id = %s"
        val = (int(lang_id), )
        cursor.execute(query, val)

        lang_code = cursor.fetchone()

        cursor.close()

        if lang_code is not None:
            return lang_code[0]
        else:
            messagebox_repo.messagebox("Retrieve language code error",
                                       "The language code for the language you chosen does not exists.", "warning", "ok")
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve language code error", f"{e}", "warning", "ok")
        return None


def retrieve_lang_id_by_lang_name(lang_name):
    try:
        cursor = conn.cursor()
        query = "SELECT lang_id FROM languages WHERE lang_name = '" + lang_name + "'"
        cursor.execute(query)

        lang_id = cursor.fetchone()

        cursor.close()

        if lang_id is not None:
            return lang_id[0]
        else:
            return None
    except Exception as e:
        messagebox_repo.messagebox("Retrieve language id error", f"{e}", "warning", "ok")
        return None


def update_user_language(user_id, source_lang_name, target_lang_name):
    try:
        source_lang_id = retrieve_lang_id_by_lang_name(source_lang_name)
        target_lang_id = retrieve_lang_id_by_lang_name(target_lang_name)

        if source_lang_id is not None and target_lang_id is not None:
            cursor = conn.cursor()
            query = "UPDATE user_settings SET source_lang = %s, target_lang = %s WHERE user_id = %s"
            val = (int(source_lang_id), int(target_lang_id), int(user_id))
            cursor.execute(query, val)

            conn.commit()
            cursor.close()
            return True
        else:
            messagebox_repo.messagebox("Update user language error",
                                       "The language IDs for the language you chosen for update does not exists.",
                                       "warning", "ok")
            return False
    except Exception as e:
        messagebox_repo.messagebox("Update language configuration error", f"{e}", "warning", "ok")
        return False
