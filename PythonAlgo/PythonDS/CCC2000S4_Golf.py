import sys
n = int(input())
li = [sys.maxsize] * (n + 1)
li[0] = 0
clubs = []
for i in range(int(input())):
    clubs.append(int(input()))

for i in range(len(li)):
    for j in range(len(clubs)):
        if li[i] != sys.maxsize and i + clubs[j] <= n:
            li[i + clubs[j]] = min(li[i + clubs[j]], li[i] + 1)

if li[n] == sys.maxsize:
    print("Roberta acknowledges defeat.")
else:
    print("Roberta wins in " + str(li[n]) + " strokes.")


