low = int(input())
high = int(input())
total = 0
for i in range(low, high+1):
    count = 0
    for j in range(1, i+1):
        if i % j == 0:
            count += 1
    if count == 4:
        total += 1
print("The number of RSA numbers between " + str(low) + " and " + str(high) + " is " + str(total))

# short
# low, high, total, count = int(input()), int(input()), 0, 0; print("The number of RSA numbers between " + str(low) + " and " + str(high) + " is " + str([1 if (k.count(True) == 4) else 0 for k in [[True if i % j == 0 else False for j in range(1, i+1)]for i in range(low, high+1)]].count(1)))




