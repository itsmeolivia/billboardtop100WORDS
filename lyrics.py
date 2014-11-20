import urllib, sys, os, re
from bs4 import BeautifulSoup

def lyricwikicase(s):
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
	s = s.replace("#", "Number_") # FIXME: "Sharp" is also an allowed substitution
	s = s.replace("[", "(")
	s = s.replace("]", ")")
	s = s.replace("{", "(")
	s = s.replace("}", ")")
	return s

def lyricwikiurl(artist, title, edit=False, fuzzy=False):
	"""Return the URL of a LyricWiki page for the given song, or its edit
	page"""

	if fuzzy:
		base = "http://lyrics.wikia.com/index.php?search="
		pagename = artist + ':' + title
		if not edit:
			url = base + pagename
			doc = lxml.html.parse(url)
			return doc.docinfo.URL
	else:
		base = "http://lyrics.wikia.com/"
		pagename = lyricwikipagename(artist, title)
	if edit:
		if fuzzy:
			url = base + pagename
			doc = lxml.html.parse(url)
			return doc.docinfo.URL + "&action=edit"
		else:
			return base + "index.php?title=%s&action=edit" % pagename
	return base + pagename


def getlyrics(artist, title, fuzzy=False):
	"""Get and return the lyrics for the given song.
	Raises an IOError if the lyrics couldn't be found.
	Raises an IndexError if there is no lyrics tag."""

	try:
		#getting lyrics
	except IOError:
		raise

	try:
		#parsing for them
	except IndexError:
		raise

	# prepare output
	lyrics = []
