M = int(input())
N = int(input())
K = int(input())

C = [0]*N
R = [0]*M

for i in range(K):
    line = input().split(" ")
    op = line[0]
    num = int(line[1])
    if op == "R":
        R[num-1] += 1
    elif op == "C":
        C[num-1] += 1

cnt = 0
for i in range(M):
    for j in range(N):
        if (R[i] + C[j])%2 != 0:
            cnt += 1

print(cnt)
