import json

with open('dicionario.json', 'r') as revertendo:
    valoresjson = json.load(revertendo)

for i in valoresjson:
    print(i.values())