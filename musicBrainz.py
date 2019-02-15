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

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Get artist info (inc Release-Groups) from MusicBrainz
def makeReleaseGroupsURL(MusicBrainz_artistMBID):
    getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_getReleaseGroups + MusicBrainz_jsonFormat
    return getReleaseGroups_totalURL