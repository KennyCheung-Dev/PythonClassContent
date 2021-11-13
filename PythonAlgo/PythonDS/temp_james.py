
# word = "abcde"

# for i in range(len(word)):
#     for j in range(i + 1, len(word) + 1):
#         print(i, j)
#         print(word[i:j])


#for i in range(4):
#     for j in range(4):
#         for k in range(4):
#             print(i, j, k)

# for i in range(10):
#     for j in range(10):
#         for k in range(10):
#             print(i, j, k)

# firstLine = input()  # "3 3"
# splitLine = firstLine.split()  # ['3', '3']
# for i in range(len(splitLine)):
#     splitLine[i] = int(splitLine[i])
#     # [3, 3]
# print(splitLine)


# line = [int(i) for i in input().split()]
# print(line)


'''
Always the troublemaker, Bessie the cow has stolen Farmer John's tractor and taken off down the road!
The road is exactly 100 miles long, and Bessie drives the entire length of the road before ultimately
being pulled over by a police officer, who gives Bessie a ticket for exceeding the speed limit,
for having an expired license, and for operating a motor vehicle while being a cow.
While Bessie concedes that the last two tickets are probably valid,
she questions whether the police officer was correct in issuing the speeding ticket,
and she wants to determine for herself if she has indeed driven faster than the speed limit for part of her journey.

The road is divided into N segments, each described by a positive integer length in miles,
as well as an integer speed limit in the range 1…100 miles per hour. As the road is 100 miles long,
the lengths of all N segments add up to 100. For example,
the road might start with a segment of length 45 miles, with speed limit 70,
and then it might end with a segment of length 55 miles, with speed limit 60.

Bessie's journey can also be described by a series of segments, M of them. During each segment,
she travels for a certain positive integer number of miles, at a certain integer speed.
For example, she might begin by traveling 50 miles at a speed of 65,
then another 50 miles at a speed of 55. The lengths of all M segments add to 100 total miles.
Farmer John's tractor can drive 100 miles per hour at its fastest.

Given the information above, please determine the maximum amount over the speed limit that Bessie travels during any part of her journey.

INPUT FORMAT (file speeding.in):
The first line of the input contains N and M, separated by a space.
The next N lines each contain two integers describing a road segment, giving its length and speed limit.

The next M lines each contain two integers describing a segment in Bessie's journey,
giving the length and also the speed at which Bessie was driving.

OUTPUT FORMAT (file speeding.out):
Please output a single line containing the maximum amount over the speed limit Bessie drove during any part of her journey.
If she never exceeds the speed limit, please output 0.

SAMPLE INPUT:
3 3
40 75
50 35
10 45
40 76
20 30
40 40

SAMPLE OUTPUT:
5
In this example, the road contains three segments (40 miles at 75 miles per hour,
followed by 50 miles at 35 miles per hour, then 10 miles at 45 miles per hour).
Bessie drives for three segments (40 miles at 76 miles per hour, 20 miles at 30 miles per hour,
and 40 miles at 40 miles per hour). During her first segment,
she is slightly over the speed limit, but her last segment is the worst infraction,
during part of which she is 5 miles per hour over the speed limit. The correct answer is therefore 5.

'''

# List Comprehension
# "3 3"
# ["3", "3"]
# [3, 3]

# speedLimitInput = []
# speedInput = []
#
# N, M = [int(i) for i in input().split()]
#
# for i in range(N):
#     speedLimitInput.append([int(i) for i in input().split()])
#
# for i in range(M):
#     speedInput.append([int(i) for i in input().split()])
#
# speedLimit = [] # 100 entries inside
# speed = []

'''
[
[40 75],
[50 35],
[10 45],
]
'''

