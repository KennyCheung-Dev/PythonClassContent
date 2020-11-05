ref, cases, n = [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000], [0, 100, 500, 1000, 5000, 10000, 25000, 50000, 100000, 500000, 1000000], int(input())
for t in [int(input()) - 1 for x in range(n)]: cases.remove(ref[t])
print("deal") if sum(cases)/n < int(input()) else print("no deal")
