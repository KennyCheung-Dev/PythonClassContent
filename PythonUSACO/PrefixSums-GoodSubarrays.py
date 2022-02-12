'''

https://codeforces.com/contest/1398/problem/C

You are given an array 𝑎1,𝑎2,…,𝑎𝑛 consisting of integers from 0 to 9. A subarray 𝑎𝑙,𝑎𝑙+1,𝑎𝑙+2,…,𝑎𝑟−1,𝑎𝑟 is good if the sum of elements of this subarray is equal to the length of this subarray (∑𝑖=𝑙𝑟𝑎𝑖=𝑟−𝑙+1).

For example, if 𝑎=[1,2,0], then there are 3 good subarrays: 𝑎1…1=[1],𝑎2…3=[2,0] and 𝑎1…3=[1,2,0].

Calculate the number of good subarrays of the array 𝑎.

Input
The first line contains one integer 𝑡 (1≤𝑡≤1000) — the number of test cases.

The first line of each test case contains one integer 𝑛 (1≤𝑛≤105) — the length of the array 𝑎.

The second line of each test case contains a string consisting of 𝑛 decimal digits, where the 𝑖-th digit is equal to the value of 𝑎𝑖.

It is guaranteed that the sum of 𝑛 over all test cases does not exceed 105.

Output
For each test case print one integer — the number of good subarrays of the array 𝑎.

Example
inputCopy
3
3
120
5
11011
6
600005
outputCopy
3
6
1
Note
The first test case is considered in the statement.

In the second test case, there are 6 good subarrays: 𝑎1…1, 𝑎2…2, 𝑎1…2, 𝑎4…4, 𝑎5…5 and 𝑎4…5.

In the third test case there is only one good subarray: 𝑎2…6.

'''

for i in range(int(input())):
    n = int(input())
    prefixSum = [0]
    line = list(map(int, list(input())))
    sum = 0
    for num in line:
        sum += num
        prefixSum.append(sum)
    goodSubarrays = 0
    for j in range(1, n + 1):
        for k in range(j, n + 1):
            if prefixSum[k] - prefixSum[j-1] == k - j + 1:
                goodSubarrays += 1
    print(goodSubarrays)

