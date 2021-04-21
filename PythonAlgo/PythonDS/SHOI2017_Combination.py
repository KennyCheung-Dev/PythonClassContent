'''
Combination C(n, m)
Returns the number of unique cases for
choosing m item from a set of n unique items
order doesn't matter

S = { 1, 2, 3 }
C(3, 2) = choosing 2 item from S
There are 3 possibilities:
{1, 2}
{1, 3}
{2, 3}

Therefore C(3, 2) = 3

Combinations formula:
C(n, m) = n! / m! * (n - m)!

Example:
C(3, 2) = 3! / 2! * 1!
        = 6 / 2
        = 3


You wanted to know more about the relation between Combination.


'''


import math

def C(n, m):
    return int(math.factorial(n) / (math.factorial(m) * math.factorial(n - m)))

#Take n p k r in the form of :
# 2 10007 2 0
def Foo(n, p, k, r):
    index = 0
    sum = 0
    while True:
        top = index * k + r
        bot = n * k
        print(str(top) + "     " + str(bot))
        if top > bot:
            break
        sum += C(bot, top)
        print("Added : " + str(C(bot, top)))
        index += 1
    return sum % p

n, p, k, r = [int(i) for i in input().split(" ")]
print(Foo(n, p, k, r))
