import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

#This function will make a soup
def makeSoup(url):
    page = urllib.request.urlopen(url)
    soup = BeautifulSoup(page, "html.parser")
    return soup

def performScraping(urlReceived, folderName, numImages):
    counter = 0
    soup = makeSoup(urlReceived)

    for image in soup.findAll('img', {'class':'s-item__image-img'}):
        if counter < numImages:
            nameOfFile = image['alt']
            nameOfFile = nameOfFile.replace('/', '-')
            nameOfFile = nameOfFile.replace('\\', '-')
            img = image['src']
            tempCheck = img.split('.')
            check = str(tempCheck[-1])
            finalImageType = '.png'
            if check == 'jpg' or check == 'jpeg' or check == 'png':
                if check == 'jpg' or check == 'jpeg':
                    finalImageType = '.jpeg'
                else:
                    finalImageType = '.png'
                folderIndividualName = folderName + "/" #Path for your image to go towards
                # Create folder according to the search name
                if not os.path.exists(folderIndividualName):
                    os.makedirs(folderIndividualName)
                imageFile = open(folderIndividualName + nameOfFile + finalImageType, 'wb')
                imageFile.write(urllib.request.urlopen(img).read())
                imageFile.close()
        counter += 1


#create necessary variables
standard_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0"
keyword = 'Marvel Spiderman' #keyword we want to search for
num_image = 10 #how many images we want
key_url = standard_url.format('+'.join(keyword.split(" ")))

performScraping(key_url, "EbayImagesOnSpiderman", 4)

# Homework:
# Download 10 photos of other topic of your choice
# Review the code, I will ask questions next week