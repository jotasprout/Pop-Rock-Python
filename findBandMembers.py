#!/usr/bin/python

import json

with open ('data/relationshipsAliceCooperPerson.json') as a:
    artist = json.load(a)

    artistName = artist['name']
    relations = artist['relations']

    for relation in relations:
        relativeName = relation['artist']['name']
        relativeType = relation['type']
        relplayed = relation['attributes']

        
        if relativeType == "member of band":
            print (relativeName " is a member of " artistName)
        elif relativeType == "instrumental supporting musician":
            print (relativeName " played " relplayed " for " artistName)