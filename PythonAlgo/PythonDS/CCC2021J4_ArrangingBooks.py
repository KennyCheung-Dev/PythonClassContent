line = input()
list = list(line)
list.sort()

StoM = 0
MtoS = 0
StoL = 0
LtoS = 0
MtoL = 0
LtoM = 0
for i in range(len(line)):
    if line[i] == "S" and list[i] == "M":
        StoM += 1
    if line[i] == "M" and list[i] == "S":
        MtoS += 1
    if line[i] == "S" and list[i] == "L":
        StoL += 1
    if line[i] == "L" and list[i] == "S":
        LtoS += 1
    if line[i] == "M" and list[i] == "L":
        MtoL += 1
    if line[i] == "L" and list[i] == "M":
        LtoM += 1

# print(StoM, MtoS, StoL, LtoS, MtoL, LtoM)

print(min(StoM, MtoS) + min(StoL, LtoS) + min(MtoL, LtoM) + (abs(StoM - MtoS) * 2))
