import time

li2 = [str(x) for x in range(5000000)]

start_time = time.time()

# ----------- Type case a list of int to strings -----------

# First way:  Normal for loop
# li = list(range(0, 5000000))
# for i in range(len(li)):
#     li[i] = str(li[i])
# print(li[0] + li[1])

# Second way: map, lambda
# li = list(map(lambda x : str(x), list(range(0, 5000000))))
# print(li[0] + li[1])

# Third way: list comprehension
# li = [str(x) for x in range(5000000)]
# print(li[0] + li[1])



# ----------- Concatenation of strings -----------

# First way:  Normal for loop
# result = ""
# for i in li2:
#     result += i

# Second way: "".join
result = "".join(li2)

print("--- %s seconds ---" % (time.time() - start_time))