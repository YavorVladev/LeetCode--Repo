# You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order.
# Apply the following algorithm on arr:
#
# Starting from left to right, remove the first number and every other number
# afterward until you reach the end of the list.
# Repeat the previous step again, but this time from right to left, remove the rightmost
# number and every other number from the remaining numbers.
# Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
# Given the integer n, return the last number that remains in arr.
#
#
#
# Example 1:
#
# Input: n = 9
# Output: 6
# Explanation:
# arr = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# arr = [2, 4, 6, 8]
# arr = [2, 6]
# arr = [6]


# Example 2:
#
# Input: n = 1
# Output: 1


class Solution:
    def lastRemaining(self, n: int) -> int:
        first = 1
        distance = 1
        step = 0
        while n > 1:
            if step % 2 == 0 or n % 2 != 0:
                first += distance

            distance = distance << 1
            step += 1
            n = n >> 1
        return first


#     SECOND SOLUTION COMING SOON



# class Solution:
#     def lastRemaining(self, n: int) -> int:
#         if n == 1:
#             return 1
#         else:
#             return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))


sol = Solution()
n = 9
res = sol.lastRemaining(n)
print(res)


