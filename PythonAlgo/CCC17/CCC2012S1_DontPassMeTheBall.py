goalNum = int(input())
count = 0
for i in range(goalNum):
    for j in range(1, i):
        for k in range(1, j):
            count+=1
print(count)