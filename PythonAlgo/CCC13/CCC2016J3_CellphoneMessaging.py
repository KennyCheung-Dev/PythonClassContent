keys = ["abc", "def", "ghi", "jkl", "mno", "pqrs", "tuv", "wxyz"]

totalTime = 0

while True:
    s = input()
    if s == "halt":
        break
    previousKey = -1
    for i in range(len(s)):
        for j in range(len(keys)):
            for k in range(len(keys[j])):
                if keys[j][k] == s[i]:
                    totalTime += k + 1;
                    if previousKey == j:
                        totalTime += 2
                    previousKey = j
    print(totalTime)
    totalTime = 0
