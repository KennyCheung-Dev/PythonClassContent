'''
Given a positive integer num, write a function which returns
if num is a perfect square else False.

Note: Do not use any built-in library function such as sqrt.

Example 1:
Input: 16
Output: true

Example 2:
Input: 14
Output: False

'''

def isPerfectSquare(num):
    if num<=4:
        return num == 1 or num == 4
    l, r = 0, num
    while l < r:
        mid = (l + r) // 2
        tmp = mid * mid
        if tmp == num:
            return True
        elif tmp < num:
            l = mid + 1
        else:
            r = mid
    return False