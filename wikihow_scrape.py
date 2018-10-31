import json
with open("data/src/travel.json") as f:
    data_root = json.load(f)

f = open("data/travel/wikihow.txt", "a")

def recurse(data):
    global flag
    if data["children"]:
        for i in data["children"]:
            recurse(i)

    for i in data["content"]:
        f.write(i["name"] + "\n")

recurse(data_root)

f.close()
