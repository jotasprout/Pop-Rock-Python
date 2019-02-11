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

# Get Release-Groups for artist from MusicBrainz
getReleaseGroups_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_getReleaseGroups + MusicBrainz_jsonFormat

responseReleaseGroups = requests.get(getReleaseGroups_totalURL)
print (responseReleaseGroups.text)