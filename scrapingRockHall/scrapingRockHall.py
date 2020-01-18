from bs4 import BeautifulSoup
import requests

BASE_URL = 'http://en.wikipedia.org/'
# Or
# BASE_URL = 'List of Rock and Roll Hall of Fame inductees - Wikipedia.html'
# Try each to see (and document) the difference(s)

# To fool it into thinking we're a browser
HEADERS = {'User-Agent': 'Mozilla/5.0'}

def get_RockHall_soup():
    response = requests.get(
        BASE_URL + 'wiki/List_of_Rock_and_Roll_Hall_of_Fame_inductees', 
        headers=HEADERS
    )
    return BeautifulSoup(response.content, "lxml") # Why lxml? What is other option?

soup = get_RockHall_soup()

