'''
CCC2013J4 - TimeOnTask
https://dmoj.ca/problem/ccc13j4
'''

limit = int(input())
tasks = []
for i in range(int(input())):
    tasks.append(int(input()))
tasks = sorted(tasks)

temp = 0
taskCount = 0
for t in tasks:
    if temp + t > limit:
        print(taskCount)
        break
    else:
        temp += t
        taskCount += 1


