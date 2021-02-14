w = 0
for i in range(6):
    s = input().strip()
    if s == "W":
        w += 1
if w == 6 or w == 5:
    print(1)
elif w == 4 or w == 3:
    print(2)
elif w == 2 or w == 1:
    print(1)
else:
    print(0)
