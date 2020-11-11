li = [int(input()), int(input())]

while (True):
    li.append(li[-2] - li[-1])
    if li[-2] < li[-1]:
        break
print(len(li))
