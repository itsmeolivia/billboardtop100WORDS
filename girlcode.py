from bs4 import BeautifulSoup
from collections import namedtuple
from lyrics import wikicase, getlyrics
import requests

def strip(word):
    result = ""
    for i in word:
        if i not in ".?,\"'-&#1234567890@()*:;[]{}<>$%^=+/\\|\n":
            result += i
    return result

def wordCount(string):
    word_count = {}
    line = strip(string)
    for word in line:
        if word not in word_count:
            word_count[i] = 0
        word_count[i] += 1
    return word_count

if __name__ == "__main__":
    soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

    rawRows = soup.select(".row-title")

    songs = []

    for row in rawRows:

        title = wikicase(row.find("h2").text.strip())
        artiste =  (row.find("h3").text.strip())

        if "Featuring" in artiste:
            artiste = artiste[0:artiste.find("Featuring") - 1]
            #TODO: the lyricsbox has [] indicating who is speaking.  I dont want that to be considered a lyric, going to have to strip
            artiste = wikicase(artiste)
            songs.append(title, artiste)



        vocabulary = {} #hashmap of word, number of appearances
        vocab_stemmed = {}

        stopWords = [] #fill in l8r

        for title, artiste in songs:
            lyrics = getlyrics(artiste, title)

	    for word in lyrics:
            if word not in stopWords
