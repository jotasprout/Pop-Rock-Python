import json

JJBh = 'JoanJettandtheBlackhearts'
JJ = 'JoanJett'

AC='AliceCooper'

dataDate = '03-16-19'

dataFolder = 'data/'
fromArtistJSON = 'AliceCooper_Group_'
toArtistJSON = 'AliceCooper_Person_'
# fromArtistJSON = 'JoanJettandtheBlackhearts_Group_'
# toArtistJSON = 'JoanJett_Person_'
ext = '.json'

fromFilename = dataFolder + fromArtistJSON + dataDate + ext
toFilename = dataFolder + toArtistJSON + dataDate + ext

# Open file from which I will take data ("b" for "band")
with open(fromFilename, 'r') as b:
    artistFrom = json.load(b)

with open(toFilename, 'r') as p:
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

with open('data/' + combinedArtistName + '_Combined_' + dataDate + '.json', 'w') as f:
    f.write(json.dumps(artistTo))

f.close
print('File written.')

