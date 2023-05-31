# Given a string columnTitle that
# represents the column title as
# appears in an Excel sheet, return its corresponding column number.
#
# For example:
#
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28
# ...
#
#
# Example 1:
#
# Input: columnTitle = "A"
# Output: 1
# Example 2:
#
# Input: columnTitle = "AB"
# Output: 28
# Example 3:
#
# Input: columnTitle = "ZY"
# Output: 701

class Solution:
    def titleToNumber(self, columnTitle: str) -> int:
        ans, pos = 0, 0
        for letter in reversed(columnTitle):
            digit = ord(letter) - 64
            ans += digit * 26 ** pos
            pos += 1

        return ans


# class Solution:
#     def titleToNumber(self, columnTitle: str) -> int:
#         data = {"A": 1, "B": 2, ...... "Z": 26}
#
#         n = len(data) - 1
#         answer = 0
#
#         for letter in (columnTitle):
#             letter = data[letter] * 26 ** n
#             n -= 1
#             answer += letter
#
#         return answer


sol = Solution()
columnTitle = "A"
result = sol.titleToNumber(columnTitle)
print(result)
