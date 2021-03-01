import json



with open('OBJECTS.json') as f:
    data = json.load(f)


print(json.dumps(data["Items"][0], indent=4))


count = 0

for i in data["Items"]:
    if i["Collection"] == "East Asian Art":
        count += 1

print(count)