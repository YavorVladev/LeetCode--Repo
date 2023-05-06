# You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
#
# Increment the large integer by one and return the resulting array of digits.

class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        lst = [str(i) for i in digits]
        s = ''
        for i in lst:
            s += i
        n = int(s) + 1
        n = str(n)
        temp = []
        for i in n:
            temp.append(i)
        r = [int(i) for i in temp]
        return r


                                     # Different Solution


# class Solution:
#     def plusOne(self, digits: List[int]) -> List[int]:
#         carry = 1
#         for i in range(len(digits) - 1, -1, -1):
#             digits[i] += carry
#             carry = digits[i] // 10
#             digits[i] %= 10
#             if not carry:
#                 break
#         if carry:
#             digits.insert(0, carry)
#         return digits


sol = Solution()
numbers = [9]
result = sol.plusOne(numbers)
print(result)
