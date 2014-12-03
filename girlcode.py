from bs4 import BeautifulSoup
from collections import namedtuple
from lyrics import wikicase
import requests

soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

rawRows = soup.select(".row-title")

songs = []

for row in rawRows:
    #title =

    title = wikicase(row.find("h2").text.strip())
    artiste =  (row.find("h3").text.strip())

    if "Featuring" in artiste:
        artiste = artiste[0:artiste.find("Feat") - 1]
    artiste = wikicase(artiste)
    
    songs.append((title, artiste))
