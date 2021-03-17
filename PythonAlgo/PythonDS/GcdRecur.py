# Use Recursion, find gcd
# 3768 % 1701 = 366
# 1701 % 366 = 237
# 366 % 237 = 129
# 237 % 129 = 108
# 129 % 108 = 21
# 108 % 21 = [3]
# 21 % 3 = 0

def GCDRecur(quotient, remainder):
    if remainder == 0:
        return quotient
    else:
        return GCDRecur(remainder, quotient % remainder)
print(GCDRecur(3768, 1701))