'''
5
1
2 4

3



15
8
4 7
4 1
14 11
10 6
13 4
4 10
10 3
9 14

7
'''

n = int(input())
xOrdered = [[0, 0], [n+1, n+1]]
for i in range(int(input())):
    s = [int(x) for x in input().split()]
    xOrdered.append(s)
xOrdered = sorted(xOrdered, key=lambda x: x[0])

biggestSquareEdge = -1
for i in range(len(xOrdered)):
    for j in range(i+1, len(xOrdered)):
        if xOrdered[j][0] == xOrdered[i][0]:
            continue
        gaps = [0, n+1]
        for k in range(i + 1, j):
            gaps.append(xOrdered[k][1])
        gaps.sort()
        biggestGap = 0
        for k in range(len(gaps) - 1):
            biggestGap = max(biggestGap, abs(gaps[k+1] - gaps[k] - 1))
        biggestGap = min(biggestGap, xOrdered[j][0] - xOrdered[i][0] - 1)
        biggestSquareEdge = max(biggestSquareEdge, biggestGap)
print(biggestSquareEdge)




# from functools import cmp_to_key
# n = int(input())
# t = int(input())
# tr = [(0,0)]*t
# xx = [0]*t
# for i in range(t):
#     x,y = input().split()
#     x = int(x)
#     y = int(y)
#     tr[i] = (x,y)
#     xx[i] = x+1
#
# def cmp(a,b):
#     ax,ay = a
#     bx,by = b
#     if ay < by:
#         return -1
#     elif ay == by and ax < bx:
#         return -1
#     return 1
#
# ntr = sorted(tr,key=cmp_to_key(cmp))
# xx = list(set(xx))
# xx.append(1)
# xx.sort()
#
#
# left = 1
# right = n+1
# while left + 1 < right:
#     flag = False
#     mid = (left + right) // 2
#     #print('mid', mid)
#     for i in range(len(xx)):
#         #print(xx[i])
#         if xx[i]+mid-1>n:
#             break
#         if flag:
#             break
#         last = 0
#         for x,y in ntr:
#             if x >= xx[i] and  x <= xx[i]+mid-1:
#                 if y - last - 1 >= mid:
#                     flag = True
#                     left = mid
#                     break
#                 else:
#                     last = y
#         if n+1-last-1>=mid:
#             flag = True
#             left = mid
#         #print(left,flag)
#     if not flag:
#         right = mid
# print(left)


