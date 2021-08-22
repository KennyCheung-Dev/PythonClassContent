import re

str = "Kenn2 ]ello, 12345X67890 -enn9 1ennv Zennh"

result = re.finditer(r"...", str)

for i in result:
    print(i)

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

# Points: 77
