'''
https://leetcode.com/problems/flip-string-to-monotone-increasing/
'''

def minFlipsMonoIncr(s):
    numFlip = 0
    num1 = 0
    for letter in s:
        if letter == "1":
            num1 += 1
        elif letter == "0":
            numFlip = min(num1, numFlip + 1)
    return numFlip
print(minFlipsMonoIncr("00011000"))

