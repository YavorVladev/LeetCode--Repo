import heapq


# A super ugly number is a positive integer whose prime
# factors are in the array primes.
#
# Given an integer n and an array of
# integers primes, return the nth super ugly number.
#
# The nth super ugly number is guaranteed
# to fit in a 32-bit signed integer.
#
#
#
# Example 1:
#
# Input: n = 12, primes = [2,7,13,19]
# Output: 32


# Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence
# of the first 12 super ugly numbers given primes = [2,7,13,19].


# Example 2:
#
# Input: n = 1, primes = [2,3,5]
# Output: 1
# Explanation: 1 has no prime factors, therefore all of its prime factors
# are in the array primes = [2,3,5].


class Solution:
    def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
        nums = primes.copy()  # do a deep copy
        heapq.heapify(nums)  # create a heap
        p = 1
        for i in range(n - 1):
            p = heapq.heappop(nums)  # take the smallest element
            for prime in primes:
                heapq.heappush(nums, p * prime)  # add all those multiples with the smallest number
                if p % prime == 0:
                    break
        return p


# Time Complexity O(n)


# class Solution:
#     def nthSuperUglyNumber(self, n: int, primes: list[int]) -> int:
#         nums = primes.copy()  # do a deep copy
#         heapq.heapify(nums)  # create a heap
#         p = 1
#         for i in range(n - 1):
#             p = heapq.heappop(nums)  # take the smallest element
#             for prime in primes:
#                 heapq.heappush(nums, p * prime)  # add all those multiples with the smallest number
#                 if p % prime == 0:
#                     break
#         return p

sol = Solution()
number = 12
primes = [2, 7, 13, 19]
res = sol.nthSuperUglyNumber(number, primes)
print(res)
