nums = list(map(int, input().split()))

diff = []
for i in range(len(nums) - 1):
    numDiff = nums[i+1] - nums[i] - 1
    if numDiff > 0:
        diff.append(numDiff)
if len(diff) == 0:
    print(0)
    print(0)
else:
    print(min(diff))
    print(max(diff))