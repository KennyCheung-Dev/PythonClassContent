import re

str = "Kenny Hello, 12345X67890"

# result = re.finditer(r"e..", str)
# result = re.finditer(r"e..", str) #.
# result = re.search(r"[0-9]*$", str).group()
# result = re.finditer(r"Ken{2}", str) #{}
# result = re.finditer(r"[a-z]", str) #[]
# result = re.finditer(r"[a-zA-Z][a-zA-Z]nny", str)  #[]nny
# result = re.finditer(r"[1-5]", str)
# result = re.finditer(r"[0-9]", str)
# result = re.finditer(r"[^0-9]", str) #^
# result = re.finditer(r"[^0-9]", str)
# result = re.finditer(r"[^\d\d\d\d\d\d\d\d\d\d\d\d]", str)  #^\d
# result = re.finditer(r"[\d\d\d\d\d\d\d\d\d\d\d\d]", str)  #\d

# MetaCharacters (Need to be escaped):
# . ^ $ * + ? { } [ ] \ | ( )

# Special Cases:

#? .
str2 = "Mr. AZ     Mr B    Ms C     Mrs. D     Mr. E"
# result = re.finditer(r"Mr\.?", str2)  #only Mr with or without .
# result = re.finditer(r"Mr\.? [a-zA-Z]+", str2)  #only Mr names
# result = re.finditer(r"Mr?s?.?\.? [a-zA-Z]+", str2)  #all names
# result = re.finditer(r"M[r|s|rs]\.? [a-zA-Z]+", str2)  #Better matches r or rs or s


'''
Quantification:
*      0 or More
+      1 or More
?      0 or 1
{3}    exactly 3 
{3, 4} range of number (min, max)


'''

emails = "kenny@hi.com       notEmail    hihi@kenny.com"
#Email:
# pattern = re.compile(r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+')
# result = pattern.finditer(emails)


#Urls:
import re

urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''
# pattern = re.compile(r'https?://(www\.)?\w+\.\w+')
# result = pattern.finditer(urls)


for i in result:
    print(i)
