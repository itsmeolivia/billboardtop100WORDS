import re, requests
from bs4 import BeautifulSoup

def wikicase(s):
	"""Return a string in LyricWiki case.
	Substitutions are performed as described at
	<http://lyrics.wikia.com/LyricWiki:Page_Names>.
	Essentially that means capitalizing every word and substituting certain
	characters."""

	words = s.split()
	newwords = []
	for word in words:
		newwords.append(word[0].capitalize() + word[1:])
	s = "_".join(newwords)
	s = s.replace("<", "Less_Than")
	s = s.replace(">", "Greater_Than")
	s = s.replace("#", "Number_")
	s = s.replace("[", "(")
	s = s.replace("]", ")")
	s = s.replace("{", "(")
	s = s.replace("}", ")")
	return s

def getlyrics(artist, title):
	"""Raises an IOError if the lyrics couldn't be found.
	 Raises an IndexError if there is no lyrics tag."""

	base = "http://lyrics.wikia.com/"
	page = artist + ':' + title


	try:
		soup = BeautifulSoup(requests.get(base + page).text)	
	except IOError:
		raise

	try:
		rawLyrics = soup.select("lyricsbox")
	except IndexError:
		raise
	
	lyrics = []
	for line in rawLyrics:
		lyrics.append(line.find("br"))

	return lyrics