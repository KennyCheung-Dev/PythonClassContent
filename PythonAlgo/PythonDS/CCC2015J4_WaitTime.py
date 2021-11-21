'''
CCC '15 J4 - Wait Time
https://dmoj.ca/problem/ccc15j4
'''
WaitTime = {}
WaitingQueue = {}
previousCommand = ""
for i in range(int(input())):

    line = input().split()
    if line[0] == "R":
        if previousCommand == "R" or previousCommand == "S":
            for j in WaitingQueue.keys():
                WaitingQueue[j] += 1
        if line[1] not in WaitingQueue:
            WaitingQueue[line[1]] = 0
    elif line[0] == "S":
        if previousCommand == "R" or previousCommand == "S":
            for j in WaitingQueue.keys():
                WaitingQueue[j] += 1
        if line[1] in WaitTime:
            WaitTime[line[1]] += int(WaitingQueue[line[1]])
        else:
            WaitTime[line[1]] = int(WaitingQueue[line[1]])
        WaitingQueue.pop(line[1])
    elif line[0] == "W":
        for j in WaitingQueue.keys():
            WaitingQueue[j] += int(line[1])
    previousCommand = line[0]

for personWhoNeverGotReplied in WaitingQueue.keys():
    WaitTime[personWhoNeverGotReplied] = -1

WaitTime = sorted(WaitTime.items(),  key=lambda x: x[0])

for key, value in WaitTime:
    print(key, value)
