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

url = "https://kennycheung-dev.github.io/portfolio.github.io/Project.html"

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
# match = soup.find("div", class_="item1").a
# print(match)
# match = soup.find("div", class_="item2").a
# print(match)
# match = soup.find("div", class_="item3").a
# print(match)
# match = soup.find("div", class_="item4").a
# print(match)
# match = soup.find("div", class_="item5").a
# print(match)

# Attributes:
# use []
# match = soup.find("div", class_="item5").a["href"]
# print(match)

# Text wrapped around a tag:
# use .text
# match = soup.find("div", class_="item5").a.text
# print(match)

#
match = soup.findAll("h2")
print(match)




#Homework
#Link: https://kennycheung-dev.github.io/portfolio.github.io/Project-Kaboom.html
#Get all images src, not including top banner, and video

print()
print()

print(soup.prettify())



