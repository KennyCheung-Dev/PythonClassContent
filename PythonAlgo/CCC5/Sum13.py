# Return the sum of the numbers in the list,
# returning 0 for an empty list.
# 13 is a very unlucky number, so it does not count and
# numbers that come immediately after a 13 also do not count

# Input:
# sum13([1, 2, 2, 1])
# Output:
# 6

# Input:
# sum13([1, 2, 2, 1, 13])
# Output:
# 6

# Input:
# sum13([1, 2, 2, 1, 13, 5])
# Output:
# 6

# Input:
# sum13([1, 2, 2, 1, 14, 5])
# Output:
# 25

# Input:
# sum13([1, 2, 2, 1, 13, 5, 4])
# Output:
# 10


def sum13(li):
    sum = 0
    for i in range(len(li)):
        if li[i] == 13 or li[i-1] == 13:
            continue
        sum += li[i]
    print(sum)

sum13([1, 2, 2, 1, 13, 5, 4])


#Homework :
# 2008 J2 - Do the Shuffle
# https://dmoj.ca/problem/ccc08j2

# 2015 J2 - Happy or Sad
# https://dmoj.ca/problem/ccc15j2

