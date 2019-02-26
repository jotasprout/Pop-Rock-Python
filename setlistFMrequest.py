import requests
import json

setlistFM_baseURL = 'https://api.setlist.fm/rest'

setlistFM_totalURL = setlistFM_baseURL + desiredGet + desired + headers

def build_setlistFM_URL(desiredGet, desired):
    setlistFM_totalURL = setlistFM_baseURL + desiredGet + desired

r = requests.get(setlistFM_totalURL, headers={"accept":"application/json", "x-api-key":"4d1da9b2-7794-4d0d-84e3-cd132f55c949"})

# r.text

# Detroit urbanized area ID
detroit = '23824'

# Ann Arbor urbanized area ID
annarbor = '02602'

get_city = '/1.0/city/{geoId}'

city = ''

get_venues = '/1.0/search/venues'
get_venue = '/1.0/venue/{venueId}'
venue = ''

# setlistFM also uses MBID for artists
get_artists = '/1.0/search/artists'
get_artist = '/1.0/artist/{mbid}'
artist = ''
