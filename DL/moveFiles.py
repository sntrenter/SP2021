from shutil import copyfile, move
import random


import os
from PIL import Image
#path = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted0'
#
#path1 = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_with_valid\data\\18th and 19th Century Art'
#path2 = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_with_valid\data\\East Asian Art'
#

test_east_asian = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_valid_train\\data\\East Asian Art'
test_19and19 = r'C:\\Users\sntre\Documents\\GitHub\SP2021\DL\\images_sorted_x256_valid_train\\data\\18th and 19th Century Art'


#test


def movefiles(path,teststring):
    files = []

    for r, d, f in os.walk(path):
        for file in f:
            if '.jpg' in file:
                files.append(os.path.join(r, file))
    j = 0
    for i in files:
        num = random.random()
        if(num < .30):
            if(num < .1):
                #test
                copyfile( i , i.replace("data", teststring))
            if (num < .3):
                #valid
                copyfile(i ,i.replace("data","Validation"))
        else:
            #train 
            copyfile(i ,i.replace("data","Training"))
            
        j+=1
        #if j > 50:
        #    break
    print(j)

def main():
    movefiles(test_east_asian, r"Testing\\Test East Asian Art")
    #movefiles(test_19and19, r"Testing\\Test 18th and 19th Century Art")


main()

print("done")

