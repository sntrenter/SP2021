import json
import csv

with open('OBJECTS.json') as f:
    data = json.load(f)


h = ["order", "ObjectID", "ObjectName", "CollectionID", "Collection", "DateBeginYear",
     "DateEndYear", "DateText", "Title", "Classification", "Creator", "PrimaryImage"]

csvrows = [h]
n = 0

for i in data["Items"]:
    s = []
    s.append(str(n))
    s.append(str(i["ObjectID"]))
    s.append(str(i["ObjectName"]))
    s.append(str(i["CollectionID"]))
    s.append(str(i["Collection"]))
    s.append(str(i["DateBeginYear"]))
    s.append(str(i["DateEndYear"]))
    s.append(str(i["DateText"]))
    s.append(str(i["Title"]))
    s.append(str(i["Classification"]))
    s.append(str(i["Creator"]))
    s.append(str(i["PrimaryImage"]["Raw"]))
    csvrows.append(s)
    n += 1

for i in range(len(csvrows)):
    for j in range(len(csvrows[i])):
        csvrows[i][j] = str(csvrows[i][j].encode("utf-8"))[2:-1]

with open('OBJECTS.csv', 'w',newline='') as f:
    # for item in csv:
    #    f.write(str("{}\n".format(item).encode("utf-8")))
    writer = csv.writer(f)
    writer.writerows(csvrows)
