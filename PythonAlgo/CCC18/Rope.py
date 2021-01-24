list = []
result = []
for i in range(int(input())):
    list.append(input())

startRight = False

def firstLetter(s):
    for i in range(len(s)):
        if s[i] != " ":
            return i
def lastLetter(s):
    for i in range(len(s) - 1, -1, -1):
        if s[i] != " ":
            return len(s) - i - 1

if firstLetter(list[-1]) == firstLetter(list[-2]):
    startRight = True
elif lastLetter(list[-1]) == lastLetter(list[-2]):
    startRight = False

goingLeft = startRight
for i in range(len(list) - 1, -1, -1):
    if goingLeft:
        for j in range(len(list[i]) - 1, -1, -1):
            if list[i][j] != " ":
                result.append(list[i][j])
        goingLeft = not goingLeft
        continue
    if not goingLeft:
        for j in range(len(list[i])):
            if list[i][j] != " ":
                result.append(list[i][j])
        goingLeft = not goingLeft
        continue

print("".join(result))