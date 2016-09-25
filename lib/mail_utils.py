__author__ = 'bluzky'
from config import mail
from flask_mail import Message

def send_mail(subject, sender, recipients, text_body, html_body, cc= None, bcc=None):
    message = Message(subject=subject, sender=sender, recipients=recipients, cc=cc, bcc=bcc)
    message.body = text_body
    message.html = html_body
    mail.send(message)