import requests
import json
import pprint
import lastFM
import musicBrainz
import artistsData

mbid_rels_array = [
    'ee58c59f-8e7f-4430-b8ca-236c4d3745ae', # Alice Cooper person   
    '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd', # Alice Cooper band 
    'fc4953aa-6bf4-4f1f-8e47-5ac79ca428e2', # Ronnie James Dio 
    '5182c1d9-c7d2-4dad-afa0-ccfeada921a8', # Black Sabbath  
    '79491354-3d83-40e3-9d8e-7592d58d790a' # deepPurple    
]

artistRelsDicts = [
    {
        "name": "Alice Cooper",
        "mbid": "ee58c59f-8e7f-4430-b8ca-236c4d3745ae",
        "type": "Person",
        "relations": []
    },
]

artistsFrom = []
artistsFrom = artistsRelsDicts
artistsTo = []

MusicBrainz_artistMBID = ''

# MusicBrainz variables
MusicBrainz_baseURL = 'https://www.musicbrainz.org/ws/2/'

# Part of URL for using artist MBID
MusicBrainz_artistMethod = 'artist/'

# Part of URL for getting MusicBrainz artist's artist relationships
MusicBrainz_artistArtistRels = '?inc=artist-rels'

# MusicBrainz response format
MusicBrainz_jsonFormat = '&fmt=json'

# Get just artist artist-rels from MusicBrainz

def makeArtistRelsURL(MusicBrainz_artistMBID):
    getArtist_totalURL = MusicBrainz_baseURL + MusicBrainz_artistMethod + MusicBrainz_artistMBID + MusicBrainz_artistArtistRels + MusicBrainz_jsonFormat
    return getArtist_totalURL

BlackSabbathGroup = '5182c1d9-c7d2-4dad-afa0-ccfeada921a8'
aliceCooperGroup = '4d7928cd-7ed2-4282-8c29-c0c9f966f1bd'
aliceCooperPerson = 'ee58c59f-8e7f-4430-b8ca-236c4d3745ae'

def get_artists_rels(artistVar):
    
    # Get artist relationships from MusicBrainz

    MusicBrainz_artistMBID = artistVar

    getArtistRelsFromMusicBrainz = musicBrainz.makeArtistRelsURL(MusicBrainz_artistMBID)

    ArtistRelsFromMB = requests.get(getArtistRelsFromMusicBrainz)

    artistRelsMB = json.loads(ArtistRelsFromMB.text)

    # BUILD ARTIST DICTIONARY
    artist = {}

    artist['name'] = artistRelsMB['name']

    # Get Relations for Artist from musicBrainz
    artist['relations'] = []
    relations = artistRelsMB['relations']
    #artist['relations'] = artistRelations

    for rel in relations:
        relTypeID = rel['type-id']
        # Do not want Tribute bands
        # tribute = 'a6f62641-2f58-470e-b02b-88d7b984dc9f'
        member = '5be4c609-9afa-4ea0-910b-12ffb71e3821'
        if relTypeID == member:
            aRelation = {}
            aRelation['type'] = rel['type']
            aRelation['mbid'] = rel['artist']['id']
            aRelation['name'] = rel['artist']['name']
            aRelation['attributes'] = rel['attributes']
            relations = relations + [aRelation]

    print (artist)

    # Add this artist to myArtists list
    artistsTo.append(artist)

putAllInArtistsTo()

print(len(artistsTo))

relsToday['myArtists'] = artistsTo

artistsrelsJSON = json.dumps(relsToday, indent=4)

absPathForFileName = '/home/roxorsox/public_html/poprock/data_text/relsTest'

newFilename = absPathForFileName + dateFor_file_name + '.json'

f = open (newFilename, 'w')
f.write (artistsrelsJSON)
f.close()

print("File written with name " + newFilename)  