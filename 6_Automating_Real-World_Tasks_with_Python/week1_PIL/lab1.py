from PIL import Image
from os import listdir
from os.path import isfile, join

path = r'./images'

imageNames = [f for f in listdir(path) if isfile(join(path, f))]

for imageName in imageNames:
    try:
        with Image.open(f"{path}/{imageName}") as im:
            # print(im.format, im.size, im.mode)
            processed_image = im.resize((128, 128)).rotate(-90).convert("RGB")
            processed_image.save('./opt/icons/'+imageName+'_processed.jpg')
    except:
        print("cannot process:", imageName)

