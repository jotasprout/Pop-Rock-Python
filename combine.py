import json

acb15 = 'data/AliceCooperBand_021519.json'
acp15 = 'data/AliceCooperPerson_021519.json'

def combineArtistsFiles(artist01, artist02):
    a1 = open(artist01, 'r')
    artistFrom = json.loads(a1)
    a1.close()
    a2 = open (artist02, 'r')
    artistTo = json.loads(a2)
    a2.close()
    artistFromAlbums = artistFrom['albums']
    print ('Band has ' + len(artistFromAlbums) + ' albums')
    artistToAlbums = artistTo['albums']
    print ('Person has ' + len(artistToAlbums) + ' albums')
    artistToAlbums = artistToAlbums + artistFromAlbums
    print ('There are ' + len(artistToAlbums) + ' total  combined albums')
    print ('artistTo now has ' + len(artist02['albums']) + ' total albums')
    combinedArtistName = artistTo['name'].replace(' ', '')
    combinedArtistJSON = json.dumps(artistTo)
    f = open(combinedArtistName + '.json', 'w')
    f.write(combinedArtistJSON)
    f.close
    print('File written.')

combineArtistsFiles(acb15, acp15)