#!/usr/bin/env python3

import shutil
import psutil
import emails
import os
import sys
import socket


def sendAlertEmail(subject):
    sender = 'automation@example.com'
    recipient = "{}@example.com".format(os.environ["USER"])
    body = 'Please check your system and resolve the issue as soon as possible.'
    message = emails.generate_email(sender, recipient, subject, body)
    emails.send_email(message)


def checkCpuUsage():
    emailSubject = 'Error - CPU usage is over 80%'
    cpu_usage = psutil.cpu_percent(1)
    if cpu_usage > 80:
        sendAlertEmail(emailSubject)


def checkAvailableDiskSpace():
    emailSubject = 'Error - Available disk space is less than 20%'
    disk_usage = shutil.disk_usage('/')
    disk_total = disk_usage.total
    disk_free = disk_usage.used
    ratio = disk_free / disk_total * 100
    if ratio < 20:
        sendAlertEmail(emailSubject)


def checkAvailableMemory():
    emailSubject = 'Error - Available memory is less than 500MB'
    available_memory_MB = psutil.virtual_memory().available / 1024 ** 2
    if available_memory_MB < 500:
        sendAlertEmail(emailSubject)


def checkLocalhost():
    emailSubject = 'Error - localhost cannot be resolved to 127.0.0.1'
    localhost_ip = socket.gethostbyname('localhost')
    if localhost_ip != "127.0.0.1":
        sendAlertEmail(emailSubject)


checkCpuUsage()
checkAvailableDiskSpace()
checkAvailableMemory()
checkLocalhost()
