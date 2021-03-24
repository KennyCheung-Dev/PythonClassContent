N = int(input())
relations = [[], [], [], [], [], []]

for i in range(1, N):
    relations[int(input()) - 1].append(i)

def Ways(i):
    if len(relations[i - 1]) == 0:
        return 2
    else:
        subsequentWays = 1
        for invitee in relations[i - 1]:
            subsequentWays *= Ways(invitee)
        return 1 + subsequentWays

print(Ways(N) - 1)