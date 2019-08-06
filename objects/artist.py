#!/usr/bin/python

class Artist(object):
    def __init__(self, name):
        self.name = name
    
    def get_stats(self):
        # either get stats from my DB or LastFM