# for section in speedLimitInput: # each i contains [40, 75]
#     for j in range(section[0]):
#         speedLimit.append(section[1])
#
# for section in speedInput:
#     for j in range(section[0]):
#         speed.append(section[1])
#
# print(speedLimit)
# print(speed)
#
# highestSpeedExceeded = -1
# for i in range(100):
#     speedTravelling = speed[i]
#     limit = speedLimit[i]
#     speedExceeded = speedTravelling - limit  # 5
#     if speedExceeded > highestSpeedExceeded:
#         highestSpeedExceeded = speedExceeded
#
# print(highestSpeedExceeded)

    # print("Bessie is travelling at " + str(speedTravelling) + "mph, the speed limit is " + str(limit))





#ATATGTAGCTAGCATAATA
# possibleEnds = ["TAA", "TAG", "TGA"]
# line = input()
# line = line[line.index("ATG"):]
# for i in range(len(line) - 3, 2, -1):
#     if line[i:i+3] in possibleEnds:
#         if i % 3 == 0:
#             print(line[0:i+3])
#             break
#
# answers = []
# for end in possibleEnds:
#     currentEndIndex = len(line)
#     while currentEndIndex > 4:
#         if line.rfind(end, 0, currentEndIndex) == -1:
#             break
#         else:
#             indexOfEndingTag = line.rfind(end, 0, currentEndIndex)
#             if indexOfEndingTag % 3 == 0:
#                 answers.append(line[0:indexOfEndingTag+3])
#                 break
#         currentEndIndex -= 1
# answers = sorted(answers, key=lambda item: len(item))
# print(answers[-1])

# Quick tutorial on lambda
# list = [[999, 1], [2, 2], [1, 3], [0, 4], [8, 5]]
# list = sorted(list, key=lambda item: 0)
# print(list)


# def AnonymousFunction(item):
#     return item[1]

# key = 5
# chr(ord("a") + ((ord("h") - ord("a")) % 26))
# index = ord("x")
# # print(index - 97) # 120 - 97 = 23
# newIndex = ((index - 97) + 5) % 26
# newChar = chr(newIndex)
# print(newChar)
'''
% 3

0 0
1 1
2 2
3 0
4 1
5 2
6 0
7 1 
8 2
9 0
10 1
11 2
12 0
13 1
'''
#
# z 25 % 26 : 25 z
# 26 % 26 : 0 a
# 27 % 26 : 1 b
#
# x + 1   24 % 26  24 = y
#
# 0 - 26 range

'''
Kenny: 50
Kenny: 60
James: 2
James: 2000
'''


# dict = {}
#
# dict["Kenny"] = 50
# dict["James"] = 1000
#
# print(dict["Kenny"])

# numbers = {
#     '0':'ling',
#     '1':'yi',
#     '2':'er',
#     '3':'san',
#     '4': 'si',
#     '5':'wu',
#     '6':'liu',
#     '7':'qi',
#     '8':'ba',
#     '9':'jiu',
#     '10': 'shi'
# }

# def Chinese(num):
#     if 0 <= num <= 10:
#         return numbers[str(num)]
#     elif 11 <= num <= 19:
#        return numbers['10'] + " " + numbers[str(num)[1]]
#     else:
#         if str(num)[1] == "0":
#             return numbers[str(num)[0]] + " " + numbers['10']
#         else:
#             return numbers[str(num)[0]] + " " + numbers['10'] + " " + numbers[str(num)[1]]
#
# print(Chinese(17))



# Hanoi Tower
# towers = [[], [], []]
# numPlate = int(input())
# for i in range(numPlate):
#     towers[0].append(numPlate - i)
#
# def Letter(i):
#     return "A" if i == 0 else "B" if i == 1 else "C"
#
# def HanoiRecur(num, fromRod, toRod, auxRod):
#     global towers
#     if num == 0:
#         pass
#     else:
#         HanoiRecur(num - 1, fromRod, auxRod, toRod)
#         towers[toRod].append(towers[fromRod].pop(-1))
#         print("Plate size: " + str(towers[toRod][-1]) + " moved from " + Letter(fromRod) + " to " + Letter(toRod))
#         HanoiRecur(num - 1, auxRod, toRod, fromRod)
#         print("At this Point, towers: " + str(towers))
#
# HanoiRecur(numPlate, 0, 2, 1)



# Reverse
# HelloWorld
# dlroWolleH



