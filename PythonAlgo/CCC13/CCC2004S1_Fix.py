for i in range(int(input())):
    fixFree = True
    words = [input() for i in range(3)]
    for j in range(3):
        for k in range(3):
            if len(words[k]) <= len(words[j]) and j != k:
                if words[j][0:len(words[k])] == words[k] or \
                        words[j][len(words[j]) - len(words[k]):len(words[j])] == words[k]:
                    fixFree = False
    print("Yes" if fixFree else "No")