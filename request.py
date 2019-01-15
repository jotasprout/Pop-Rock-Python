baseURL = 'https://www.musicbrainz.org'

# Part of URL for getting MusicBrainz artist info

# Get MBID for artist
# Get Release-Groups for artist
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

