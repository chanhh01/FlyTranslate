import uuid
import mysql_config
import hashlib
import re
from repository import messagebox_repo

conn = mysql_config.setup_mysql()


def add_user_device_into_session(user_id):
    try:
        mac_address = str(uuid.getnode())
        cursor = conn.cursor()
        query = "INSERT INTO device_session (user_id, mac_address) VALUES (%s, %s)"
        value = (user_id, mac_address)
        cursor.execute(query, value)
        conn.commit()
        cursor.close()
    except Exception as e:
        messagebox_repo.messagebox("Remember device error",
                                   f"This device is not remembered due to some errors. Details: {e}", "warning", "ok")


# source: https://medium.com/@dwernychukjosh/sha256-encryption-with-python-bf216db497f9
def encrypt_pass(password):
    encoded_pass = hashlib.sha256(password.encode()).hexdigest()
    return encoded_pass


def validate_email_format(email):
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    if re.match(pattern, email):
        return True
    else:
        msg = "Email format should be 'example@email.com', please try again with appropriate email format!"
        messagebox_repo.messagebox("Invalid email format", msg, "warning", "ok")
        return False


def login_user(username_or_email, password, remember_device):
    encoded_pass = encrypt_pass(password)

    try:
        cursor = conn.cursor()
        query = "SELECT user_id, username FROM users WHERE (username = %s OR email = %s) AND pass = %s"
        val = (username_or_email, username_or_email, encoded_pass)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is None:
            messagebox_repo.messagebox("Login error", "Invalid credentials or password, please try again!",
                                       "warning", "ok")
            return None
        else:
            user_id = res[0]
            username = res[1]
            if remember_device:
                add_user_device_into_session(user_id)

            messagebox_repo.messagebox("Login success!", f"Welcome back, {username}!", "info", "ok")
            return user_id

    except Exception as e:
        messagebox_repo.messagebox("Login error", f"{e}", "warning", "ok")
        return None


def register_user(username, email, password):
    encoded_pass = encrypt_pass(password)

    try:
        cursor = conn.cursor()
        query = "INSERT INTO users (username, email, pass, user_role) VALUES (%s, %s, %s, %s)"
        val = (username, email, encoded_pass, "normal_user")
        cursor.execute(query, val)
        conn.commit()
        user_id = cursor.lastrowid
        cursor.close()

        messagebox_repo.messagebox("Success!", "You are successfully registered!", "info", "ok")
        return user_id

    except Exception as e:
        messagebox_repo.messagebox("Register error", f"{e}", "warning", "ok")
        return None


def retrieve_user_detail_by_userid(user_id):
    try:
        cursor = conn.cursor()
        query = "SELECT username, email, user_role FROM users WHERE user_id = %s"
        val = (int(user_id),)
        cursor.execute(query, val)

        details = cursor.fetchone()

        if len(details) > 0:
            return details
        else:
            return None

    except Exception as e:
        messagebox_repo.messagebox("Retrieve users detail error", f"{e}", "warning", "ok")
        return None


def retrieve_username_by_userid(userid):
    try:
        details = retrieve_user_detail_by_userid(userid)

        if details is None:
            messagebox_repo.messagebox("Retrieve username error",
                                       "User not found, no username retrieved.", "warning", "ok")
            return "Username placeholder (Error)"
        else:
            username = details[0]
            return username

    except Exception as e:
        messagebox_repo.messagebox("Retrieve username error", f"{e}", "warning", "ok")
        return "Username placeholder (Error)"


def retrieve_email_by_username(username):
    try:
        cursor = conn.cursor()
        query = "SELECT email FROM users WHERE username = %s"
        val = (username,)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res:
            email = res[0]
            return email
        else:
            messagebox_repo.messagebox("Retrieve email error",
                                       "Email not found for this feedback user.", "warning", "ok")
            return None
    except Exception as e:
        messagebox_repo.messagebox("Retrieve email error", f"{e}", "warning", "ok")
        return None


def check_if_username_exists(username):
    try:
        cursor = conn.cursor()
        query = "SELECT username FROM users WHERE username = %s"
        val = (username,)
        cursor.execute(query, val)

        res = cursor.fetchone()

        cursor.close()

        if res is None:
            return False
        else:
            messagebox_repo.messagebox("Duplicate username",
                                       f"Username of '{username}' is used by other user. Try another username.",
                                       "warning", "ok")
            return True

    except Exception as e:
        messagebox_repo.messagebox("Username verification error", f"{e}", "warning", "ok")
        return True


