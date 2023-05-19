# The set [1, 2, 3, ..., n] contains a
# total of n! unique permutations.
#
# By listing and labeling all of the
# permutations in order, we get the
# following sequence for n = 3:
#
# "123"
# "132"
# "213"
# "231"
# "312"
# "321"
# Given n and k, return the kth permutation sequence.

class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        numbers = [str(i) for i in range(1, n+1)]
        result = ""
        factorial = 1
        for i in range(2, n+1):
            factorial *= i

        k -= 1

        for i in range(n, 0, -1):
            factorial //= i
            index = k // factorial
            result += numbers[index]
            numbers.pop(index)
            k %= factorial

        return result


sol = Solution()
number = 3
exact_permutation = 6
result = sol.getPermutation(number, exact_permutation)
print(result)

