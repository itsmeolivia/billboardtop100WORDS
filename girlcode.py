from bs4 import BeautifulSoup
from collections import namedtuple
from lyrics import wikicase, getlyrics
import requests

soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

rawRows = soup.select(".row-title")

songs = []

for row in rawRows:

    title = wikicase(row.find("h2").text.strip())
    artiste =  (row.find("h3").text.strip())

    if "Featuring" in artiste:
        artiste = artiste[0:artiste.find("Feat") - 1]
        #TODO: the lyricsbox has [] indicating who is speaking.  I dont want that to be considered a lyric, going to have to strip
    artiste = wikicase(artiste)
    
    songs.append((title, artiste))



vocabulary = [] #hashmap of word, number of appearances
vocab_stemmed = []

stopWords = [] #fill in l8r

for title, artiste in songs:
	lyrics = getlyrics(artiste, title)

	for word in lyrics:
		if word not in stopWords: