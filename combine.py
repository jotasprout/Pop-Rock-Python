import json

# Open file from which I will take data ("b" for "band")
with open('data/AliceCooperBand_021519.json', 'r') as b:
    artistFrom = json.load(b)

with open('data/AliceCooperPerson_021519.json', 'r') as p:
    artistTo = json.load(p)

artistFromAlbums = artistFrom['albums']
print ('Band has ' + str(len(artistFromAlbums)) + ' albums')

artistToAlbums = artistTo['albums']
print ('Person has ' + str(len(artistTo['albums'])) + ' albums')

artistToAlbums = artistToAlbums + artistFromAlbums
print ('There are ' + str(len(artistToAlbums)) + ' total combined albums')

artistTo['albums'] = artistToAlbums
print ('artistTo now has ' + str(len(artistTo['albums'])) + ' total albums')

newArtistToAlbums = artistTo['albums']
print ('artistTo really has ' + str(len(newArtistToAlbums)) + ' albums')

combinedArtistName = artistTo['name'].replace(' ', '')

with open(combinedArtistName + '.json', 'w') as f:
    f.write(json.dumps(artistTo))

f.close
print('File written.')

