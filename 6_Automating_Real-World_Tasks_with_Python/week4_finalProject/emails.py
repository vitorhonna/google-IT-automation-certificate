#!/usr/bin/env python3

import smtplib
import mimetypes
from email.message import EmailMessage
import os.path


def generate_email(sender, recipient, subject, body, attachment_path = None):
    message = EmailMessage()
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    if attachment_path != None:
        mime_type, _ = mimetypes.guess_type(attachment_path)
        mime_type, mime_subtype = mime_type.split('/', 1)
        with open(attachment_path, 'rb') as attachment:
            message.add_attachment(attachment.read(),
                                maintype=mime_type,
                                subtype=mime_subtype,
                                filename=os.path.basename(attachment_path))

    return message


def send_email(message):
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
