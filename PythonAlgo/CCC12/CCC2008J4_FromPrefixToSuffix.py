def Converge(s):
    skips = 0
    while (len(s) > 1):
        result = []
        for i in range(len(s)):
            if skips > 0:
                skips -= 1
                continue
            if i >= len(s) - 2:
                result.append(s[i])
            else:
                if s[i] == "-" or s[i] == "+":
                    if not s[i+1] == "-" and not s[i+1] == "+":
                        if not s[i+2] == "-" and not s[i+2] == "+":
                            result.append(s[i+1] + s[i+2] + s[i])
                            skips = 2
                            continue
                result.append(s[i])
        s = result
    return s

split = []
while (True):
    s = input()
    if s == "0":
        break
    split.append(s.split(" "))

for i in range(len(split)):
    split[i] = Converge(split[i])

for i in range(len(split)):
    for j in range(len(split[i][0])):
        print(split[i][0][j], end="")
        if j != len(split[i][0]) - 1:
            print(" ", end="")
    print()