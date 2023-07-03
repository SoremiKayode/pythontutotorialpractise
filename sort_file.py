import os
import shutil
desktop_path = "C:/Users/kayodebarnabas.DESKTOP-N3C038F/Videos"
path = os.listdir("C:/Users/kayodebarnabas.DESKTOP-N3C038F/Desktop")

dir = "C:/Users/kayodebarnabas.DESKTOP-N3C038F/Desktop"

# os.mkdir(f"{desktop_path}/image_folder")

image_list = [image for image in path if image.endswith((".mp4", ".avi"))]
for item in image_list :
    item = os.path.join(dir, item)
    shutil.(item, dir)

# image_list = []

# for item in path :
#     image_list.append(item)

# print(image_list)

