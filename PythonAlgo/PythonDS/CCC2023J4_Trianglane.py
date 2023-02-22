c = int(input())
r1 = list(map(int, input().split(" ")))
r2 = list(map(int, input().split(" ")))

count = 0

for i in range(c):
    if r1[i] == 0:
        continue
    else:
        count += 3
        if i != 0 and r1[i - 1] == 1:
            count -= 2

for i in range(c):
    if r2[i] == 0:
        continue
    else:
        count += 3
        if i % 2 == 0:
            if r1[i] == 1:
                count -= 2
        if i != 0 and r2[i - 1] == 1:
            count -= 2

print(count)
