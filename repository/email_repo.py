from email.message import EmailMessage
import smtplib
import ssl
from repository import messagebox_repo

# inspired by https://www.youtube.com/watch?v=zxFXnLEmnb4


def send_otp_to_target_email(email, otp):
    try:
        email_sender = 'flytranslate123@gmail.com'
        email_pass = 'token placeholder'
        email_receiver = email

        subject = "Verify your email"
        body = f"""
            We just received registration or modification attempt for {email}.
            If this is you, please copy the 6-digit OTP below and paste it into the program.
            If this is not you, kindly ignore the message.

            OTP: {otp}

            Thank you for using FlyTranslate!
            """

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_pass)
            smtp.sendmail(email_sender, email_receiver, em.as_string())
    except Exception as e:
        messagebox_repo.messagebox("Send OTP error",
                                   f"OTP is not sent, try again. Details: {e}", "warning", "ok")


def reply_feedback_by_email(email, subject, content):
    try:
        email_sender = 'flytranslate123@gmail.com'
        email_pass = 'token placeholder'
        email_receiver = email

        subject = subject
        body = content

        em = EmailMessage()
        em['From'] = email_sender
        em['To'] = email_receiver
        em['subject'] = subject
        em.set_content(body)

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, email_pass)
            smtp.sendmail(email_sender, email_receiver, em.as_string())

        return True
    except Exception as e:
        messagebox_repo.messagebox("Error",
                                   f"Reply sent error, try again. Details: {e}", "warning", "ok")
        return False
