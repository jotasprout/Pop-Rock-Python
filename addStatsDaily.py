#pL = pP = gL = gP = cL = cP = 0

#jj = 'f376828a-b438-4fda-bb2e-dcd5fbe81f83'
#bh = '46e63d3b-d91b-4791-bb73-e9f638a45ea0'

def getStats(jj, bh):
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == jj):
            pL = int(artist['stats']['listeners'])
            pP = int(artist['stats']['playcount'])
            break
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == bh):
            gL = int(artist['stats']['listeners'])
            gP = int(artist['stats']['playcount'])
            break
    print ('JJ has ' + str(pL) + ' listeners')
    print ('JJ has ' + str(pP) + ' plays')
    print ('Blackhearts have ' + str(gL) + ' listeners')
    print ('Blackhearts have ' + str(gP) + ' plays')

def addStatsDaily (pL,pP,gL,gP):
    cL = pL + gL
    cP = pP + gP

def updateJJstats(cL,cP):
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == jj):
            artist['stats']['listeners'] = pL
            artist['stats']['playcount'] = pP
            break

def deleteBH():
    global artistsTo
    for artist in artistsTo:
        artistMBID = artist['mbid']
        if (artistMBID == bh):
            del artist
            break

#getStats(jj, bh)
#addStatsDaily (pL,pP,gL,gP)
#updateJJstats(cL,cP)
#deleteBH()