#!/usr/bin/env python3

import reports
import os
from os import listdir
from os.path import isfile, join
import emails
from datetime import date


def parseSupplierData(path):
    descriptionFilenames = [f for f in listdir(path) if isfile(join(path, f))]
    # print(descriptionFilenames)

    attachment = '/tmp/processed.pdf'
    title = f"Processed Update on {date.today().strftime('%b %d, %Y')}"
    paragraph = ''

    for descriptionFilename in descriptionFilenames:
        # print(descriptionFilename)
        with open(path + descriptionFilename, 'r') as fh:
            description_raw = ''
            for line in fh:
                description_raw += line
            description_list = description_raw.split('\n')
            paragraph += f'name: {description_list[0]}<br/>weight: {description_list[1]}<br/><br/>'

    return attachment, title, paragraph


if __name__ == "__main__":
    attachment, title, paragraph = parseSupplierData('./supplier-data/descriptions/')
    reports.generate_report(attachment, title, paragraph)

    sender = 'automation@example.com'
    recipient = "{}@example.com".format(os.environ["USER"])
    subject = 'Upload Completed - Online Fruit Store'
    body = 'All fruits are uploaded to our website successfully. A detailed list is attached to this email.'

    message = emails.generate_email(sender, recipient, subject, body, attachment)
    emails.send_email(message)
