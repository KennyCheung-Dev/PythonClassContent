times = int(input())
for i in range(times):
    s = input()
    ps = s[0]
    count = 0
    for j in range(len(s)):
        if s[j] != ps:
            print(str(count) + " " + str(ps) + " ", end="")
            count = 1
        else:
            count += 1
        ps = s[j]
    print(str(count) + " " + str(ps), end="")
    print()