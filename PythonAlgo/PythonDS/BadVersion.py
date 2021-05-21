'''
Exercise: 1
You are a product manager and currently leading a team to develop a new product.

Unfortunately, the latest version of your product fails the quality check.
Since each version is developed based on the previous versions, all the versions after a bad version are also bad.

Suppose you have n version [1, 2, .... n] and you want to find out the first bad one, which
causes all the following ones to be bad.

You are given an API tool isBadVersion(version) which will return whether version is bad.
Implement a function to find the first bad version. YOu should minimize the number of calls to
the API.

Example:
    Given n = 5, version = 4 is the first bad version
    call isBadVersion(3) -> False
    call isBadVersion(5) -> True
    call isBadVersion(4) -> True

    Then 4 is the first bad version
'''

# versions = [False, False, False, False, False, False, True, True, True, True, True, True, True]
#
# def isVersionBad(x):
#     return versions[x]




