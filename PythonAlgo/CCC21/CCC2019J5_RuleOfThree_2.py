rules = [] # ["AB", "ABB"],
rulesReversed = []

for i in range(3):
    line = input().split(" ")
    rules.append([line[0], line[1], i + 1])
    rulesReversed.append([line[1], line[0], i + 1])

line = input().split(" ")
steps = int(int(line[0]) / 2)
secondHalfSteps = int(line[0]) - steps
start = line[1]
end = line[2]

firstHalfResult = []
firstHalfSequence = {}
secondHalfResult = []
secondHalfSequence = {}

finished = False

#Do FirstHalf
def RecurSub(start, currentCycle, accumulatingStep, rules, isFirstHalf):
    global finished
    if finished:
        return False
    currentCycle += 1
    if currentCycle > (steps if isFirstHalf else secondHalfSteps):
        return False
    for i in range(len(start)):
        for j in range(i + 1, len(start) + 1):
            if isFirstHalf:
                for ruleKey, ruleValue, ruleNum in rules:
                    if start[i:j] == ruleKey:
                        newAccumulatingStep = accumulatingStep.copy()
                        next = start[0:i] + ruleValue + start[j:len(start)]
                        newAccumulatingStep.append([str(ruleNum), str(i + 1), next])
                        if currentCycle == steps:
                            if next not in firstHalfResult:
                                firstHalfResult.append(next)
                                firstHalfSequence[next] = newAccumulatingStep
                        RecurSub(next, currentCycle, newAccumulatingStep, rules, isFirstHalf)
            else:
                for ruleKey, ruleValue, ruleNum in rulesReversed:
                    if start[i:j] == ruleKey:
                        newAccumulatingStep = accumulatingStep.copy()
                        next = start[0:i] + ruleValue + start[j:len(start)]
                        newAccumulatingStep.append([str(ruleNum), str(i + 1), start])
                        if currentCycle == secondHalfSteps:
                            if next in firstHalfResult:
                                secondHalfResult.append(next)
                                secondHalfSequence[next] = newAccumulatingStep
                                finished = True
                        RecurSub(next, currentCycle, newAccumulatingStep, rules, isFirstHalf)


RecurSub(start, 0, [], rules, True)

RecurSub(end, 0, [], rulesReversed, False)

found = False

for i in firstHalfResult:
    if found:
        break
    for j in secondHalfResult:
        if i == j:
            for k in firstHalfSequence[i]:
                print(" ".join(k))
            for l in reversed(secondHalfSequence[j]):
                print(" ".join(l))
            found = True
            break

