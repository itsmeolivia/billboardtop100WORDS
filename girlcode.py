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

def getSongs(row):
    title = wikicase(row.find("h2").text.strip())
    artiste =  (row.find("h3").text.strip())

    if "Featuring" in artiste:
        artiste = artiste[0:artiste.find("Featuring") - 1]
    artiste = wikicase(artiste)

    return title, artiste

if __name__ == "__main__":

    soups = []

    soup_page0 = BeautifulSoup(requests.get("http://www.billboard.com/charts/r-b-hip-hop-songs").text)
    soup_page1 = BeautifulSoup(requests.get("http://www.billboard.com/charts/r-b-hip-hop-songs?page=1").text)
    soup_page2 = BeautifulSoup(requests.get("http://www.billboard.com/charts/r-b-hip-hop-songs?page=2").text)

    soups.extend([soup_page0, soup_page1, soup_page2])
    songs = []

    for soup in soups:
        rawRows = soup.select(".row-title")
        for row in rawRows:
            title, artiste = getSongs(row)
            songs.append((title, artiste))

    vocabulary = {} #hashmap of word, number of appearances

    unordered_list = file('output_rb.txt', 'w')
    for title, artiste in songs:
        lyrics = getlyrics(artiste, title)

        for word in TextBlob(lyrics).words:
            normalized = Word(word).lemmatize().lower()
            if normalized not in vocabulary:
                vocabulary[normalized] = 0
            vocabulary[normalized] += 1
            unordered_list.write(word.encode('utf8') + '\n')

    sorted_v = sorted(vocabulary.items(), key=operator.itemgetter(1))

    f = file('output_rb.csv', 'w')
    for word, count in sorted_v:
        f.write(word.encode('utf8') + "," + str(count) + "\n")
