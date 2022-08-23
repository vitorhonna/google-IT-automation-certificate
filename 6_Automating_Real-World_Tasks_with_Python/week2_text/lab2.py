# Great Customer Service
# John
# 2017-12-21
# The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price.
# Campared to other dealers, they provided the lowest price. Definttely recommend!

# ['Great Customer Service', 'John', '2017-12-21', 'The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!', '']

# {'title': 'Great Customer Service', 'name': 'John', 'date': '2017-12-21', 'feedback': 'The customer service here is very good. They helped me find a 2017 Camry with good condition in reasonable price. Campared to other dealers, they provided the lowest price. Definttely recommend!'}

#! /usr/bin/env python3

import os
import requests
import json


path = r'/data/feedback/'
feedbackFilenames = os.listdir(path)
# print(feedbackFilenames)

feedbacks = {}

for feedbackFilename in feedbackFilenames:
    with open(path+feedbackFilename, 'r') as feedbackHandler:
        feedback_raw = ''
        for line in feedbackHandler:
            feedback_raw += line
        feedback_contentList = feedback_raw.split('\n')
        feedback_dict = {
            'title': feedback_contentList[0],
            'name': feedback_contentList[1],
            'date': feedback_contentList[2],
            'feedback': feedback_contentList[3].replace('\n', '')
        }
        response = requests.post(
            'http://34.170.166.225/feedback/', json=feedback_dict)

        if (response.status_code == 201):
            print(f'{feedbackFilename} successfully posted!')
        else:
            print(
                f'Error posting {feedbackFilename}, status code: {response.status_code}')
