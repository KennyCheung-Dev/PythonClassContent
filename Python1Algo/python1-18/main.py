# RoundUp Above or Equal to 5, Round down below 5,
# to the nearest multiple of 10
# 15 round up to 20
# 12 round down to 10
# Write a function that takes in 3 integer, round, and return the sum

def round10(num):
    digit = num % 10
    num -= digit
    if digit >= 5:
        num += 10
    return num

def round_sum(n1, n2, n3):
    return round10(n1) + round10(n2) + round10(n3)

print(round_sum(14, 17, 18))

# --------------------------------------------------------

# Non-Repeating Sum
# 不重复 的 和

def lone_sum(li):
    sum = 0
    for i in li:
        if li.count(i) == 1:
            sum += i
    return sum

print(lone_sum([2, 5, 5, 1]))

# --------------------------------------------------------

# 游戏：
# 4位数密码
# 猜方猜4位数，host告诉猜放有多少位置号码都对了 有多少位置不对但是号码对了
# 号码位置都对了是 bull  位置不对但号码对了是cows
# Secret: 1807
# Guess:  7810
# 1 bull 3 cows
def BullCows(secret, guess):
    secret = str(secret)
    guess = str(guess)
    cows = 0
    bull = 0
    for i in range(len(guess)):
        if guess[i] in secret:
            if guess[i] == secret[i]:
                bull += 1
            else:
                cows += 1
    # print("{} bull and {} cows.".format(bull,  cows))
    return (bull, cows)

secret = 1807
guess = 7810
BullCows(1807, 7810)

# --------------------------------------------------------

import random

while True:
    secret = random.randint(1000, 9999)
    for i in range(1000, 9999):
        bull, cows = BullCows(secret, i)
        if bull == 4:
            print("Game Won! Answer: " + str(i))
            break
        elif bull > 0 or cows > 0:
            print("Num : " + str(i) + " , Bull : " + str(bull) + " , Cows: " + str(cows))
    break