def check_if_email_exists(email):
    try:
        cursor = conn.cursor()
        query = "SELECT user_id FROM users WHERE email = %s"
        val = (email,)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is None:
            return False
        else:
            return True

    except Exception as e:
        messagebox_repo.messagebox("Email verification error", f"{e}", "warning", "ok")
        return True


def check_if_user_password_is_correct(email, password):
    encoded_password = encrypt_pass(password)

    try:
        cursor = conn.cursor()
        query = "SELECT pass FROM users WHERE email = %s"
        val = (email,)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is None:
            return False
        else:
            if encoded_password == res[0]:
                return True
            else:
                msg = "Due to safety reasons, you cannot reset password without knowing your old password."
                messagebox_repo.messagebox("Old password is not correct.", msg, "warning", "ok")
                return False

    except Exception as e:
        messagebox_repo.messagebox("Old password check error", f"{e}", "warning", "ok")
        return False


def reset_password(email, password):
    encoded_password = encrypt_pass(password)

    try:
        cursor = conn.cursor()
        query = "UPDATE users SET pass = %s WHERE email = %s"
        val = (encoded_password, email)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()

        messagebox_repo.messagebox("Success!", "Password successfully reset!", "info", "ok")
    except Exception as e:
        messagebox_repo.messagebox("Reset password error", f"{e}", "warning", "ok")


def update_user_username(user_id, username):
    try:
        is_new_username_existed = check_if_username_exists(username)

        if not is_new_username_existed:
            cursor = conn.cursor()
            query = "UPDATE users SET username = %s WHERE user_id = %s"
            val = (username, int(user_id))
            cursor.execute(query, val)

            conn.commit()
            cursor.close()
            return True
        else:
            return False

    except Exception as e:
        messagebox_repo.messagebox("Update profile error", f"{e}", "warning", "ok")
        return False


def update_user_email(user_id, email):
    try:
        cursor = conn.cursor()
        query = "UPDATE users SET email = %s WHERE user_id = %s"
        val = (email, int(user_id))
        cursor.execute(query, val)

        conn.commit()
        cursor.close()
        return True
    except Exception as e:
        messagebox_repo.messagebox("Update profile error", f"{e}", "warning", "ok")
        return False


def retrieve_email_by_user_id(user_id):
    try:
        details = retrieve_user_detail_by_userid(user_id)

        if details is None:
            messagebox_repo.messagebox("Retrieve email error", "Email is not found through this user.", "warning", "ok")
            return None
        else:
            email = details[1]
            return email
    except Exception as e:
        messagebox_repo.messagebox("Retrieve email error", f"{e}", "warning", "ok")
        return None


def retrieve_user_role_by_user_id(user_id):
    try:
        details = retrieve_user_detail_by_userid(user_id)

        if details is None:
            messagebox_repo.messagebox("Retrieve user role error", "User does not exists.", "warning", "ok")
            return "normal_user"
        else:
            user_role = details[2]
            return user_role
    except Exception as e:
        messagebox_repo.messagebox("Retrieve user role error", f"{e}", "warning", "ok")
        return "normal_user"


def check_for_session():
    try:
        mac_address = str(uuid.getnode())
        cursor = conn.cursor()
        query = "SELECT user_id FROM device_session WHERE mac_address = %s"
        val = (mac_address,)
        cursor.execute(query, val)

        res = cursor.fetchone()
        cursor.close()

        if res is None:
            return False, None
        else:
            return True, res[0]
    except Exception as e:
        messagebox_repo.messagebox("Retrieve session error", f"{e}", "warning", "ok")
        return False, None


def remove_session():
    try:
        mac_address = str(uuid.getnode())
        cursor = conn.cursor()
        query = "DELETE FROM device_session WHERE mac_address = %s"
        val = (mac_address,)
        cursor.execute(query, val)

        conn.commit()
        cursor.close()

    except Exception as e:
        messagebox_repo.messagebox("Remove session error", f"{e}", "warning", "ok")
