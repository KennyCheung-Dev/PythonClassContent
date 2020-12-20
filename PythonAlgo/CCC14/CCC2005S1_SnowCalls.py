keys = [[],[],[],[],[],[],[],[],[],[]]
keys[2] = ["A", "B", "C"]
keys[3] = ["D", "E", "F"]
keys[4] = ["G", "H", "I"]
keys[5] = ["J", "K", "L"]
keys[6] = ["M", "N", "O"]
keys[7] = ["P", "Q", "R", "S"]
keys[8] = ["T", "U", "V"]
keys[9] = ["W", "X", "Y", "Z"]

for i in range(int(input())):
    result = ""
    s = input()
    for j in range(len(s)):
        if s[j] != "-":
            try:
                temp = int(s[j])
                result += str(temp)
            except:
                for k in range(len(keys)):
                    if s[j] in keys[k]:
                        result += str(k)
        if len(result) == 3 or len(result) == 7:
            result += "-"
    print(result[0:12])




