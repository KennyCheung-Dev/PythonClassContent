# regex
# regexp
# regular expression

import re

str = "Hello, Kenny  3Regnny nny Rexnny 6Quadnny Deny Hello, Danny    Hello, Rexjs,  Hello, Hex Hello Redx , Hello 12345X67890"
'''
Kenny
Regnny
nny
Rexnny
Quadnny
Danny
'''
#??nny
# Goal: A
# ll English Letters
# result = re.finditer(r"[0-9a-zA-Z]", str) # Numbers and Letters
# result = re.finditer(r"Hello, [A-VY-Za-vy-z]{5}", str) #Not any name with an x
# # result = re.finditer(r"[^0-9a-z]", str) #Not ^
# result = re.finditer(r"[A-Za-z]{5}", str)
# result = re.finditer(r"[a-zA-Z]*nny", str)
# result = re.finditer(r"\d{3}", str)

#\d


str2 = "Mr. AZ   Mr B   Ms C    Mrs. D    Mr. E"
# result = re.finditer(r"Mr\.?\ [A-Za-z]+", str2) # only Mr with or without .
# result = re.finditer(r"Mr [A-Za-z]+", str2) # only Mr names without .
# result = re.finditer(r"Mr?s?\.? [A-Za-z]+", str2) # All names
# result = re.finditer(r"(Mr|Mrs|Ms)\.? [A-Za-z]+", str2)
# result = re.finditer(r"M(r|rs|s)\.? [A-Za-z]+", str2)

nums = '''
604-710-2031
302-214-2313
425-326-7244
123-535-2623
213121313123
932-32-3
324-123-4522
911-911-9111
'''

result = re.finditer(r"\d{3}\-\d{3}\-\d{4}", nums)

'''
Mr. AZ
Mr B
Mr. E
'''

for i in result:
    print(i.group())

'''
Quantification:
*       0 or More
+       1 or More
?       ? 0 or 1
{3}     exactly 3
{3, 4}  range of number (min, max)

'''

'''
Matching conditions:
\d = numbers
\D = ncharacter that is not a decimal digit

\w an character which is word letters or numbers
\W any character which is not a word character

'''

#Homework:

emails = '''
kenny@hi.com
fe@sef.sith
efefefefefefef.efefef.ef.ef.ef.ef
notEmail
hihi@kenny.com
ke.fsefjis@gmail.com
rex@rex.rex
rex@rex.com
danny@rex.gov
'''

#not that .gov  .com are correct website, sith isn't  .rex isn't



urls = '''
http://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
http://rex.com
'''
