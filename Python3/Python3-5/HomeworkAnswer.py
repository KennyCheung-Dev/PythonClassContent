import numpy as np

a = np.random.randint(1, 1001, size=1000)
b = np.random.randint(1, 1001, size=1000)
c = np.random.randint(1, 1001, size=1000)

d = a * b / c

result = d[np.argsort(d)]

result2 = np.delete(result, list(range(1, 1001))[::2])

print(result2)
