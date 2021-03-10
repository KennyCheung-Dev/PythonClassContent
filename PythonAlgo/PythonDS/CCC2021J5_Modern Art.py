row = int(input())
col = int(input())

R = [0] * row
C = [0] * col

for i in range(int(input())):
    line = input().split(" ")
    if line[0] == "R":
        R[int(line[1]) - 1] += 1
    elif line[0] == "C":
        C[int(line[1]) - 1] += 1

count = 0
for i in range(row):
    for j in range(col):
        if (R[i] + C[j]) % 2 == 1:
            count += 1

print(count)

















