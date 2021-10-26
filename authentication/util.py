# from django.core.mail import EmailMessage
from email.message import EmailMessage
import smtplib
import os

class Util:
    @staticmethod
    def send_email(data):
        msg = EmailMessage()
        msg.set_content(data['email_body'])

        fromEmail = os.getenv('EAMIL_HOST_USER')
        toEmail = data['to_email']

        msg['Subject'] = data['email_subject']
        msg['From'] = fromEmail
        msg['To'] = toEmail

        s = smtplib.SMTP('smtp.gmail.com', 587)

        s.starttls()

        s.login(fromEmail, os.getenv('EAMIL_HOST_PASSWORD'))
        s.send_message(msg)
