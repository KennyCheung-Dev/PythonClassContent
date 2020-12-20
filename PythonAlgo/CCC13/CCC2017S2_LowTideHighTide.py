n = int(input())

li = input()
li = [int(i) for i in li.split(" ")]
li.sort()

lowIndex = int((len(li) / 2) - 1 if n % 2 == 0 else len(li) / 2)
highIndex = int(len(li) / 2 if n % 2 == 0 else (len(li) / 2) + 1)

tides = []

while True:
    if lowIndex >= 0:
        tides.append(li[lowIndex])
    if highIndex < len(li):
        tides.append(li[highIndex])
    lowIndex -= 1
    highIndex += 1
    if lowIndex < 0 and highIndex >= len(li):
        break

for i in range(len(tides)):
    print(tides[i], end="")
    if i != len(tides) - 1:
        print(" ", end="")
