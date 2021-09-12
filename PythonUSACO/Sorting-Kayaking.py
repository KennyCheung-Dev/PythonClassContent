'''
B. Kayaking
time limit per test2 seconds
memory limit per test256 megabytes
inputstandard input
outputstandard output
Vadim is really keen on travelling. Recently he heard about kayaking activity near his town and became very excited about it, so he joined a party of kayakers.

Now the party is ready to start its journey, but firstly they have to choose kayaks. There are 2·n people in the group (including Vadim), and they have exactly n - 1 tandem kayaks (each of which, obviously, can carry two people) and 2 single kayaks. i-th person's weight is wi, and weight is an important matter in kayaking — if the difference between the weights of two people that sit in the same tandem kayak is too large, then it can crash. And, of course, people want to distribute their seats in kayaks in order to minimize the chances that kayaks will crash.

Formally, the instability of a single kayak is always 0, and the instability of a tandem kayak is the absolute difference between weights of the people that are in this kayak. Instability of the whole journey is the total instability of all kayaks.

Help the party to determine minimum possible total instability!

Input
The first line contains one number n (2 ≤ n ≤ 50).

The second line contains 2·n integer numbers w1, w2, ..., w2n, where wi is weight of person i (1 ≤ wi ≤ 1000).

Output
Print minimum possible total instability.

Examples
inputCopy
2
1 2 3 4
outputCopy
1
inputCopy
4
1 3 4 6 3 4 100 200
outputCopy
5
'''

num = int(input())
people = [int(i) for i in input().split()]

people.sort()

totalInstability = 0

while len(people) > 2:
    minDiff = 1200
    minDiffPerson = []
    for i in range(len(people) - 1):
        tempDiff = people[i + 1] - people[i]
        if tempDiff < minDiff:
            minDiff = tempDiff
            minDiffPerson = [i, i+1]
    totalInstability += minDiff
    people.pop(minDiffPerson[0])
    people.pop(minDiffPerson[1] - 1)
print(totalInstability)