'''

Problem J4/S2: Good Groups
Problem Description
A class has been divided into groups of three. This division into groups might violate two types of constraints: some students must work together in the same group, and some students must work in separate groups.
Your job is to determine how many of the constraints are violated.
Input Specification
The first line will contain an integer X with X ≥ 0. The next X lines will each consist of two different names, separated by a single space. These two students must be in the same group.
The next line will contain an integer Y with Y ≥ 0. The next Y lines will each consist of two different names, separated by a single space. These two students must not be in the same group.
Among these X + Y lines representing constraints, each possible pair of students appears at most once.
The next line will contain an integer G with G ≥ 1. The last G lines will each consist of three different names, separated by single spaces. These three students have been placed in the same group.
Each name will consist of between 1 and 10 uppercase letters. No two students will have the same name and each name appearing in a constraint will appear in exactly one of the G groups.
The following table shows how the available 15 marks are distributed at the Junior level.
 Marks Awarded
4marks 10marks 1mark
Number of Groups
G≤50
G≤50 G≤100000
Number of Constraints
X≤50andY =0 X≤50andY ≤50 X≤100000andY ≤100000
    The following table shows how the available 15 marks are distributed at the Senior level.
 Marks Awarded
3marks 5marks 7 marks
Output Specification
Number of Groups
G≤50
G≤50
G ≤ 100000
Number of Constraints
X≤50andY =0 X≤50andY ≤50
X ≤ 100000 and Y ≤ 100000
    Output an integer between 0 and X+Y which is the number of constraints that are violated. La version fran ̧caise figure a` la suite de la version anglaise.
Sample Input 1



1
ELODIE CHI
0
2
DWAYNE BEN ANJALI
CHI FRANCOIS ELODIE



Output for Sample Input 1
0
Explanation of Output for Sample Input 1
There is only one constraint and it is not violated: ELODIE and CHI are in the same group.
Sample Input 2
3
A B
G L
J K
2
D F
D G
4
A C G
B D F
E H I
J K L
Output for Sample Input 2
3
Explanation of Output for Sample Input 2
The first constraint is that A and B must be in the same group. This is violated.
The second constraint is that G and L must be in the same group. This is violated.
The third constraint is that J and K must be in the same group. This is not violated. The fourth constraint is that D and F must not be in the same group. This is violated. The fifth constraint is that D and G must not be in the same group. This is not violated. Of the five constraints, three are violated.

'''

numRule1 = int(input())
rule1Pairs = []
rule2Pairs = []
for i in range(numRule1):
    rule1Pairs.append(input().split())
numRule2 = int(input())
for i in range(numRule2):
    rule2Pairs.append(input().split())
numGroup = int(input())
groupNum = 0
groupings = {}
for i in range(numGroup):
    groupEntries = input().split()
    for name in groupEntries:
        groupings[name] = groupNum
    groupNum += 1

rulesViolating = 0
for i in rule1Pairs:
    if groupings[i[0]] != groupings[i[1]]:
        rulesViolating += 1
for i in rule2Pairs:
    if groupings[i[0]] == groupings[i[1]]:
        rulesViolating += 1
print(rulesViolating)