dict = {}

for i in range(int(input())):
    line = input().split(" ")
    dict[line[0]] = 2 * int(line[1]) + 3 * int(line[2]) + int(line[3])

highestName = ""
secondHighestName = ""
highestScore = -1
secondHighestScore = -2

for key, value in dict.items():
    if value > highestScore:
        secondHighestScore = highestScore
        secondHighestName = highestName
        highestScore = value
        highestName = key
        continue
    elif value == highestScore:
        if key < highestName:
            secondHighestScore = highestScore
            secondHighestName = highestName
            highestScore = value
            highestName = key
            continue
    if value > secondHighestScore:
        secondHighestScore = value
        secondHighestName = key
        continue
    elif value == secondHighestName:
        if key < secondHighestName:
            secondHighestScore = value
            secondHighestName = key
            continue
if len(dict) == 1:
    for key in dict.keys():
        print(key)
else:
    print(highestName)
    print(secondHighestName)