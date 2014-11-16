from bs4 import BeautifulSoup
import requests

soup = BeautifulSoup(requests.get("http://www.billboard.com/charts/hot-100").text)

rawRows = soup.select(".row-title")

songs = []

for row in rawRows:
    title = row.find("h2").text.strip()
    artiste = row.find("a").text.strip()
    songs.append((title, artiste))

print songs
