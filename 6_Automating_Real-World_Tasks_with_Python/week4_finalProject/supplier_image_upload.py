#!/usr/bin/env python3
import requests
from os import listdir
from os.path import isfile, join

path = r'./supplier-data/images/'

imageNames = [f for f in listdir(path) if (f.endswith('.jpeg'))]
# print(imageNames)

url = "http://localhost/upload/"
for imageName in imageNames:
    with open(path + imageName, 'rb') as opened:
        r = requests.post(url, files={'file': opened})
