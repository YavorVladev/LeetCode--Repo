class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        d = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in d:
                return [d[complement], i]
            d[num] = i


nums = [2, 7, 11, 15]
target = 9

sol = Solution()
result = sol.twoSum(nums, target)

print(result)

