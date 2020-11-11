import re
def ISBNCheck(s):
    s = re.sub(r'[^\w]', '', s)
    sum = 0
    for i in range(9):
        sum += (i+1) * int(s[i])
    print("YES") if sum % 11 == int(s[9]) else print("NO")

ISBNCheck(input())