def Bananas(word):
    for i in range(1, len(word)):
        if word[i] == "N" and Bananas(word[0:i]) and Bananas(word[i+1:len(word)+1]):
            return True
    if word[0] == "B" and word[-1] == "S" and Bananas(word[1:-1]):
        return True
    if word == "A":
        return True
    return False

while (True):
    word = input()
    if word == "X":
        break
    print(Bananas(word))



