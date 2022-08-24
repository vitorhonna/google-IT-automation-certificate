import getpass
import smtplib
import mimetypes
from email.message import EmailMessage
import os.path

print()

# Create message
message = EmailMessage()

# Compose message
sender = 'vitorhonna.dev@gmail.com'
recipient = 'vitorhonna@gmail.com'
subject = 'Greetings from {} to {}!'.format(sender, recipient)
body = '''Hey there!
I'm learning to send emails using Python!'''

message['From'] = sender
message['To'] = recipient
message['Subject'] = subject
message.set_content(body)

# Add attachment
attachment_path = r'./example.png'
attachment_filename = os.path.basename(attachment_path)

mime_type, _ = mimetypes.guess_type(attachment_path)
mime_type, mime_subtype = mime_type.split('/', 1)
# print(mime_type, mime_subtype)

with open(attachment_path, 'rb') as attachment:
    message.add_attachment(attachment.read(),
                           maintype=mime_type,
                           subtype=mime_subtype,
                           filename=os.path.basename(attachment_path))

# print(message)

# Send message through an SMTP server
mail_server = smtplib.SMTP_SSL('smtp.gmail.com')
mail_pass = getpass.getpass('Password? ')
mail_server.login(sender, mail_pass)

mail_server.send_message(message)
mail_server.quit()