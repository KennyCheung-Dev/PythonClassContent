import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

# this function will create a soup
def makeSoup(url):
    # This will load the webpage for the given url
    page = urllib.request.urlopen(url)
    # this BeautifulSoup below will parse the html file
    soup = BeautifulSoup(page, "html.parser")
    return soup

url = "https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html"

soup = makeSoup(url)

# match = soup.head.link
# print(match)

# match = soup.find("head").find("link")
# print(match)

# match = soup.findAll("p")
# for eachMatch in match:
#     print(eachMatch)

# Homework
# Match all a tags that is under a div tag that has a class "item?"





print()
print()

print(soup.prettify())



