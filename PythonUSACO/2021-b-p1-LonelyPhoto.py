n = int(input())
cows = input()
count = 0
# for i in range(n):
#     for j in range(i + 3, n + 1):
#         photo = cows[i:j]
#         if photo.count("G") == 1 or photo.count("H") == 1:
#             count += 1
# print(count)

for i in range(3, len(cows) + 1):
    upperLimit = i - 1
    currentString = cows[0]
    accumulation = 1
    newString = cows[0]
    for j in range(1, len(cows)):
        if cows[j] == currentString:
            accumulation += 1
            if accumulation <= upperLimit:
                newString += cows[j]
        if cows[j] != currentString:
            accumulation = 1
            currentString = "G" if currentString == "H" else "H"
            newString +=  cows[j]
    # print(newString)
    for k in range(len(newString) - i + 1):
        photo = newString[k:k + i]
        # pr
        # int("photo: " + photo)
        if photo.count("G") == 1 or photo.count("H") == 1:
            count += 1
print(count)






 # currentString = "G" if currentString == "H" else "H"
