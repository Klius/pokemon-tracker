import json

new_mons = list()
with open('list.txt') as f:
    lines = f.readlines()
    for line in lines:
        line = line.replace("\n", "")
        split = line.split(" ")
        mon = {
            "index": split[0],
            "name": split[1]
        }
        new_mons.append(mon)
with open("sample.json", "w") as outfile:
    json.dump(new_mons, outfile)
