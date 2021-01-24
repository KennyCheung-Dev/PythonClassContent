firstLine = input()
scores = []
lowestRank = []
for i in range(int(firstLine.split(" ")[0])):
    scores.append(0)
    lowestRank.append(0)
for i in range(int(firstLine.split(" ")[1])):
    round = [int(j) for j in input().split(" ")]
    for j in range(len(scores)):
        scores[j] += round[j]

    yodellerRanked = 1
    currentRank = 1
    dupScoreForRanking = scores.copy()
    while yodellerRanked <= len(scores):
        highestScore = max(dupScoreForRanking)
        for i in range(len(dupScoreForRanking)):
            if dupScoreForRanking[i] == highestScore:
                if currentRank > lowestRank[i]:
                    lowestRank[i] = currentRank
                dupScoreForRanking[i] = -2147483648
                yodellerRanked += 1
        currentRank += 1
        if currentRank < yodellerRanked:
            currentRank = yodellerRanked

winnerIndex = []
currentHigh = scores[0]
for i in range(len(scores)):
    if scores[i] == currentHigh:
        winnerIndex.append(i)
    elif scores[i] > currentHigh:
        winnerIndex.clear()
        winnerIndex.append(i)
        currentHigh = scores[i]
winnerIndex.sort()

for i in winnerIndex:
    print("Yodeller {} is the TopYodeller: score {}, worst rank {}".format(i + 1, scores[i], lowestRank[i]))
