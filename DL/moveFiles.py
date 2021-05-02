from shutil import copyfile
import random


import os
from PIL import Image
path = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted0'

path1 = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_with_valid\data\\18th and 19th Century Art'
path2 = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_with_valid\data\\East Asian Art'





def movefiles(path):
    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))
    j = 0
    for i in files:
        if(random.random() < .20):
            copyfile(i ,i.replace("data","Validation"))
        else:
            copyfile(i ,i.replace("data","Training"))
        j+=1
        #if j > 10:
        #    break
    print(j)

def main():
    movefiles(path1)
    movefiles(path2)


main()

print("done")

