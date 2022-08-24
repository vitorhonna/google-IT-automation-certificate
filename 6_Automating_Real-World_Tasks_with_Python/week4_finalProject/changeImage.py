#!/usr/bin/env python3

from PIL import Image
from os import listdir
from os.path import isfile, join

path = r'./supplier-data/images/'

imageNames = [f for f in listdir(path) if isfile(join(path, f))]

for imageName in imageNames:
    try:
        with Image.open(f"{path}/{imageName}") as im:
            # print(im.format, im.size, im.mode)
            processed_image = im.resize((600, 400)).convert("RGB")
            processed_image.save(path+imageName.replace('.tiff', '')+'.jpeg')
            # print(f"{imageName} successfully processed: ",
            #   processed_image.format, processed_image.size, processed_image.mode)
    except:
        print("cannot process:", imageName)
