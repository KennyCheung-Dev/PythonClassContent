size = int(input());
ai = []
line = input()
ai = [int(i) for i in line.split(" ")]

ai.sort()

happyCount = 0;
currentEntry = ai[0];
ai.pop(0)
currentIndex = 0;
while len(ai) > 0:
    if ai[currentIndex] > currentEntry:
        currentEntry = ai[currentIndex]
        ai.pop(currentIndex)
        happyCount+=1
        currentIndex = 0
    else:
        if currentIndex + 1 < len(ai):
            currentIndex+=1
        else:
            currentEntry = ai[0]
            ai.pop(0)
            currentIndex = 0
print(happyCount)