n = int(input())
# bty = list(map(int, input().split()))
nums = [int(i) for i in input().split(" ")]
print(nums)
cot = []
for i in range(n):
	if nums[i] != '*':
		cnt = 1
		for j in range(i + 1, n):
			if nums[j] == nums[i]:
				cnt += 1
				nums[j] = '*'
		cot.append(cnt)
#print cot
res = 0
while True:
	cmt = 0
	for c in cot:
		if c > 0:
			cmt += 1
	if cmt <= 1:
		break
	else:
		res += (cmt - 1)
		cot = map(lambda x: x - 1, cot)
print(res)