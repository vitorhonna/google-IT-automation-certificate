from PIL import Image
from os import listdir
from os.path import isfile, join

path = r'./images'

imageNames = [f for f in listdir(path) if isfile(join(path, f))]

# for imageName in imageNames:
#     print(imageName)

imageName = r'ic_add_location_black_48dp'

imageObject = Image.open(f"{path}/{imageName}")
new_image = imageObject.rotate(90)
new_image.save(f"dfgfgfdgfdgdfgdf_processed.jpg")
