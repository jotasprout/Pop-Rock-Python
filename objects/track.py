#!/usr/bin/python

class Track(object):
    def __init__(self, mbid):
        self.mbid = mbid
        self.title = ''
        self.release = ''
        self.artist = ''
        self.
        

    def set_release (releaseMBID):
        self.releaseMBID = releaseMBID

    def set_albumTitle(albumTitle):
        self.albumTitle = albumTitle

    def set_trackTitle(trackTitle):
        self.trackTitle = trackTitle
    
    def describe(self):
        return "{} is track #{} from {} by {}".format(self.title, self.trackNumber, self.releaseTitle, self.artistName)