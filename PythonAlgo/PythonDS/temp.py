import re

str = "Kenn2 ]ello, 12345X67890 -enn9 1ennv Zennh"

str2 = "<header><h2>Hmmmmmm</h2><a href=\"google.com\">Link</a></header>"
str3 = "<header></header>"
str4 = "<header>lkfjgdshrlklifgjgjpwiot4ulersogw]]][]t4ueohsu4ghrosu</header>"

result = re.finditer(r"<header>", str2)


for i in result:
    print(i)

'''
Quantification
*       0 or More
+       1 or More 
?       0 or 1
{3}     exactly 3
{3, 6}  between of 3 to 6
'''

# Homework: 10 points
# Match the following:
'''
nn2
, 1
234
5X6
789
nn9
'''

# Points: 140
