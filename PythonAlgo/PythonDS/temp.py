import re

str = "Kenny Hello, 12345X67890 Kenny Lenny Zenny"

result = re.finditer(r"[]", str)

for i in result:
    print(i)

# Homework:
# Match the following:
'''
y 
, 
0 
y 
y 
'''

# 40
