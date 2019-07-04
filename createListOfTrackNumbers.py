#!/usr/bin/python

import json
import artistsData

artists = []



def getTrackNumbers(fromFileName):
    artist = {}
    artist['tracks'] = []

    fileName = fromFileName

    with open(fileName, 'r') as f:
        artistData = json.load(f)
        albums = artistData['albums']
        for album in albums:
            

    LastFM_artistListeners = artistData['artist']['stats']['listeners']
    LastFM_artistPlaycount = artistData['artist']['stats']['playcount']
    artist['stats']['listeners'] = LastFM_artistListeners
    artist['stats']['playcount'] = LastFM_artistPlaycount
        artist['name'] = artistData['name']
        artist['mbid'] = artistData['mbid']  
        artist['type'] = artistData['type']
        artist['stats'] = {}
        artist['stats']['listeners'] = ''
        artist['stats']['playcount'] = ''
        blackNumbers.append(artist)
    f.close()
    
filenames = [
	'data/BlackSabbath_Group_07-02-19.json', 
    'data/Heaven&Hell_Group_07-02-19.json'
]

for file in filenames:
    getTrackNumbers(file)
    
#artistData = json.loads(artist_info_from_LastFM.text)

# Write dict to file
artistsInfoJSON = json.dumps(blackTracks, indent=4)

newFilename = 'myArtistDicts' + '.json'

with open(newFilename, 'w') as n:
    n.write (artistsInfoJSON)
    n.close()

print("File written")


