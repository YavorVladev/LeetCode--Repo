class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            else:
                seen.add(num)

        return False


sol = Solution()
numbers = [1, 2, 3, 4]
res = sol.containsDuplicate(numbers)
print(res)
