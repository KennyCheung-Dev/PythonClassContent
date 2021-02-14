rules = {}  # "AB" : "ABC"
rulesNum = {}  #"AB" : 2


for i in range(3):
    line = input().split(" ")
    rules[line[0]] = line[1]
    rulesNum[line[0]] = i + 1
line = input().split(" ")
steps = int(line[0])
start = line[1]
end = line[2]
found = False
def RecurSub(start, currentCycle, accumulatingStep):
    global found
    currentCycle += 1
    if currentCycle > steps:
        return False
    for i in range(len(start)):
        for j in range(i + 1, len(start) + 1):
            if start[i:j] in rules:
                # print("Turning " + start[i:j] + " into " + rules.get(start[i:j]) + " whole word : " + start[0:i] + rules.get(start[i:j]) + start[j:len(start)] + " steps : " + str(currentCycle))
                next = start[0:i] + rules.get(start[i:j]) + start[j:len(start)]
                newAccumulatingStep = accumulatingStep.copy()
                newAccumulatingStep.append([str(rulesNum.get(start[i:j])), str(i + 1), next])
                # [1, 2, "ABDDD"]
                if next == end:
                    if currentCycle == steps:
                        found = True
                        for line in newAccumulatingStep:
                            print(" ".join(line))
                if not found:
                    RecurSub(next, currentCycle, newAccumulatingStep)
RecurSub(start, 0, [])
# A AB
# C C
# CD CD
# 5 ABB ABBBBBBB

# A AB
# C C
# CD CD
# 1 ABB ABBB
