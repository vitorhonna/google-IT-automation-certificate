from email.message import EmailMessage
print()


message = EmailMessage()

sender = 'me@example.com'
recipient = 'you@example.com'
subject = 'Greetings from {} to {}!'.format(sender, recipient)
body = '''Hey there!

I'm learning to send emails using Python!'''

message['From'] = sender
message['To'] = recipient
message['Subject'] = subject
message.set_content(body)

print(message)
