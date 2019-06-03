#!/usr/bin/python

import requests
import json
from pprint import pprint
import lastFM
import artistsData

artistArtGallery = []

def get_artists_Art(artistVar):
    global artistArtGallery

    LastFM_artistMBID = artistVar
    get_artist_info_from_LastFM = lastFM.makeGetArtistInfoFromLastFM_URL(LastFM_artistMBID)
    artist_info_from_LastFM = requests.get(get_artist_info_from_LastFM)
    artistData = json.loads(artist_info_from_LastFM.text)
    #pp.pprint (artistData)

    artist = {}
    artist['name'] = artistData['artist']['name']
    artistName = artist['name']
    artist['mbid'] = LastFM_artistMBID   
    artistPrettyFace = ''
    artist['prettyFace'] = '' 

    images = artistData['artist']['image']
    print(artistName)
    pprint(images)
    for image in images:
        imageSize = image['size']
        if imageSize == "extralarge":
            artistPrettyFace = image['#text']
            pprint (artistPrettyFace)
            break

    artist['prettyFace'] = artistPrettyFace
    
    print (artistName + " has an image here: " + artistPrettyFace)

    artistArtGallery.append(artist)

for mbid in artistsData.mbid_array:
    get_artists_Art(mbid)

facesJSON = json.dumps(artistArtGallery, indent=4)

newFilename = 'artistArtGallery.json'

f = open (newFilename, 'w')
f.write (facesJSON)
f.close()

print("File written with name " + newFilename)    