import re

str = "Kenny Hello, 12345X67890 Kenny"

result = re.finditer(r"Kenny", str)

for i in result:
    print(i)

# regexp