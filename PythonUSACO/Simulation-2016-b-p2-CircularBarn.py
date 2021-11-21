'''

Being a fan of contemporary architecture, Farmer John has built a new barn in the shape of a perfect circle. Inside, the barn consists of a ring of n rooms, numbered clockwise from 1…n around the perimeter of the barn (3≤n≤1,000). Each room has doors to its two neighboring rooms, and also a door opening to the exterior of the barn.
Farmer John wants exactly ri cows to end up in each room i (1≤ri≤100). To herd the cows into the barn in an orderly fashion, he plans to unlock the exterior door of a single room, allowing the cows to enter through that door. Each cow then walks clockwise through the rooms until she reaches a suitable destination. Farmer John wants to unlock the exterior door that will cause his cows to collectively walk a minimum total amount of distance. Please determine the minimum total distance his cows will need to walk, if he chooses the best such door to unlock. The distance walked by a single cow is the number of interior doors through which she passes.

INPUT FORMAT (file cbarn.in):
The first line of input contains n. Each of the remaining n lines contain r1…rn.
OUTPUT FORMAT (file cbarn.out):
Please write out the minimum total amount of distance the cows collectively need to travel.
SAMPLE INPUT:
5
4
7
8
6
4
SAMPLE OUTPUT:
48
In this example, the best solution is to let the cows enter through the door of the room that requires 7 cows.

Problem credits: Brian Dean

'''

def Steps(li):
    sum = 0
    for i in range(1, len(li)):
        sum += i * li[i]
    return sum

li = []
for i in range(int(input())):
    li.append(int(input()))

lowest = Steps(li)
for i in range(len(li) - 1):
    li.append(li.pop(0))
    temp = Steps(li)
    if temp < lowest:
        lowest = temp
print(lowest)