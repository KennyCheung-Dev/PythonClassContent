import re  #regular expression

str = "Kenny1 Hel2lo, $50 Benny3, Zen4ny ()Van2ny 12345X67890 283943802943302  Ken5ny"

# result = re.finditer(r"Kenny", str)
# result = re.finditer(r"[0-9]", str)
# result = re.finditer(r"[a-z]", str)
# result = re.finditer(r"[A-Z]", str)
# result = re.finditer(r"[a-zA-Z0-9]", str)
# result = re.finditer(r"[a-f]", str)
# result = re.finditer(r"Ken{60}y", str)
# result = re.finditer(r"Ken{60}y", str)
# result = re.finditer(r"[A-Z][a-z]nny", str)
# result = re.finditer(r"[^Kenny]", str)
# # result = re.finditer(r"..nny", str)
# result = re.finditer(r"\d", str)
# result = re.finditer(r"\w", str)
# result = re.finditer(r"\(\)", str)
# result = re.finditer(r"\\\\\\\\\\", str)


# Meta Characters (Needs to be escaped):
#    . ^ $ * + ? { } [ ] \ / ( )


''' Quantification:
*      0 or More
+      1 or More
?      0 or 1
{3}    Exactly 3
{3, 4} Range of number (min, max)
'''
# result = re.finditer(r"[A-Z][a-z]{2}[0-9]?[a-z]{2}[0-9]?", str)
# result = re.finditer(r"[A-Za-z]+[0-9]?[A-Za-z]+[0-9]?", str)

# emails = "kenny@hi.com   notEmail   hihi@kenny.com"

phone = "604-710-2313   6043210392   (103)203-2049   (203)-401-2918"
# result =re.finditer(r"[0-9]{3}[\)]", str)




# "(UpperCase, any letter)(LowerCase, any letter)nny"


urls = '''
https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
http ://wiemnfaefa
http ://wiemnfaefa.a
https://www.hoyolab.com/genshin/
https://reqres.in/api/login
reddit.com/r/Genshin_Impact/
https://www.reddit.com/r/Genshin_Impact/
https://amazondating.co/
https://genshin.mihoyo.com/en/home
https://www.google.com/maps/@49.0640375,-122.7789566,14z
https://llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk/
'''

# result = re.finditer(r"https?://(www\.)?[A-z/]+\.[A-z/]+", urls)



#Homework!!!!

#Hint:
# https://docs.python.org/3/library/re.html

website = '''
<h1>HeaderHere</h1>
<p>Hmm my paragraph</p>
<a href="www.google.com">google.com</a>
'''

result = re.findall(r"<([a-z0-9]+||a href=\"(.+)\")>(.+)</[a-z0-9]+>", website)


'''
<    (      [a-z0-9]+       ||      a href=\"(.+)\"      )   >
(.+)
<     /     [a-z0-9]+     >
'''



print(result)
# for i in result:
#     if i[0][0] == "a":
#         print("Tag: a    Content: " + i[2] + "     Link: " + i[1])
#     else:
#         print("Tag: " + i[0] + "   Content: " + i[2])
#Output: Print
'''
Tag: h1  Content: HeaderHere
Tag: p   Content: Hmm my paragraph
Tag: a   Content: google.com   Link: www.google.com
'''


s = "aljefhlasf<1>akusehfasefas<3>kajwbrgajkgaf<4><6><7><9><10><12>"
result = re.findall(r"<([0-9]+)>", s)  #Hint: () use groups
for i in result:
    print(i)

'''
1
3
4
6
7
9
10
12

'''


