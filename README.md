# PopRock with Python

These scripts support Pop-Rock-PHP with the following tasks:

- Get information from MusicBrainz about artists, their albums, and tracks
- Get data from Last.fm (listeners and playcounts)
- Extra data preparation tasks required for some artists

## MusicBrainz

*musicBrainz.py* creates URLs for retrieving information using the [MusicBrainz API](https://musicbrainz.org/doc/MusicBrainz_API/Examples)

- Release Groups (Each album)
- Releases (Versions of each album)
- Recordings (Songs)
- Relationships (band members and other personnel)

### MusicBrainz Documentation

[Beginners Guide](https://musicbrainz.org/doc/Beginners_Guide)

## Last.fm

*lastFM.py* creates URLs for retrieving listener statistics from multiple platforms using the [last.fm API](https://www.last.fm/api) about

- Artists
- Albums (using a release's MBID)
- Tracks (using a recording's MBID)

## ListenBrainz.org

[ListenBrainz.org](https://listenbrainz.org/) includes these helpful pages:

- [Main Documentation](https://listenbrainz.readthedocs.io/en/production/)
- [ListenBrainz API](https://listenbrainz.readthedocs.io/en/production/dev/api.html)
- [JSON Documentation](https://listenbrainz.readthedocs.io/en/production/dev/json.html)

## SeatGeek

Now using using the [SeatGeek API](http://platform.seatgeek.com/) because both the API and its documentation are far superior to setlist.fm.

## SetList.fm -- Nope

Their API is pretty useless and their documentation is even worse. Replaced with SeatGeek.
