# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
#
# Example 1:
#
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
# Example 2:
#
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step

class Solution:
    def climbStairs(self, n: int) -> int:

        data = {}
        data[1] = 1
        data[2] = 2

        def climb(n):
            if n in data:
                return data[n]
            else:
                data[n] = climb(n - 1) + climb(n - 2)
                return data[n]

        return climb(n)

                                # Time complexity O(n)

                                # Different Solution - Simplified

#     def climbStairs(n: int) -> int:
#     if n <= 2:
#         return n
#
#     dp = [0] * (n + 1)
#     dp[1] = 1
#     dp[2] = 2
#
#     for i in range(3, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#
#     return dp[n]


sol = Solution()
number = 7
result = sol.climbStairs(number)
print(result)
