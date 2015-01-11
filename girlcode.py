from textblob import Word, TextBlob
from bs4 import BeautifulSoup
from collections import namedtuple
from lyrics import wikicase, getlyrics
import requests, operator

def strip(word):
    result = ""
    for i in word:
        if i not in ".?,\"'-&#1234567890@()*:;[]{}<>$%^=+/\\|\n":
            result += i
    return result

if __name__ == "__main__":
    soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

    rawRows = soup.select(".row-title")

    songs = []

    for row in rawRows:

        title = wikicase(row.find("h2").text.strip())
        artiste =  (row.find("h3").text.strip())

        if "Featuring" in artiste:
            artiste = artiste[0:artiste.find("Featuring") - 1]
        artiste = wikicase(artiste)

        songs.append((title, artiste))

    vocabulary = {} #hashmap of word, number of appearances

    for title, artiste in songs:
        lyrics = getlyrics(artiste, title)

        for word in TextBlob(lyrics).words:
            normalized = Word(word).lemmatize().lower()
            if normalized not in vocabulary:
                vocabulary[normalized] = 0
            vocabulary[normalized] += 1
            
    sorted_v = sorted(vocabulary.items(), key=operator.itemgetter(1))

    f = file('output.csv', 'w')
    for word, count in sorted_v:
        f.write(word.encode('utf8') + "," + str(count) + "\n")
