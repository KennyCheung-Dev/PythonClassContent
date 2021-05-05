def Fib(a):
    if a == 0 or a == 1:
        return 1
    return Fib(a - 1) + Fib(a - 2)

import math
sum = 0
for i in range(4):
    sum += int(math.pow(Fib(i), 2))


print(sum)