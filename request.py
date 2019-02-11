import requests
import json

# Get MBID for artist
# By going to MusicBrainz.org and search
# Refer to blog post on next line for instructions
# https://jotascript.wordpress.com

aliceCooperPerson = 'ee58c59f-8e7f-4430-b8ca-236c4d3745ae'
aliceCooperBand = '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd'

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

MusicBrainz_artistMBID = aliceCooperPerson

# Part of URL for getting MusicBrainz Release Groups info
MusicBrainz_getReleaseGroups = '?inc=release-groups'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Total MusicBrainz URL
MusicBrainz_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_releaseGroups + MusicBrainz_jsonFormat

# LastFM variables
LastFM_baseURL = 'http://ws.audioscrobbler.com/2.0/?method='

# Part of URL for getting LastFM artist info
LastFM_artistInfo = 'artist.getinfo&mbid='

LastFM_artistMBID = MusicBrainz_artistMBID

# Part of URL for getting LastFM album info
LastFM_albumInfo = 'album.getinfo&mbid='

LastFM_albumMBID = '' # item in array of MusicBrainz_releaseMBID 

# Part of URL for getting LastFM album info
LastFM_trackInfo = 'track.getinfo&mbid='

LastFM_trackMBID = '' # item in array of MusicBrainz_recordingMBID 

# LastFM API key
LastFM_apiKey = '&api_key=333a292213e03c10f38269019b5f3985'

# LastFM response format
LastFM_jsonFormat = '&format=json'

# Total LastFM URL
LastFM_totalURL = LastFM_baseURL + LastFM_artistInfo + LastFM_artistMBID + LastFM_apiKey + LastFM_jsonFormat

# Get Listeners and Playcount for Artist from LastFM
LastFM_artistListeners = ''
LastFM_artistPlaycount = ''

# Get Release-Groups for artist from MusicBrainz
getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_getReleaseGroups + MusicBrainz_jsonFormat

responseReleaseGroups = requests.get(getReleaseGroups_totalURL)
print (responseReleaseGroups.text)
releaseGroupsJSON = responseReleaseGroups.json()

#create artist dict
artist = {}

artistName = releaseGroupsJSON['name']
artist['name'] = artistName
file_name = artistName.replace(' ', '')

artistBirthday = releaseGroupsJSON['life-span']['begin']
artist['birthday'] = artistBirthday

artistJSON = json.dumps(artist)

f = open (file_name + '.json', 'a') # a is for append if artist dict already started
f.write (artistJSON)
f.close()

# Store MBID for each Release-Group in a list
releaseGroupsList = []

for releaseGroup in releaseGroupsJSON['release-groups']:
    aReleaseGroup = [] # list of ReleaseGroup properties
    releaseGroupMBID = releaseGroup['id']
    releaseGroupTitle = releaseGroup['title']
    releaseGroupDate = releaseGroup['first-release-date']
    aReleaseGroup = [releaseGroupMBID, releaseGroupTitle, releaseGroupDate]
    releaseGroupsList = releaseGroupsList + [aReleaseGroup]

MusicBrainz_releasegroupMBID = releaseGroupsList[0][0]

# Part of URL for using Release Groups MBID to get Releases
MusicBrainz_releasegroupMethod = 'release-group/'

# Part of URL for getting MusicBrainz Releases info
MusicBrainz_releases = '?inc=releases'

# Get Releases of a Release-Group from MusicBrainz
getReleases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_releasegroupMBID + MusicBrainz_releases + MusicBrainz_jsonFormat

responseReleases = requests.get(getReleases_totalURL)

releasesJSON = responseReleases.json()

# Create list to store MBID for each release
all_Releases_from_releaseGroup = []
validAlbums = []

# Loop through all_Releases_from_releaseGroup list 
# For each Release, get MBID
for release in releases['releasesJSON']:
    aRelease = []
    releaseMBID = release['id']
    releaseTitle = release['title']
    releaseDate = release['date']
    releaseCountry = release['country']
    releaseDisambiguation = release['disambiguation']
    releasePackaging = release['packaging']
    aRelease = [releaseMBID, releaseTitle, releaseDate, releaseCountry, releaseDisambiguation, releasePackaging]
    all_Releases_from_releaseGroup = all_Releases_from_releaseGroup + [aRelease]    

# Check which releases are valid albums in LastFM
# For each album, get listeners, and playcount
# Get Listeners and Playcount for each Album (using Release MBID) by an Artist
LastFM_albumListeners = ''
LastFM_albumPlaycount = ''

for release in releases:
    LastFM_albumMBID = release[0]
    LastFM_albumCheckURL = LastFM_baseURL + LastFM_albumInfo + LastFM_albumMBID + LastFM_apiKey + LastFM_jsonFormat
    responseCheck = requests.get(LastFM_albumCheckURL)
    albumData = json.loads(responseCheck.text)
    if "error" in albumData:
        print (LastFM_albumMBID + " does not exist in LastFM")
    else:
        print (LastFM_albumMBID + " has " + albumData['album']['listeners'] + " listeners and " + albumData['album']['playcount'] + " plays")
        validAlbums = validAlbums + [LastFM_albumMBID]

print ('These are the valid albums: ' + validAlbums)

# For each release, get MBID for recordings on that release from MusicBrainz

# Part of URL for using Release MBID
MusicBrainz_releaseMethod = 'release/'

MusicBrainz_releaseMBID = all_Releases_from_releaseGroup[0][0]

# Part of URL for getting MusicBrainz Recordings info
MusicBrainz_recordings = '?inc=recordings'

getRecordings_URL = MusicBrainz_baseURL + MusicBrainz_releaseMethod + MusicBrainz_releaseMBID + MusicBrainz_recordings + MusicBrainz_jsonFormat

responseRecordings = requests.get(getRecordings_URL)

recordingsJSON = responseRecordings.json()

# Store each Recording MBID in a list
recordings = []

for recording in recordingsJSON['recordings']:
    aRecording = []
    recordingMBID = recording['id']
    recordingTitle = recording['title']
    recordingDate = recording['date']
    recordingCountry = recording['country']
    recordingDisambiguation = recording['disambiguation']
    recordingPackaging = recording['packaging']
    aRecording = [recordingMBID, recordingTitle, recordingDate, recordingCountry, recordingDisambiguation, recordingPackaging]
    recordings = recordings + [aRecording]

# Get Recording info from LastFM
MusicBrainz_recordingMBID = ''

# Get Listeners and Playcount for each Track (using Recording MBID) on an Album
LastFM_trackListeners = ''
LastFM_trackPlaycount = ''

# Questions to ask 
## Which artists, albums, tracks, have a lower listener-to-play ratio?