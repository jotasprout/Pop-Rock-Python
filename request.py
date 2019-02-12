import requests
import json

# MBIDs from MusicBrainz.org

aliceCooperPerson = 'ee58c59f-8e7f-4430-b8ca-236c4d3745ae'
aliceCooperBand = '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd'
blackSabbath = '5182c1d9-c7d2-4dad-afa0-ccfeada921a8'
defLeppard = '7249b899-8db8-43e7-9e6e-22f1e736024e'
dio = 'c55193fb-f5d2-4839-a263-4c044fca1456'
dioAndtheProphets = '9f6c4063-ce0a-4b71-a7b7-a32c91997260'
dioAndtheRedcaps = '883871a1-f154-4df8-a7f7-558ea456dd0a'
electricElves = '30f9591a-778b-40dd-be8f-105589f9c998'
elf = '57e0e9f3-24b5-46a6-be00-be793ca26e21'
frost = '6ab0acff-51de-45db-95cc-bdf5a6dd8578'
heavenHell = '484a1d40-0fb9-4768-acff-b570cedaacb4'
kidRock = 'ad0ecd8b-805e-406e-82cb-5b00c3a3a29e'
meatLoaf = 'b134d1bf-c7c7-4427-93ac-9fdbc2b59ef1'
stoneyMeatLoaf = '2cb3b264-277f-4d8f-bc86-1923ff8abdc0'
ozzyOsbourne = '8aa5b65a-5b3c-4029-92bf-47a544356934'
popcornBlizzard = 'dad3fb79-469f-4892-bb39-56d01a9d2485'
quietRiot = '5c6acb91-4b9b-4245-b92f-e817295c4ed0'
rainbow = 'e3cb4543-210f-499a-b0d1-3882c312dfb9'
dickWagner = 'f92d6bfd-76e7-4394-aaec-9490756eb50c'

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

# Part of URL for getting MusicBrainz Release Groups info
MusicBrainz_getReleaseGroups = '?inc=release-groups'

# Part of URL for using Release Groups MBID to get Releases
MusicBrainz_releasegroupMethod = 'release-group/'

# Part of URL for getting MusicBrainz Releases info
MusicBrainz_releases = '?inc=releases'

# Part of URL for using Release MBID
MusicBrainz_releaseMethod = 'release/'

# Part of URL for getting MusicBrainz Recordings info
MusicBrainz_recordings = '?inc=recordings'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# LastFM variables
LastFM_baseURL = 'http://ws.audioscrobbler.com/2.0/?method='

# Part of URL for getting LastFM artist info
LastFM_artistInfo = 'artist.getinfo&mbid='

# Part of URL for getting LastFM album info
LastFM_albumInfo = 'album.getinfo&mbid='

LastFM_albumMBID = '' # item in list of MusicBrainz_releaseMBID 

# Part of URL for getting LastFM track info
LastFM_trackInfo = 'track.getinfo&mbid='

LastFM_trackMBID = '' # item in list of MusicBrainz_recordingMBID 

# LastFM API key
LastFM_apiKey = '&api_key=333a292213e03c10f38269019b5f3985'

# LastFM response format
LastFM_jsonFormat = '&format=json'

# ARTIST INFO (inc Release-Groups)

# Get artist info and Release-Groups for artist from MusicBrainz
MusicBrainz_artistMBID = aliceCooperPerson

getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_getReleaseGroups + MusicBrainz_jsonFormat

responseReleaseGroups = requests.get(getReleaseGroups_totalURL)

releaseGroupsJSON = responseReleaseGroups.json()

# get Artist Stats from LastFM URL
LastFM_artistMBID = MusicBrainz_artistMBID

get_artist_info_from_LastFM = LastFM_baseURL + LastFM_artistInfo + LastFM_artistMBID + LastFM_apiKey + LastFM_jsonFormat

artist_info_from_LastFM = requests.get(get_artist_info_from_LastFM)

artistData = json.loads(artist_info_from_LastFM.text)

# START BUILDING ARTIST DICTIONARY

#create artist dict
artist = {}

artistName = releaseGroupsJSON['name']
artist['name'] = artistName

# Get Listeners and Playcount for Artist from LastFM
LastFM_artistListeners = artistData['artist']['stats']['listeners']
LastFM_artistPlaycount = artistData['artist']['stats']['playcount']

artist['stats']['listeners'] = LastFM_artistListeners
artist['stats']['playcount'] = LastFM_artistPlaycount

artistBirthday = releaseGroupsJSON['life-span']['begin']
artist['birthday'] = artistBirthday

genres = []

tags = artistData['artist']['tags']['tag']

for tag in tags:
    genre = tag['name']
    genres = genres + [genre]

artist['genres'] = genres

print (artistName + ' has ' + LastFM_artistListeners + ' listeners and ' + LastFM_artistPlaycount + ' plays.')

# GATHER MBID FOR RELEASE GROUPS

