# Given a string s consisting of words and spaces,
# return the length of the last word in the string.
#
# A word is a maximal substring
# consisting of non-space characters only.
#
#
#
# Example 1:
#
# Input: s = "Hello World"
# Output: 5
# Explanation: The last word is "World" with length 5.


class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.split()[-1]
        return len(s)

#     Time Complexity O(1)


sol = Solution()
text = "   fly me   to   the moon  "
result = sol.lengthOfLastWord(text)
print(result)

sol1 = Solution()
text = "Hello World"
result = sol.lengthOfLastWord(text)
print(result)

sol2 = Solution()
text = "luffy is still joyboy"
result = sol.lengthOfLastWord(text)
print(result)
