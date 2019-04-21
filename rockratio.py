import json
import artistList

dataDate = '04-21-19'

dataFolder = 'data/'
artist = ''
ext = '.json'

def makeFilename(artistName):
    filename = dataFolder + artistName + dataDate + ext
    return filename

def makeArtist(artistName):
    artist = {}
    artist['name'] = artistName
    artist['stats'] = {}

for artist in artistList.artistList:
    artistThing = artist
    filename = makeFilename(artistThing)
    with open(filename, 'r') as a:
        artistJSON = json.load(a)
        name = artistJSON['name']
        #makeArtist(artistName)
        artistListeners = int(artistJSON['stats']['listeners'])
        artistPlaycount = int(artistJSON['stats']['playcount'])
        playsFloat = round(artistPlaycount/artistListeners)
        playsStr = str(playsFloat)
        print (name + "'s Listener-to-Plays ratio is " + playsStr + " plays per Listener.")
        