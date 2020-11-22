# Strip the ISBN number from symbols or dashes
# 0-789-75198-4
# 0789751984
int("9")
# 1

import re

def ISBNCheck(s):
    s = re.sub(r'[^\w]', '', s)
    sum = 0
    for i in range(9):
        sum += (i + 1) * int(s[i])
    if sum % 11 == int(s[9]):
        print("YES")
    else:
        print("NO")

ISBNCheck(input())