# Store MBID for each Release-Group in a list
releaseGroupsList = []
print("BEHOLD the Release-Groups:")
for releaseGroup in releaseGroupsJSON['release-groups']:
    aReleaseGroup = [] # list of ReleaseGroup properties
    releaseGroupMBID = releaseGroup['id']
    releaseGroupTitle = releaseGroup['title']
    print('- ' + releaseGroupTitle)
    #releaseGroupDate = releaseGroup['first-release-date']
    aReleaseGroup = [releaseGroupMBID, releaseGroupTitle]
    releaseGroupsList = releaseGroupsList + [aReleaseGroup]

# Get Releases of a Release-Group from MusicBrainz
for release_group in releaseGroupsList:
    MusicBrainz_releasegroupMBID = release_group[0]
    getReleases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_releasegroupMBID + MusicBrainz_releases + MusicBrainz_jsonFormat
    responseReleases = requests.get(getReleases_totalURL)
    releasesJSON = responseReleases.json()

# Create list to store MBID for all releases in a release-group
all_Releases_from_releaseGroup = []
print ("BEHOLD the Releases")
# Loop through all_Releases_from_releaseGroup list 
# For each Release, get MBID
for release in releasesJSON['releases']:
    aRelease = []
    releaseMBID = release['id']
    releaseTitle = release['title']
    releaseDate = release['date']
    releaseCountry = release['country']
    print ('- ' + releaseTitle + ' from ' + releaseCountry)
    releaseDisambiguation = release['disambiguation']
    releasePackaging = release['packaging']
    aRelease = [releaseMBID, releaseTitle, releaseDate, releaseCountry, releaseDisambiguation, releasePackaging]
    all_Releases_from_releaseGroup = all_Releases_from_releaseGroup + [aRelease]    

# Check which releases are valid albums in LastFM
# For each valid album, get listeners, and playcount
validAlbums = []
artist['validReleases'] = []

for release in all_Releases_from_releaseGroup:
    LastFM_albumMBID = release[0]
    LastFM_albumCheckURL = LastFM_baseURL + LastFM_albumInfo + LastFM_albumMBID + LastFM_apiKey + LastFM_jsonFormat
    responseCheck = requests.get(LastFM_albumCheckURL)
    albumData = json.loads(responseCheck.text)
    if "error" in albumData:
        print (LastFM_albumMBID + " does not exist in LastFM")
    else:
        thisAlbum = {}
        thisAlbum['mbid'] = albumData['album']['mbid']
        thisAlbum['name'] = albumData['album']['name']
        thisAlbum['listeners'] = albumData['album']['listeners']
        thisAlbum['playcount'] = albumData['album']['playcount']
        validAlbums = validAlbums + [thisAlbum]

artist['validReleases'] = artist['validReleases'] + [validAlbums]

# Save artist and albums info thus far
file_name = artistName.replace(' ', '')

artistJSON = json.dumps(artist)

f = open (file_name + '.json', 'w') # a is for append if artist dict already started
f.write (artistJSON)
f.close()

# For each release, get MBID for recordings on that release from MusicBrainz
for validAlbum in validAlbums:
    MusicBrainz_releaseMBID = validAlbum['mbid']
    print(validAlbum['name'] + ' is a valid album')
    getRecordings_totalURL = MusicBrainz_baseURL + MusicBrainz_releaseMethod + MusicBrainz_releaseMBID + MusicBrainz_recordings + MusicBrainz_jsonFormat
    responseRecordings = requests.get(getRecordings_totalURL)
    recordingsJSON = responseRecordings.json()
    recordingsFromRelease = json.loads(responseRecordings.text)

# Store each Recording MBID in a list
recordings = []

print ("BEHOLD the recordings")
#tracks = 

for track in recordingsFromRelease['media'][0]['tracks']:
    aRecording = {}
    aRecording['mbid'] = track['recording']['id']
    aRecording['title'] = track['recording']['title']
    print ('- ' + aRecording['title'])
    recordings = recordings + [aRecording]

print (recordings)
tracks = []

# Get Listeners and Playcount for each Track (using Recording MBID) on an Album from LastFM
for recording in recordings:
    LastFM_trackMBID = recording['mbid']
    LastFM_trackURL = LastFM_baseURL + LastFM_trackInfo + LastFM_trackMBID + LastFM_apiKey + LastFM_jsonFormat

    responseTrack = requests.get(LastFM_trackURL)
    trackData = json.loads(responseTrack.text)

    if "error" in trackData:
        print (LastFM_trackMBID + " does not exist in LastFM")
    else:
        thisTrack = {}
        thisTrack['mbid'] = trackStuff['track']['mbid']
        thisTrack['name'] = trackJSON['track']['name']
        thisTrack['stats']['listeners'] = trackJSON['track']['listeners']
        thisTrack['stats']['playcount'] = trackJSON['track']['playcount']
        trackName = thisTrack['name']
        trackListeners = thisTrack['stats']['listeners']
        trackPlaycount = thisTrack['stats']['playcount']
        print(trackName + ' has ' + trackListeners + ' listeners and ' + trackPlaycount + ' plays.')
        tracks = tracks + [thisTrack]


f = open (file_name + '.json', 'a') # a is for append if artist dict already started
f.write (tracks)
f.close()
# Questions to ask 
## Which artists, albums, tracks, have a lower listener-to-play ratio?