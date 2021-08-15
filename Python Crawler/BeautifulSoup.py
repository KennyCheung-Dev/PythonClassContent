import os
import urllib
import urllib.request
from bs4 import BeautifulSoup


# this function will create a soup and retuens which is the parsed html format for extracting html tags of the webpage
def makeSoup(url):
    # This will load the webpage for the given url
    page = urllib.request.urlopen(url)
    # this BeautifulSoup below will parse the html file
    soup = BeautifulSoup(page, "html.parser")
    return soup


# create necessary variables
url = "https://kennycheung-dev.github.io/portfolio.github.io/Gallery.html"

soup = makeSoup(url)

# print(soup.prettify())

# match = soup.head.title.text
# print(match)

# find by class
# match = soup.find("div", class_="item4")
# print(match)


# mix find and .body
# match = soup.body.find("div", class_="item4")
# print(match)

# [attribute]
# match = soup.body.find("div", class_="item4")
# link = match.find("a")["href"]
# print(link)


# grid = soup.find("div", class_="row")
# columns = grid.findAll("div", class_="column")
# entries = []
# for column in columns:
#     for entry in column.findAll("a"):
#         # entries.append("https://kennycheung-dev.github.io/portfolio.github.io/" + entry.find("img")["src"])
# print(entries)




# for i in soup.findAll("a"):
#     print(i)
#     print()

