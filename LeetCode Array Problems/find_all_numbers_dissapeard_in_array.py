# Given an array nums of n integers where nums[i]
# is in the range [1, n], return an array of all the
# integers in the range [1, n] that do not appear in nums.
#
#
#
# Example 1:
#
# Input: nums = [4,3,2,7,8,2,3,1]
# Output: [5,6]
# Example 2:
#
# Input: nums = [1,1]
# Output: [2]

class Solution(object):
    def findDisappearedNumbers(self, nums):
        for i in range(len(nums)):
            index = abs(nums[i]) - 1
            nums[index] = - abs(nums[index])

        return [i + 1 for i in range(len(nums)) if nums[i] > 0]

