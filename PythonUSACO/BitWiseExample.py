'''
Apple Division:
https://cses.fi/problemset/task/1623
'''


# n = int(input())
# p = list(map(int, input().split()))
#
# ans = float('inf')
# for mask in range(1 << n):
# 	s1, s2 = 0, 0
# 	for i in range(n):
# 		if mask & (1 << i):
# 			s1 += p[i]
# 		else:
# 			s2 += p[i]
# 	ans = min(ans, abs(s1 - s2))
#
# print(ans)

n = 3
for i in range(1 << n):
	for j in range(n):
		print("Mask : " + str(bin(i)))
		print("Bit : " + str(bin(1 << j)))
		if i & (1 << j):
			print("Match, to go bucket 1")
		else:
			print("Not Match, to bucket 0")
		print()

