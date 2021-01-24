line = input().split(" ")
list = []
for i in range(int(line[0])):
    list.append([])
    for k in input():
        list[i].append(k)
for i in list:
    print(i)
for k in range(100):
    for i in range(len(list) - 1):
        for j in range(len(list[i])):
            if list[i][j] == 'o' and list[i + 1][j] == '.':
                list[i][j] = '.'
                list[i + 1][j] = 'o'

print()
for i in list:
    print(i)