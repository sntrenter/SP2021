import os
from PIL import Image
path = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted0'

files = []

for r, d, f in os.walk(path):
    for file in f:
        if '.jpg' in file:
            files.append(os.path.join(r, file))

print(len(files))
print(files[0])
#print(files[0].replace("images_sorted0","images_sorted_resize"))

itor = 0

for i in files:
    print(i)
    img = Image.open(i)
    img = img.resize((256,256))
    img.save(i)
    print("saved")
    itor+=1
    #if itor >= 1:
    #    break

print("done")