# Warmup
# print the following:
'''
*
**
***
****
*****
'''

[print("*" * j) for j in range(1, 6)]

'''
Print the multiplication table:
1 * 1 = 1 | 1 * 2 = 2 | 1 * 3 ...
2 * 1 = 2 | ...
....... | 9 * 9 = 81
'''

# [[print("{} * {} = {}".format(i, j, i*j)) for j in range(1, 10)] for i in range(1, 10)]

for i in range(1, 10):
    for j in range(1, 10):
        print("{} * {} = {}".format(i, j, i*j), end = "")
        if j != 9:
            print(" | ", end = "")
        else:
            print()


