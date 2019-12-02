#!/usr/bin/python

import json
import artistsData

basePath = '../Pop-Rock-PHP/crons/lastFM/'

myArtists = []

filenames2 = []

filenames = [
    'data/BlackSabbath_Group_12-01-19.json',
    'data/Dio_Group_12-01-19.json', 
    'data/Elf_Group_12-01-19.json', 
    'data/TheElectricElves_Group_12-01-19.json', 
    'data/Heaven&Hell_Group_12-01-19.json', 
	'data/Rainbow_Group_09-24-19.json12-01-19.json',
    'data/RonnieDioandtheProphets_Group_12-01-19.json', 
    'data/RonnieDioandtheRedCaps_Group_12-01-19.json',
    'data/KerryLivgren_Person_12-01-19.json',
    'data/RogerGlover_Person_12-01-19.json'          
]

def find_best_release(releaseGroup):
    releaseGroup = releaseGroup


def get_artist_info(fromFileName):

    global myArtists

    fileName = fromFileName

    with open(fileName, 'r') as f:
        artistInfo = json.load(f)
        artist = {}
        artist['name'] = artistInfo['name']
        artist['mbid'] = artistInfo['mbid']  
        artist['type'] = artistInfo['type']
        artist['stats'] = {}
        artist['stats']['listeners'] = ''
        artist['stats']['playcount'] = ''
        artist['genres'] = artistInfo['genres']
        artist['birthday'] = artistInfo['birthday']
        jsonAlbumsList = artistInfo['albums']
        artist['albums'] = []
        albums = artist['albums']

        def get_album_info(thisRelease):
            global albums
            thisAlbum = {}
            thisAlbum['name'] = thisRelease['name']
            thisAlbum['mbid'] = thisRelease['mbid']
            thisAlbum['stats'] = {}
            thisAlbum['stats']['listeners'] = ''
            thisAlbum['stats']['playcount'] = ''
            thisAlbum['date'] = thisRelease['date']
            thisAlbum['country'] = thisRelease['country']
            thisAlbum['disambiguation'] = thisRelease['disambiguation']
            thisAlbum['packaging'] = thisRelease['packaging']
            thisAlbum['tracks'] = []
            thisAlbum['tracks'] = thisRelease['tracks']
            tracks = thisAlbum['tracks']
            for track in tracks:
                track['stats']['listeners'] = ''
                track['stats']['playcount'] = ''
            albums = albums + ['thisAlbum']
        
        for album in jsonAlbumsList:
            releasesList = []
            releasesList = album['releases']
            thisRelease = {}
            for jsonRelease in releasesList:
                if jsonRelease['country'] == 'US':
                    thisRelease = jsonRelease
                    get_album_info(thisRelease)
                    break
                else:
                    thisRelease = releasesList[0]
                    get_album_info(thisRelease)
            #get_album_info(thisRelease)
            
    # Write artist to file
    artistName = artist['name']
    artistNameFor_file_name = artistName.replace(' ', '')

    artistTypeFor_file_name = artistType

    artistJSON = json.dumps(artist, indent=4)

    absPathFor_file_name = '/home/roxorsox/public_html/poprock/crons/lastFM/templates/'

    newFilename = absPathFor_file_name + artistNameFor_file_name + '_' + artistTypeFor_file_name  + 'TEMPLATE' + '.json'

    encodedFilename = newFilename.encode('utf-8')

    f = open (encodedFilename, 'w')
    f.write (artistJSON)

    f.close()

for file in filenames2:
    get_artist_info(file)
    
#artistData = json.loads(artist_info_from_LastFM.text)

# Write dict to file
artistsInfoJSON = json.dumps(myArtists, indent=4)

newFilename = 'myBigArtistDicts' + '.json'

with open(newFilename, 'w') as n:
    n.write (artistsInfoJSON)
    n.close()

print("File written")
#pprint.pprint(artist)