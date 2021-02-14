li = []

for i in range(int(input())):
    num = int(input())

    if num == 0:
        if len(li) > 0:
            li.pop(len(li) - 1)
    else:
        li.append(num)
print(sum(li))