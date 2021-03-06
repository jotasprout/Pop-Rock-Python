#!/usr/bin/python

import requests
import json
#import pprint
#import time
import lastFM
import artistsData

#date = time.strftime("%Y-%m-%d")
#statsData = {}
#artistsFrom = []
#artistsFrom = artistsData.myArtistDicts
artistsTo = []

def get_artists_data(artistVar):
    global artistsTo

    LastFM_artistMBID = artistVar
    get_artist_info_from_LastFM = lastFM.makeGetArtistInfoFromLastFM_URL(LastFM_artistMBID)
    artist_info_from_LastFM = requests.get(get_artist_info_from_LastFM)
    artistData = json.loads(artist_info_from_LastFM.text)

    artist = {}
    artist['name'] = artistData['artist']['name']
    artist['mbid'] = LastFM_artistMBID    
    genres = []

    #def makeGenres():
    tags = artistData['artist']['tags']['tag']
    for tag in tags:
        genre = tag['name']
        genres = genres + [genre]
    artist['genres'] = genres

    print (artist)

    artistsTo.append(artist)

for mbid in artistsData.mbid_array:
    get_artists_data(mbid)

genresJSON = json.dumps(artistsTo, indent=4)

newFilename = 'genres.json'

f = open (newFilename, 'w')
f.write (genresJSON)
f.close()

print("File written with name " + newFilename)    