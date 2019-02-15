import json

with open('AliceCooperPerson.json', 'r') as f:
    data = f.read()

artist = json.loads(data)