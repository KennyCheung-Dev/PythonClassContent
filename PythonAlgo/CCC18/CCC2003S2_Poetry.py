vowels = ["a", "e", "i", "o", "u"]
poemsRhymes = []
# Looping through each poem
for i in range(int(input())):
    # Providing list for words
    poemsRhymes.append([])
    for j in range(4):
        lastWord = input().split(" ")[-1]
        #Check Individual Rhyme in last words
        hasVowel = False
        rhyme = ""
        for char in lastWord:
            if char in vowels:
                rhyme = ""
                rhyme += char
                hasVowel = True
            else:
                rhyme += char if hasVowel else ""
        #If there is no vowel in the last word
        if not hasVowel:
            rhyme = lastWord
        #Add rhymes into List
        poemsRhymes[i].append(rhyme)

    # Check Rhymes in each poems and print result
    if poemsRhymes[i][0] == poemsRhymes[i][1] == poemsRhymes[i][2] == poemsRhymes[i][3]:
        print("perfect")
    elif poemsRhymes[i][0] == poemsRhymes[i][1] and poemsRhymes[i][2] == poemsRhymes[i][3]:
        print("even")
    elif poemsRhymes[i][0] == poemsRhymes[i][2] and poemsRhymes[i][1] == poemsRhymes[i][3]:
        print("cross")
    elif poemsRhymes[i][0] == poemsRhymes[i][3] and poemsRhymes[i][1] == poemsRhymes[i][2]:
        print("shell")
    else:
        print("free")


