stack = []
s = input()

res = 0

closing = '}])>'
opening = '<({['

revert = {'}': '{', ')': '(', ']': '[', '>': '<'}

for char in s:

    if char in opening:
        stack.append(char)

    if char in closing:
        if len(stack) == 0:
            print('Impossible')
            exit(0)

        if stack[-1] != revert[char]:
            res += 1

        k = stack.pop(-1)

if len(stack) != 0:
    print('Impossible')
    exit(0)

print(res)
