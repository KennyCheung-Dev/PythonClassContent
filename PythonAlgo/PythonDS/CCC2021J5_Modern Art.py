row = int(input())
col = int(input())

R = [0] * row  #[0, 0, 0, 0]
C = [0] * col  #[0, 0, 0, 0]

for i in range(int(input())):
    line = input().split(" ") # R 2
    if line[0] == "R":
        lineNum = line[1]
        intCasted = int(lineNum)
        machineIndex = intCasted - 1
        R[machineIndex] += 1
    elif line[0] == "C":
        C[int(line[1]) - 1] += 1

count = 0
for i in range(row):
    for j in range(col):
        if (R[i] + C[j]) % 2 == 1:
            count += 1

print(count)

















