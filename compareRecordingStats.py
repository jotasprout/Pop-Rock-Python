import json
import csv

with open('../Pop-Rock-PHP/data_text/jsonLastFM/AliceCooper_Combined_03-03-19.json', 'r') as p:
    artist = json.load(p)

artistName = artist['name']

fileLoc = '../Pop-Rock-PHP/data_text/jsonLastFM/tracks/'
artistNameFor_file_name = artistName.replace(' ', '')
thing = '_Tracks_'
dateFor_file_name = artist['date']
ext = '.csv'

tracksFileName = fileLoc + artistNameFor_file_name + thing + dateFor_file_name + ext

with open (tracksFileName, 'w') as tracksFile:
    tracksWriter = csv.writer(tracksFile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

    for album in artist['albums']:
        releases = album['releases']
        if len(releases)!=0:
            albumMBID = album['mbid']
            albumTitle = album['title']
            for release in releases:
                releaseMBID = release['mbid']
                releaseName = release['name']
                tracks = release['tracks']
                for track in tracks:
                    row = []
                    trackMBID = track['mbid']
                    trackTitle = track['title']
                    trackListeners = track['stats']['listeners']
                    trackPlaycount = track['stats']['playcount']
                    row = [albumMBID, albumTitle, releaseMBID, releaseName, trackMBID, trackTitle, trackListeners, trackPlaycount]  
                    tracksWriter.writerow(row)
                                
tracksFile.close()
print("Tracks stats written and closed")

p.close()
print("JSON file closed")