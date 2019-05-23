#!/usr/bin/python

import requests
import json
import pprint
import time
import lastFM

date = time.strftime("%Y-%m-%d")
thisStart = time.time()

# ARTIST STATS
#print ("Getting Artist stats from LastFM")
#print (" ")

# CREATE ARTISTS DICT
statsToday = {}
statsToday['date'] = date

# START BUILDING ARTISTS LIST

myArtists = []
statsToday['myArtists'] = myArtists

def get_artists_data(artistVar):

    # Get artist info (inc Release-Groups) from MusicBrainz
    LastFM_artistMBID = artistVar

    get_artist_info_from_LastFM = lastFM.makeGetArtistInfoFromLastFM_URL(LastFM_artistMBID)

    artist_info_from_LastFM = requests.get(get_artist_info_from_LastFM)

    artistData = json.loads(artist_info_from_LastFM.text)

    # BUILD ARTIST DICTIONARY
    artist = {}

    artist['name'] = artistData['name']
    artist['mbid'] = LastFM_artistMBID    

    # Get Listeners and Playcount for Artist from LastFM
    artist['stats'] = {}
    LastFM_artistListeners = artistData['artist']['stats']['listeners']
    LastFM_artistPlaycount = artistData['artist']['stats']['playcount']
    artist['stats']['listeners'] = LastFM_artistListeners
    artist['stats']['playcount'] = LastFM_artistPlaycount

    # Add this artist to myArtists list
    statsToday['myArtists'] = statsToday['myArtists'] + artist

basePath = '../Pop-Rock-PHP/crons/lastFM/'

myArtists = []

def get_artist_info(fromFileName):

    global myArtists

    fileName = basePath + fromFileName

    with open(fileName, 'r') as f:
        artistInfo = json.load(f)
        artist = {}
        artist['name'] = artistInfo['name']
        artist['mbid'] = artistInfo['mbid']  
        artist['type'] = artistInfo['type']
        artist['stats'] = {}
        artist['stats']['listeners'] = ''
        artist['stats']['playcount'] = ''
        myArtists.append(artist)
    f.close()
    
for mbid in artistsData.mbid_array_justArtistData:
    get_artists_data(mbid)

thisEnd = time.time()
duration = thisEnd - thisStart
statsToday['taskDuration'] = {}
statsToday['taskDuration']['Task Start'] = thisStart
statsToday['taskDuration']['Task End'] = thisEnd
statsToday['taskDuration']['Task Duration'] = duration

# Write statsToday to file

dateFor_file_name = time.strftime("%m-%d-%y")

artistsStatsJSON = json.dumps(statsToday, indent=4)

absPathForFileName = '/home/roxorsox/public_html/poprock/crons/lastFM/data/daily/'

newFilename = absPathForFileName + dateFor_file_name + '.json'

f = open (newFilename, 'w')
f.write (artistsStatsJSON)
f.close()

print("File written")
#pprint.pprint(artist)