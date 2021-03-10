K = int(input())
line = input()
result = ""
for i in range(len(line)):
    S = 3 * (i + 1) + K
    index = ord(line[i]) - S
    while (index < 65):
        index += 26
    while (index > 90):
        index -= 26
    result += (chr(index))
print(result)