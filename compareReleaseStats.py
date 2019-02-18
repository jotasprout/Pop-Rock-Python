import json
import artistsData

# Open file from which I will take data ("b" for "band")
with open(artistsData.acp15, 'r') as p:
    artist = json.load(p)

#for release in artist['albums'][0]['releases']:
#    print (release['name'] + " has " + release['playcount'] + " plays") 


# Get a list of keys from dictionary which has the given value

def getKeysByValue(dictOfElements, valueToFind):
    listOfKeys = list()
    listOfItems = dictOfElements.items()
    for item  in listOfItems:
        if item[1] == valueToFind:
            listOfKeys.append(item[0])
    return  listOfKeys

# Get list of keys with value 43

listOfKeys = getKeysByValue(artist, 43)
 
print("Keys with value equal to 43")
#Iterate over the list of keys
for key  in listOfKeys:
        print(key)