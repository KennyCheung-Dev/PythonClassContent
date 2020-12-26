size = int(input())
nums = []
nums = [int(i) for i in input().split(" ")]

numsSorted = nums.copy()
numsSorted.sort()


print(nums)
currentIndexFront = 0
currentIndexEnd = len(numsSorted) - 1
while True:
    if currentIndexFront > currentIndexEnd:
        break
    print(str(nums.index(numsSorted[currentIndexFront]) + 1), end=" ")
    nums[nums.index(numsSorted[currentIndexFront])] = None
    print(str(nums.index(numsSorted[currentIndexEnd]) + 1))
    nums[nums.index(numsSorted[currentIndexEnd])] = None
    currentIndexFront += 1
    currentIndexEnd -= 1

