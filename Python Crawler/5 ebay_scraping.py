import os
import urllib
import urllib.request
from bs4 import BeautifulSoup

#this function will create a soup and retuens which is the parsed html format for extracting html tags of the webpage
def makeSoup(url):
    #This will load the webpage for the given url
    page = urllib.request.urlopen(url) 
    #this BeautifulSoup below will parse the html file
    soup = BeautifulSoup(page, "html.parser")
    return soup



#This function will be called every new keyword line is encountered and will start scraping the amazon web page of the search result according to the text mention in the keywords text file
def perfromScraping(urlReceived, folderName, breakPointNumber):
    breaki = 1
    url = urlReceived #This will hold the url addres
    soup = makeSoup(url)
    print("Folder Name is ", folderName)

    i = 1
    for image in soup.findAll('img', {'class':'s-item__image-img'}):
        if(breaki <= breakPointNumber): #This statement checks the number of images that were restricted to which were supposed to be downloaded
            #print(image)
            print("Image number ", i ," : \n", image.get('src'), "\n")
            i = i+1
            breaki = breaki + 1

            nameOfFile = image.get('alt')
            nameOfFile = nameOfFile.replace('/','-')
            img = image.get('src')
            tempCheck = img.split('.')
            check = str(tempCheck[len(tempCheck) - 1])
            ImageType = ".jpeg"
            if (check == "jpg" or check == "jpeg" or check == "png"):

                if check == "jpg" or check == "jpeg":
                    ImageType = ".jpeg"
                else:
                    ImageType = ".png"

                filename = nameOfFile
                folderIndividualName = "EbayImages/" + folderName + "/" #Creates the path where the images will be sto
                #Create The folder according to search name
                if not os.path.exists(folderIndividualName):
                    os.makedirs(folderIndividualName)
                imageFile = open(folderIndividualName + filename + ImageType, 'wb')
                imageFile.write(urllib.request.urlopen(img).read()) #This will read the image file from the link and download it and save it in the folder mentioned all at the same time
                imageFile.close()

        

#create necessary variables                 
standard_url = "https://www.ebay.com/sch/i.html?_from=R40&_trksid=p2380057.m570.l1313&_nkw={}&_sacat=0"
keyword = 'marvel t shirt' #keyword we want to search for
num_image = 10 #how many images we want 
key_url = standard_url.format('+'.join(keyword.split()))



#start scraping 
perfromScraping(key_url, keyword, num_image)

