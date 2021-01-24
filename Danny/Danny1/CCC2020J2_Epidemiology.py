P = int(input())
N = int(input())
R = int(input())
accumulation = N
infected = N * R
counter = 0
while True:
    accumulation += infected
    counter += 1
    print(accumulation)
    if accumulation > P:
        break
    infected *= R
print(counter)