# LastFM variables
LastFM_baseURL = 'http://ws.audioscrobbler.com/2.0/?method='

# Part of URL for getting LastFM artist info
LastFM_artistInfo = 'artist.getinfo&mbid='

LastFM_artistMBID = ''

# Part of URL for getting LastFM album info
LastFM_albumInfo = 'album.getinfo&mbid='

LastFM_albumMBID = ''

# LastFM API key
LastFM_apiKey = '&api_key=333a292213e03c10f38269019b5f3985'

# LastFM response format
LastFM_jsonFormat = '&format=json'

# Total LastFM URL
LastFM_totalURL = LastFM_baseURL + LastFM_artistInfo + LastFM_MBID + LastFM_apiKey + LastFM_jsonFormat

# Other LastFM
LastFM_artistListeners = ''
LastFM_artistPlaycount = ''
LastFM_albumListeners = ''
LastFM_albumPlaycount = ''

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

MusicBrainz_artistMBID = ''

# Part of URL for using Release Groups MBID
MusicBrainz_releasegroupMethod = 'release-group/'

MusicBrainz_releasegroupMBID = ''

# Part of URL for getting MusicBrainz Release Groups info
MusicBrainz_releaseGroups = '?inc=release-groups'

# Part of URL for getting MusicBrainz Releases info
MusicBrainz_releases = '?inc=releases'

# Part of URL for using Release MBID
MusicBrainz_releaseMethod = 'release/'

MusicBrainz_releaseMBID = ''

# Part of URL for getting MusicBrainz Recordings info
MusicBrainz_recordings = '?inc=recordings'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Total MusicBrainz URL
MusicBrainz_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat

# Get Release-Groups for artist from MusicBrainz
releaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat

# Get Releases for a Release-Group from MusicBrainz
releases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_MBID + MusicBrainz_releaseGroups + MusicBrainz_apiKey + jsonFormat

# Get MBID for artist
# Store MBID for each Release-Group in an array
# Loop through Release-Group array
# For each Release-Group, get MBID for releases in that group
# Store MBID for each release in an array
# Loop through Releases array 
# For each Release, get MBID for recordings on that release
# Store MBID for each Recording in an array

f = open ('artist.json', 'a') # a is for append if artist dict already started
f.write ('variable goes here for data from MusicBrainz')
f.close()

response = requests.get('https://en.wikipedia.org/wiki/Nobel_Prize')