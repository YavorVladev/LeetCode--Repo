# Given an integer num, repeatedly add all its digits
# until the result has only one digit, and return it.


class Solution:
    def addDigits(self, num: int) -> int:
        if (num == 0): return 0
        if num % 9 == 0:
            return 9
        else:
            return num % 9

#         Time Complexity O(1)


sol = Solution()
n = 38
res = sol.addDigits(n)
print(res)
