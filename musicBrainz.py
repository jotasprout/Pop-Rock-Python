MusicBrainz_artistMBID = ''

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

# Part of URL for getting MusicBrainz artist genres
MusicBrainz_genres = '?inc=genres'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Get artist info (inc Release-Groups) from MusicBrainz
def makeReleaseGroupsURL(MusicBrainz_artistMBID):
    getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_getReleaseGroups + MusicBrainz_jsonFormat
    return getReleaseGroups_totalURL

def makeGetReleases_totalURL(MusicBrainz_releasegroupMBID):
    getReleases_totalURL = MusicBrainz_baseURL + MusicBrainz_releasegroupMethod + MusicBrainz_releasegroupMBID + MusicBrainz_releases + MusicBrainz_jsonFormat
    return getReleases_totalURL

# Below is get releases of release group
#rels = 'https://www.musicbrainz.org/ws/2/release-group/43ac82b5-eceb-3909-a153-3c00ea9c7b9a?inc=releases&fmt=json'

def makeGetRecordings_totalURL(MusicBrainz_releaseMBID):
    getRecordings_totalURL = MusicBrainz_baseURL + MusicBrainz_releaseMethod + MusicBrainz_releaseMBID + MusicBrainz_recordings + MusicBrainz_jsonFormat
    return getRecordings_totalURL

# Get release
justRelease = ''

# Get just artist info from MusicBrainz
def makeArtistURL(MusicBrainz_artistMBID):
    getArtist_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_jsonFormat
    return getArtist_totalURL

# Get artist info with genres from MusicBrainz
def makeArtistGenresURL(MusicBrainz_artistMBID):
    getArtistGenres_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_genres + MusicBrainz_jsonFormat
    return getArtistGenres_totalURL

# Below is just artist info
#test = 'https://www.musicbrainz.org/ws/2/artist/ee58c59f-8e7f-4430-b8ca-236c4d3745ae?fmt=json'  

# Below is get recordings
# rec = 'https://www.musicbrainz.org/ws/2/release/d7c44a20-2c64-3c3a-8e6f-e865671cb56c?inc=recordings&fmt=json'