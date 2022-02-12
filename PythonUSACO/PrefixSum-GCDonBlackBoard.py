'''

https://atcoder.jp/contests/abc125/tasks/abc125_c

Problem Statement
There are N integers, A
1
​
 ,A
2
​
 ,...,A
N
​
 , written on the blackboard.

You will choose one of them and replace it with an integer of your choice between 1 and 10
9
  (inclusive), possibly the same as the integer originally written.

Find the maximum possible greatest common divisor of the N integers on the blackboard after your move.

Constraints
All values in input are integers.
2≤N≤10
5

1≤A
i
​
 ≤10
9

Output
Input is given from Standard Input in the following format:

N
A
1
​
  A
2
​
  ... A
N
​

Output
Print the maximum possible greatest common divisor of the N integers on the blackboard after your move.

Sample Input 1
Copy
3
7 6 8
Sample Output 1
Copy
2
If we replace 7 with 4, the greatest common divisor of the three integers on the blackboard will be 2, which is the maximum possible value.

Sample Input 2
Copy
3
12 15 18
Sample Output 2
Copy
6
Sample Input 3
Copy
2
1000000000 1000000000
Sample Output 3
Copy
1000000000
We can replace an integer with itself.

'''


#Brute Force
# import math
#
# n = int(input())
# nums = [int(i) for i in input().split()]
#
# biggestGcd = -1
# for i in range(n):
#     left = -1
#     right = -1
#
#     if i != 0:
#         left = nums[0]
#         for j in range(1, i):
#             left = math.gcd(left, nums[j])
#
#     if i != n-1:
#         right = nums[i + 1]
#         for j in range(i + 2, n):
#             right = math.gcd(right, nums[j])
#
#     if i == 0:
#         combinedGcd = right
#     elif i == n-1:
#         combinedGcd = left
#     else:
#         combinedGcd = math.gcd(left, right)
#     if combinedGcd > biggestGcd:
#         biggestGcd = combinedGcd
# print(biggestGcd)


# Prefix Sum
import math

n = int(input())
nums = [int(i) for i in input().split()]

left = [nums[0]]
right = [nums[-1]]

for j in range(1, n):
    left.append(math.gcd(left[-1], nums[j]))

for j in range(n-2, -1, -1):
    right.insert(0, math.gcd(right[0], nums[j]))

biggestGcd = -1
for i in range(n):
    tempGcd = -1
    if i == 0:
        tempGcd = right[i+1]
    elif i == n-1:
        tempGcd = left[i-1]
    else:
        tempGcd = math.gcd(left[i-1], right[i+1])
    if tempGcd > biggestGcd:
        biggestGcd = tempGcd

print(biggestGcd)


