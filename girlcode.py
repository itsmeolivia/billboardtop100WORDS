from bs4 import BeautifulSoup
from collections import namedtuple
import requests, lyrics

soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

rawRows = soup.select(".row-title")

songs = []

for row in rawRows:
    title = wikicase(row.find("h2").text.strip())
    artiste = wikicase(row.find("a").text.strip())

    songs.append((title, artiste))
