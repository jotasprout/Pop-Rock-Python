#!/usr/bin/python

import requests
import json
import pprint
import time
import lastFM

pL = pP = gL = gP = cL = cP = 0

jj = 'f376828a-b438-4fda-bb2e-dcd5fbe81f83'
bh = '46e63d3b-d91b-4791-bb73-e9f638a45ea0'

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

def putAllInArtistsTo ():
    #global artistsFrom
    for artist in artistsFrom:
        # get artist mbid
        artistMBID = artist['mbid'] 
        # create LastFM url for artist
        # get artist stats from LastFM
        # update artist in statsToday['myArtists']
        get_artists_data(artistMBID)
        #lastFM.makeGetArtistInfoFromLastFM_URL(artistMBID) 


def getStats(jj, bh):
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == jj):
            pL = int(artist['stats']['listeners'])
            pP = int(artist['stats']['playcount'])
            break
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == bh):
            gL = int(artist['stats']['listeners'])
            gP = int(artist['stats']['playcount'])
            break
    print ('JJ has ' + str(pL) + ' listeners')
    print ('JJ has ' + str(pP) + ' plays')
    print ('Blackhearts have ' + str(gL) + ' listeners')
    print ('Blackhearts have ' + str(gP) + ' plays')

def addStatsDaily (pL,pP,gL,gP):
    cL = pL + gL
    cP = pP + gP

def updateJJstats(cL,cP):
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == jj):
            artist['stats']['listeners'] = pL
            artist['stats']['playcount'] = pP
            break
    print ('Combined has ' + str(cL) + ' listeners')
    print ('Combined has' + str(cP) + ' plays')

def deleteBH():
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == bh):
            del artist
            break

getArtistListFromJSON()
putAllInArtistsTo()

print(len(artistsTo))
getStats(jj, bh)
addStatsDaily (pL,pP,gL,gP)
updateJJstats(cL,cP)
deleteBH()
print(len(artistsTo))

statsToday['myArtists'] = artistsTo
  
dateFor_file_name = time.strftime("%m-%d-%y")

artistsStatsJSON = json.dumps(statsToday, indent=4)

#absPathForFileName = '/home/roxorsox/public_html/poprock/crons/lastFM/data/daily/'

absPathForFileName = 'test6_'

newFilename = absPathForFileName + dateFor_file_name + '.json'

f = open (newFilename, 'w')
f.write (artistsStatsJSON)
f.close()

print("File written")    