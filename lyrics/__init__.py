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

	s = s.replace("!", "")
	return s

def getlyrics(artist, title):

	base = "http://lyrics.wikia.com/"
	page = artist + ':' + title

	soup = BeautifulSoup(requests.get(base + page).text)
	try:
		rawLyrics = soup.select(".lyricbox")[0]
	except IndexError:
		return "" #no lyrics to be found

#	import pdb; pdb.set_trace()
	lyrics = ""
	for thing in rawLyrics.contents:
		if isinstance(thing, unicode) and '[' not in thing and 'p>' not in thing:
			lyrics += thing + " "
	return lyrics.strip()
