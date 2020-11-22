a, b = 100, 100
for i in range(int(input())):
    s = input()
    c = int(s.split(" ")[0])
    d = int(s.split(" ")[1])
    if c < d:
        a -= d
    elif c > d:
        b -= c
print(a)
print(b)