import json
import csv
import requests
#import Queue
import threading

with open('OBJECTS.json') as f:
    data = json.load(f)


images = []

for i in data["Items"]:
    images.append(i["PrimaryImage"]["Raw"])



def DownloadImage(url):
    if type(url) != str:
        return
    print(url)
    image = requests.get(i).content
    with open("Images2/"+url.split("/")[-1], "wb") as img_file:
        img_file.write(image)



def createNewDownloadThread(url):
    download_thread = threading.Thread(target=DownloadImage, args=(url,))
    download_thread.start()

for i in images:
    createNewDownloadThread(i)










