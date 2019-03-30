import json

dataDate = '02-28-19'

person = 'JoanJett_Person_'
group = 'JoanJettandtheBlackhearts_Group_'
combined = 'JoanJett_Combined_'
ext = '.json'

personFile = person + dataDate + ext
groupFile = group + dataDate + ext
combinedFile = combined + dataDate + ext

# Open file from which I will take data ("bh" for "Blackhearts")
with open(groupFile, 'r') as g:
    blackheartsJSON = json.load(g)

with open(personFile, 'r') as p:
    joanjettJSON = json.load(p)

with open(combinedFile, 'r') as c:
    combinedJSON = json.load(c)

joanjettListeners = int(joanjettJSON['stats']['listeners'])
print ('JJ has ' + str(joanjettListeners) + ' listeners')

joanjettPlays = int(joanjettJSON['stats']['playcount'])
print ('JJ has ' + str(joanjettPlays) + ' plays')

blackheartsListeners = int(blackheartsJSON['stats']['listeners'])
print ('Blackhearts have ' + str(blackheartsListeners) + ' listeners')

blackheartsPlays = int(blackheartsJSON['stats']['playcount'])
print ('Blackhearts have ' + str(blackheartsPlays) + ' plays')

# Location of combined file stats
#combinedListeners = combinedJSON['stats']['listeners']
#combinedPlays = combinedJSON['stats']['playcount']

# Add person listeners + group listeners
newcombinedListeners = joanjettListeners + blackheartsListeners
newcombinedPlays = joanjettPlays + blackheartsPlays

# Change combined file totals to new sums
combinedListeners = newcombinedListeners
combinedPlays = newcombinedPlays

print ('Combined Listeners is ' + str(combinedListeners) + ' total listeners')
print ('Combined Playcount is ' + str(combinedPlays) + ' total plays')

#with open('data/' + combinedArtistName + '_Combined_' + dataDate + '.json', 'w') as f:
#    f.write(json.dumps(blackheartsJSON))

#f.close
#print('File written.')

