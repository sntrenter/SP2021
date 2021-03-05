import json
import csv
import math


with open('OBJECTS.json') as f:
    data = json.load(f)

#if before year zero postion 0, if after 2000, -1 else goes by 100 year incraments 
datelist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]

elist = [0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,
0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0
]

iter = 0

for i in data["Items"]:
    b = i["DateBeginYear"]
    e = i["DateEndYear"]
    m = int(e - ((e - b)/2))#mid date(what we should use)
    e = e - b#acceptable error margin
    #calculate datelist
    group = math.ceil(m/50)
    if group < 0:
        datelist[0] += 1
    #elif group > 40:#I don't think this should happen
    #    datelist[-1] += 1
    else:
        datelist[group] += 1
    #calculate errormargine buckets
    egroup = math.ceil(e/5)
    if egroup < 0:
        raise Exception("guh")
    else:
        elist[egroup] +=1
    #print(m,e,group)
    #iter += 1
    #if iter > 10:
    #    break
print(datelist)


for i in range(len(datelist)):
    if i == 0:
        print("pre 0: ",datelist[i])
    else:
        print("from {} - {}".format(i * 50 - 50,i * 50),datelist[i])


for i in range(len(elist)):
    if elist[i] == 0:
        continue
    print("error range within {} : {}".format(i * 5,elist[i]))

for i in range(len(elist)):
    if elist[i] == 0:
        continue
    print(" {} ".format(i * 5))
for i in range(len(elist)):
    if elist[i] == 0:
        continue
    print("{}".format(elist[i]))