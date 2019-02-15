import json

with open('alicecooper.json', 'r') as f:
    data = f.read()

artist = json.loads(data)