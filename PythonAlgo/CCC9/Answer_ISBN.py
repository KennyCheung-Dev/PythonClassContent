# import re
#
# def ISBNCheck(s):
#     s = re.sub(r'[^\w]', '', s)
#     sum = 0
#     for i in range(9):
#         sum += (i + 1) * int(s[i])
#     print("YES") if sum % 11 == int(s[9]) else print("NO")
# ISBNCheck(input())

# def haha(ig):
#     no_dashes = ig.replace('-', '')
#     test = list(map(int, no_dashes))
#     first = int(test[0]) + int(test[1])*2 + int(test[2])*3 + int(test[4])*5 + int(test[6])*7 + int(test[7])*8 + int(test[8])*9
#     tata = first%11
#     if int(test[9])==tata:
#         return True
#     else:
#         return False
# print(haha('0-789-75198-4'))



