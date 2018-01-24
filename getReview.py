#!usr/bin/python3
#Author: SanipRijal

import urllib.request
from bs4 import BeautifulSoup as soup
import urllib.parse as uparse
import re

class AppURLOpener(urllib.request.FancyURLopener):
	version = "Mozilla/5.0"
opener = AppURLOpener()

#ask the user for the name of movie
movie_name = input("Enter the movie name: ")
movie_name = re.sub(r"\s+", "_", movie_name)	#replace blankspaces with underscore in the movie name
url = "https://www.rottentomatoes.com/m/" + movie_name #urll for the movie

uClient = opener.open(url)	#open the url 	
html = uClient.read()	#read the html page
uClient.close()

page_soup = soup(html, "html.parser")	

#get the div from the page with class 'media-body'
divs = page_soup.find_all('div', attrs={"class":"media-body"})


review = []	#create a list to store the reviews

#loop through the ResultSet obtained
for x in divs:
	r = (x.find('p'))	#find the 'p' tag
	ch = ["<p>", "</p>", "None"]

	#to replace the texts like '<p>', '</p>' and 'None' from the reviews
	for c in ch:
		if c in str(r):
			r = str(r).replace(c, "")
	print(r)

	#add the reviews to the list
	review.append(r)

	#write the reviews into a file named 'reviews.txt'
	with open("reviews.txt", "w") as reviewfile:
		for item in review:
			reviewfile.write("%s\n" %item)

