import re
l1 = re.sub(r'[^\w]', '', input())
l2 = re.sub(r'[^\w]', '', input())
print(l1)
print(l2)
dict1 = {}
dict2 = {}
for i in l1:
    if i in dict1:
        dict1[i] += 1
    else:
        dict1[i] = 1
for i in l2:
    if i in dict2:
        dict2[i] += 1
    else:
        dict2[i] = 1
if dict1==dict2:
    print("Is an anagram.")
else:
    print("Is not an anagram.")