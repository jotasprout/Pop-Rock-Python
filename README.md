# PopRock with Python

## APIs that deserve and receive my gratitude
- Last.fm

## Current and Future To Do (Ideas and whatnot)
- Gather band member information

## Overall and Ongoing Purpose
Gather and wrangle data from:

### MusicBrainz
musicBrainz.py creates URLs for retrieving information using the MusicBrainz API
- Release Groups (Each album)
- Releases (Versions of each album)
- Recordings (Songs)

### Last.fm
lastFM.py creates URLs for retrieving statistics using the last.fm API about
- Artists
- Albums (using a release's MBID)
- Tracks (using a recording's MBID)

### SeatGeek

### SetList.fm -- Nope
Their API is pretty useless and their documentation is even worse. Replaced with SeatGeek.