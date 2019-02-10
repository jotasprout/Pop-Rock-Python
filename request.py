import requests

# Get MBID for artist
# By going to MusicBrainz.org and search
# Refer to blog post on next line for instructions
# https://jotascript.wordpress.com

aliceCooperPerson = 'ee58c59f-8e7f-4430-b8ca-236c4d3745ae'
aliceCooperBand = '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd'

# Loop through Releases array 
# For each Release, get MBID for recordings on that release
# Store MBID for each Recording in an array

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

MusicBrainz_artistMBID = aliceCooperPerson

# Part of URL for getting MusicBrainz Release Groups info
MusicBrainz_releaseGroups = '?inc=release-groups'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Get Release-Groups for artist from MusicBrainz
getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_releaseGroups + MusicBrainz_jsonFormat

response = requests.get(getReleaseGroups_totalURL)
# print (response.text)
responseJSON = response.json()

artistName = responseJSON['name']
artistBirthday = responseJSON['life-span']['begin']
#print(artistBirthday)
# Store MBID for each Release-Group in an array
artistReleaseGroups = []

for releaseGroup in responseJSON['release-groups']:
    aReleaseGroup = []
    releaseGroupMBID = releaseGroup['id']
    releaseGroupTitle = releaseGroup['title']
    releaseGroupDate = releaseGroup['first-release-date']
    aReleaseGroup = [releaseGroupMBID, releaseGroupTitle, releaseGroupDate]
    artistReleaseGroups = artistReleaseGroups + [aReleaseGroup]

#print (artistReleaseGroups)

#for i in artistReleaseGroups:
#    print(i[0] + ' on ' + i[1])

# constrictor = '24c4fdde-4494-3837-a288-5b4fdbe966eb'

MusicBrainz_releasegroupMBID = artistReleaseGroups[0][0]

# Part of URL for using Release Groups MBID to get Releases
MusicBrainz_releasegroupMethod = 'release-group/'

# Part of URL for getting MusicBrainz Releases info
MusicBrainz_releases = '?inc=releases'

# Get Releases for a Release-Group from MusicBrainz
releases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_releasegroupMBID + MusicBrainz_releases + MusicBrainz_jsonFormat

response2 = requests.get(releases_totalURL)
# print (response.text)
response2JSON = response2.json()
#print (response2JSON)
# Loop through Release-Group array
# For each Release-Group, get MBID for releases in that group

# Store MBID for each release in an array
releases = []
# Loop through each release in the release array
for release in response2JSON['releases']:
    aRelease = []
    releaseMBID = release['id']
    releaseTitle = release['title']
    releaseDate = release['date']
    releaseCountry = release['country']
    releaseDisambiguation = release['disambiguation']
    releasePackaging = release['packaging']
    aRelease = [releaseMBID, releaseTitle, releaseDate, releaseCountry, releaseDisambiguation, releasePackaging]
    releases = releases + [aRelease]    

#print(releases)

# Part of URL for using Release MBID
MusicBrainz_releaseMethod = 'release/'

# Part of URL for getting MusicBrainz Recordings info
MusicBrainz_recordings = '?inc=recordings'

# Get Recordings for a Release from MusicBrainz
#recordings_totalURL = MusicBrainz_baseURL + MusicBrainz_releaseMethod + MusicBrainz_releaseMBID + MusicBrainz_recordings + MusicBrainz_jsonFormat

#response3 = requests.get(releases_totalURL)
# print (response.text)
#response3JSON = response3.json()

# For each Release, get MBID for all Recordings and store them in an array
recordings = []

#for recording in response3JSON['recordings']:
#    aRecording = []
 #   recordingMBID = recording['id']
  #  recordingTitle = recording['title']
   # recordingDate = recording['date']
    #recordingCountry = recording['country']
#    recordingDisambiguation = recording['disambiguation']
#    recordingPackaging = recording['packaging']
#    aRecording = [recordingMBID, recordingTitle, recordingDate, recordingCountry, recordingDisambiguation, recordingPackaging]
#    recordings = recordings + [aRecording]

#print (recordings)

# Store MBID for Recordings in an array

# Recording MBID isn't used at MusicBrainz but at LastFM
MusicBrainz_recordingMBID = ''

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

for release in releases:
    LastFM_albumMBID = release[0]
    LastFM_albumCheckURL = LastFM_baseURL + LastFM_albumInfo + LastFM_albumMBID + LastFM_apiKey + LastFM_jsonFormat
    responseCheck = requests.get(LastFM_albumCheckURL)
    print (responseCheck.text)

# With this array of releases, check each release in the response for 
# error '6'
# if no error '6' get
# albumListeners and
# albumPlaycount

# Other LastFM
LastFM_artistListeners = ''
LastFM_artistPlaycount = ''
LastFM_albumListeners = ''
LastFM_albumPlaycount = ''
LastFM_trackListeners = ''
LastFM_trackPlaycount = ''

# Get artist Listeners and Playcount from LastFM

# Get Listeners and Playcount for each Album (using Release MBID) by an Artist

# Get Listeners and Playcount for each Track (using Recording MBID) on an Album

# f = open ('artist.json', 'a') # a is for append if artist dict already started
# f.write ('variable goes here for data from MusicBrainz')
# f.close()

# Questions to ask 
## Which artists, albums, tracks, have a lower listener-to-play ratio?