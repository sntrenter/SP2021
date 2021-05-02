import json
import csv
import requests
import rglob
import sys
import os

with open('OBJECTS.json') as f:
    data = json.load(f)


images = []
Collection = []
for i in data["Items"]:
    images.append((i["PrimaryImage"]["Raw"],i["Collection"]))
    if i["Collection"] not in Collection:
        Collection.append(i["Collection"] )
#get location
print(images[0])
print(Collection)

for i in Collection:
    path = "images_sorted\\" + i
    if not os.path.exists(path):
        print("adding ", path)
        os.mkdir(path)



nulls = 0
itor = 0
for i in images:
    if type(i[0]) != str:
        print("null found")
        nulls += 1
        continue


    image = requests.get(i[0]).content
    print(itor,":","images_sorted/"+i[1]+"/"+i[0].split("/")[-1])
    with open("images_sorted/"+i[1]+"/"+i[0].split("/")[-1], "wb") as img_file:
        img_file.write(image)
    
    #if itor > 100:
    #    break
    itor += 1



sys.exit("DONE!")
print(len(images))

filelist = rglob.rglob("Images/","*")
print(len(filelist))
print(images[0])
print(filelist[0])

def returnjustfile(x):
    return x.split('\\')[-1]

def returnjustfilefromlink(x):
    if x == None:
        return
    return x.split('/')[-1]

filelist = list(map(returnjustfile,filelist))
images_lr = list(map(returnjustfilefromlink,images))
print(len(filelist))
print(filelist[0])
print(images_lr[0])




for i in filelist:
    if i in images_lr:
        images_lr.remove(i)

print(images_lr)

nulls = 0
itor = 0
for i in images:
    if type(i) != str:
        print("null found")
        nulls += 1
        continue
    if i.split('/')[-1] not in filelist:
        print("missing file found")
        print("iteration: ",i.split('/')[-1])
        print(i)


    if i.split('/')[-1] in images_lr:
        print(i.split('/')[-1])
        image = requests.get(i).content
        with open("Images/"+i.split("/")[-1], "wb") as img_file:
            img_file.write(image)


        #if itor > 100:
        #    break
        #itor += 1

for i in filelist:
    if i in images_lr:
        images_lr.remove(i)

print(images_lr)


print(nulls)