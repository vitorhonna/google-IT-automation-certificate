#!/usr/bin/env python3

from reports import generate_report
import getpass
import smtplib
import mimetypes
from email.message import EmailMessage
import os.path
import os
import requests
from os import listdir
from os.path import isfile, join
import emails

path = r'./supplier-data/descriptions/'

descriptionFilenames = [f for f in listdir(path) if isfile(join(path, f))]
# print(descriptionFilenames)

data = []

for descriptionFilename in descriptionFilenames:
    # print(descriptionFilename)
    with open(path + descriptionFilename, 'r') as fh:
        description_raw = ''
        for line in fh:
            description_raw += line
        description_list = description_raw.split('\n')
        description_dict = {
            'name': description_list[0],
            'weight': description_list[1],
        }
        # print(description_dict)
        data.append(description_dict)

# print(data)

if __name__ == "__main__":
    generate_report(data)
    emails.generate_email()
    emails.send_email()
