N = int(input())

winner = ""
max_score = 0

for i in range(N):
    name = input()
    score = int(input())
    if score > max_score:
        winner = name
        max_score = score
print(winner)