'''
https://leetcode.com/problems/maximum-subarray/
'''

nums = [-2,1,-3,4,-1,2,1,-5,4]
def maxSubArray(nums):
        li = nums.copy()
        for i in range(1, len(nums)):
            li[i] = max(nums[i], nums[i] + li[i-1])
        return max(li)
print(maxSubArray(nums))