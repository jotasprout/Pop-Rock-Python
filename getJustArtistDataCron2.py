#!/usr/bin/python

import requests
import json
import pprint
import time
import lastFM

date = time.strftime("%Y-%m-%d")
statsToday = {}
statsToday['date'] = date
artistsFrom = []
artistsTo = []

def getArtistListFromJSON ():
    global artistsFrom
    with open('myArtistDicts.json', 'r') as a:
        artistInfo = json.load(a)
    artistsFrom = artistInfo
    a.close()

def get_artists_data(artistVar):

    # Get artist info (inc Release-Groups) from MusicBrainz
    LastFM_artistMBID = artistVar

    get_artist_info_from_LastFM = lastFM.makeGetArtistInfoFromLastFM_URL(LastFM_artistMBID)

    artist_info_from_LastFM = requests.get(get_artist_info_from_LastFM)

    artistData = json.loads(artist_info_from_LastFM.text)

    # BUILD ARTIST DICTIONARY
    artist = {}

    artist['name'] = artistData['artist']['name']
    artist['mbid'] = LastFM_artistMBID    

    # Get Listeners and Playcount for Artist from LastFM
    artist['stats'] = {}
    LastFM_artistListeners = artistData['artist']['stats']['listeners']
    LastFM_artistPlaycount = artistData['artist']['stats']['playcount']
    artist['stats']['listeners'] = LastFM_artistListeners
    artist['stats']['playcount'] = LastFM_artistPlaycount

    print (artist)

    # Add this artist to myArtists list
    artistsTo.append(artist)


getArtistListFromJSON()

for artist in artistsFrom:
    # get artist mbid
    artistMBID = artist['mbid'] 
    # create LastFM url for artist
    # get artist stats from LastFM
    # update artist in statsToday['myArtists']
    get_artists_data(artistMBID)
    #lastFM.makeGetArtistInfoFromLastFM_URL(artistMBID) 

statsToday['myArtists'] = artistsTo
  
dateFor_file_name = time.strftime("%m-%d-%y")

artistsStatsJSON = json.dumps(statsToday, indent=4)

#absPathForFileName = '/home/roxorsox/public_html/poprock/crons/lastFM/data/daily/'

absPathForFileName = 'test_'

newFilename = absPathForFileName + dateFor_file_name + '.json'

f = open (newFilename, 'w')
f.write (artistsStatsJSON)
f.close()

print("File written")    