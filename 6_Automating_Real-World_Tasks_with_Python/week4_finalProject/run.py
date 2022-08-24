#!/usr/bin/env python3

import os
import requests
from os import listdir
from os.path import isfile, join

path = r'./supplier-data/descriptions/'

descriptionFilenames = [f for f in listdir(path) if isfile(join(path, f))]
# print(descriptionFilenames)

for descriptionFilename in descriptionFilenames:
    # print(descriptionFilename)
    with open(path + descriptionFilename, 'r') as fh:
        description_raw = ''
        for line in fh:
            description_raw += line
        description_list = description_raw.split('\n')
        description_dict = {
            'name': description_list[0],
            'weight': int(description_list[1].replace(' lbs', '')),
            'description': description_list[2],
            'image_name': descriptionFilename.replace('.txt', '.jpeg')
        }
        # print(description_dict)
        response = requests.post(
            'http://localhost/fruits/', json=description_dict)
        if (response.status_code == 201):
            print(f'{descriptionFilename} successfully posted!')
        else:
            print(
                f'Error posting {descriptionFilename}, status code: {response.status_code}')
