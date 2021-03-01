import requests
import json

addkey = "?apikey=" + "DvTvDAGvJ8RY51JxS2ZWae6FKjoNFuAKB089oY9Ux4iamYuLaVF8KrHYoEaTLtfP"


def yearURL(s,e):
    return "http://api.thewalters.org/v1/objects"+addkey+"&yearBegin="+str(s)+"&yearEnd="+str(e)

def get100(page=1):
    return "http://api.thewalters.org/v1/objects"+addkey+"&PageSize=100&Page={}".format(page)
    #&medium=canvas

def main():
    print("start")

    r = requests.get(get100())
    j = json.loads(r.text)
    print(json.dumps(j["Items"][0], indent=4))
    #print(json.dumps(j["NextPage"],indent=4))
    #print(j["NextPage"] == True)
    #print(json.dumps(r.json(),indent=4,sort_keys=True))
    PAGE = 1 
    COUNT = 0
    COLLECTION = []
    CLASSIFICATION = []
    possiblegood = ['Painting & Drawing','Mosaics & Cosmati','Prints']
    goodcount = 0
    OBJECTS = {}
    OBJECTS["Items"] = []
    while True:
        r = requests.get(get100(PAGE))
        PAGE += 1
        j = json.loads(r.text)
        for i in j["Items"]:
            COUNT += 1
            if(i["Classification"] not in CLASSIFICATION):
                CLASSIFICATION.append(i["Classification"])
            if(i["Collection"] not in COLLECTION):
                COLLECTION.append(i["Collection"])

            if(i["Classification"] in possiblegood):
                goodcount += 1
                print(i["ObjectID"],"|",i["Classification"],": ",i["PrimaryImage"]["Raw"])
            
                OBJECTS["Items"].append(i)
        if(not j["NextPage"]):
            break
        #if PAGE == 5:
        #    break
        
    print(CLASSIFICATION)
    print(COLLECTION)
    print("len of OBJECTS: ", len(OBJECTS["Items"]))
    with open("OBJECTS.json",'w') as outfiles:
        json.dump(OBJECTS,outfiles)
    print("the final count of good objects is: {}".format(goodcount))
    print("the final count of objects is: {}".format(COUNT))
    print("end")

main()