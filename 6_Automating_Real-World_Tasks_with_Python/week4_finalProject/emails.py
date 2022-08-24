import smtplib
import mimetypes
from email.message import EmailMessage
import os.path
import report_email


def generate_email():
    # TODO
    print()


def send_email():
    message = EmailMessage()
    sender = 'automation@example.com'
    recipient = 'student-00-bc16a9a2075a@example.com'
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'
    message['From'] = sender
    message['To'] = recipient
    message['Subject'] = subject
    message.set_content(body)

    attachment_path = 'processed.pdf'
    attachment_filename = os.path.basename(attachment_path)
    mime_type, _ = mimetypes.guess_type(attachment_path)
    mime_type, mime_subtype = mime_type.split('/', 1)
    with open(attachment_path, 'rb') as attachment:
        message.add_attachment(attachment.read(),
                               maintype=mime_type,
                               subtype=mime_subtype,
                               filename=os.path.basename(attachment_path))
    mail_server = smtplib.SMTP('localhost')
    mail_server.send_message(message)
    mail_server.quit()
