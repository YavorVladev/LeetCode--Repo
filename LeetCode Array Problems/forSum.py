# Given an array nums of n integers, return an array of all the unique
# quadruplets [nums[a], nums[b], nums[c], nums[d]] such that:
#
# 0 <= a, b, c, d < n
# a, b, c, and d are distinct.
# nums[a] + nums[b] + nums[c] + nums[d] == target
# You may return the answer in any order.
#
#
#
# Example 1:
#
# Input: nums = [1,0,-1,0,-2,2], target = 0
# Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
# Example 2:
#
# Input: nums = [2,2,2,2,2], target = 8
# Output: [[2,2,2,2]]


class Solution(object):
    def threeSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 2):
            l = i + 1;
            r = len(nums) - 1
            t = target - nums[i]
            if i == 0 or nums[i] != nums[i - 1]:
                while l < r:
                    s = nums[l] + nums[r]
                    if s == t:
                        results.append([nums[i], nums[l], nums[r]])
                        while l < r and nums[l] == nums[l + 1]: l += 1
                        while l < r and nums[r] == nums[r - 1]: r -= 1
                        l += 1;
                        r -= 1
                    elif s < t:
                        l += 1
                    else:
                        r -= 1

        return results

    def fourSum(self, nums, target):
        results = []
        nums.sort()
        for i in range(len(nums) - 3):
            if i == 0 or nums[i] != nums[i - 1]:
                threeResult = self.threeSum(nums[i + 1:], target - nums[i])
                for item in threeResult:
                    results.append([nums[i]] + item)
        return results
