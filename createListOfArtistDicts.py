#!/usr/bin/python

import json
import artistsData

basePath = '../Pop-Rock-PHP/crons/lastFM/'

myArtists = []

def get_artist_info(fromFileName):

    global myArtists

    fileName = basePath + fromFileName

    with open(fileName, 'r') as f:
        artistInfo = json.load(f)
        artist = {}
        artist['name'] = artistInfo['name']
        artist['mbid'] = artistInfo['mbid']  
        artist['type'] = artistInfo['type']
        artist['stats'] = {}
        artist['stats']['listeners'] = ''
        artist['stats']['playcount'] = ''
        myArtists.append(artist)
    f.close()
    
filenames = [
    'data/2Pac_Person_04-30-19.json',
    'data/AliceCooper_Person_04-30-19.json',
    'data/Anvil_Group_04-30-19.json',
    'data/BlackSabbath_Group_04-30-19.json',
    'data/DavidBowie_Person_04-30-19.json',
    'data/LindseyBuckingham_Person_04-30-19.json',
    'data/Eminem_Person_04-30-19.json',
    'data/Cream_Group_04-30-19.json',
    'data/DefLeppard_Group_04-30-19.json',
    'data/Dio_Group_04-30-19.json', 
    'data/Elf_Group_04-30-19.json', 
    'data/EricClapton_Person_04-30-19.json',
    'data/EvilStig_Group_04-30-19.json', 
    'data/FleetwoodMac_Group_04-30-19.json',
    'data/Heaven&Hell_Group_04-30-19.json', 
    'data/IggyandTheStooges_Group_04-30-19.json',
    'data/JanetJackson_Person_04-30-19.json', 
    'data/JimmyPage_Person_04-30-19.json',
    'data/JimmyPage&RobertPlant_Group_04-30-19.json',
    'data/JoanJett_Person_04-30-19.json', 
    'data/Journey_Group_04-30-19.json', 
    'data/LedZeppelin_Group_04-30-19.json',
    'data/MeatLoaf_Person_04-30-19.json', 
    'data/MötleyCrüe_Group_04-30-19.json', 
    'data/NeilYoung_Person_04-30-19.json',
    'data/StevieNicks_Person_04-30-19.json',
    'data/OzzyOsbourne_Person_04-30-19.json', 
    'data/RobertPlant_Person_04-30-19.json',
    'data/IggyPop_Person_04-30-19.json',
    'data/Queen_Group_04-30-19.json', 
    'data/QuietRiot_Group_04-30-19.json', 
    'data/Radiohead_Group_04-30-19.json',
    'data/Rainbow_Group_04-30-19.json', 
    'data/RonnieDioandtheProphets_Group_04-30-19.json', 
    'data/RonnieDioandtheRedCaps_Group_04-30-19.json', 
    'data/RoxyMusic_Group_04-30-19.json',
    'data/Saxon_Group_04-30-19.json', 
    'data/Stoney&Meatloaf_Group_04-30-19.json',
    'data/TedNugent_Person_04-30-19.json', 
    'data/TheAmboyDukes_Group_04-30-19.json',
    'data/TheCure_Group_04-30-19.json',
    'data/TheElectricElves_Group_04-30-19.json', 
    'data/TheFirm_Group_04-30-19.json',
    'data/TheRunaways_Group_04-30-19.json',
    'data/TheStooges_Group_04-30-19.json',
    'data/TheYardbirds_Group_04-30-19.json',
    'data/TheZombies_Group_04-30-19.json'
]

for file in filenames:
    get_artist_info(file)
    
#artistData = json.loads(artist_info_from_LastFM.text)

# Write dict to file
artistsInfoJSON = json.dumps(myArtists, indent=4)

newFilename = 'myArtistDicts' + '.json'

with open(newFilename, 'w') as n:
    n.write (artistsInfoJSON)
    n.close()

print("File written")
#pprint.pprint(artist)