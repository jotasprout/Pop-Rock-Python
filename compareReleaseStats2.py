import json
import artistsData

# Open file from which I will take data ("b" for "band")
with open('data/AliceCooper_Combined_03-03-19.json', 'r') as p:
    artist = json.load(p)

#for album in artist['albums']:
#    for release in album['releases']:
#        print (release['name'] + " with MBID " + release['mbid'] + " has " + release['playcount'] + " plays and " + release['listeners'] + " listeners.") 

for album in artist['albums']:
    releases = album['releases']
    if len(releases)!=0:
        albumMBID = album['releases'][0]['mbid']
        albumName = album['releases'][0]['name']
        albumListeners = album['releases'][0]['listeners']
        albumPlaycount = album['releases'][0]['playcount']
        print (albumName + " with MBID " + albumMBID + " has " + albumPlaycount + " plays and " + albumListeners + " listeners.") 