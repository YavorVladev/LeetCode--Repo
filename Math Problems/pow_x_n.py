# Implement pow(x, n), which calculates x raised to the power n (i.e., xn).
#
#
#
# Example 1:
#
# Input: x = 2.00000, n = 10
# Output: 1024.00000
# Example 2:
#
# Input: x = 2.10000, n = 3
# Output: 9.26100


class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0:
            x = 1 / x
            n = abs(n)
        res = 1
        while n > 0:
            if n % 2 == 1:
                res *= x
            x *= x
            n //= 2
        return

    #     Time complexity O(n)
