import json

with open('../Pop-Rock-PHP/data_text/jsonLastFM/AliceCooper_Combined_03-03-19.json', 'r') as p:
    artist = json.load(p)

for album in artist['albums']:
    releases = album['releases']
    if len(releases)!=0:
        albumMBID = album['releases'][0]['mbid']
        albumName = album['releases'][0]['name']
        albumListeners = album['releases'][0]['listeners']
        albumPlaycount = album['releases'][0]['playcount']
        print (albumName + " with MBID " + albumMBID + " has " + albumPlaycount + " plays and " + albumListeners + " listeners.") 