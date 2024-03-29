# Given two strings ransomNote and magazine,
# return true if ransomNote can be constructed
# by using the letters from magazine and false otherwise.
#
# Each letter in magazine can only be used once in ransomNote.
#
#
#
# Example 1:
#
# Input: ransomNote = "a", magazine = "b"
# Output: false
# Example 2:
#
# Input: ransomNote = "aa", magazine = "ab"
# Output: false
# Example 3:
#
# Input: ransomNote = "aa", magazine = "aab"
# Output: true


class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:

        for i in set(ransomNote):
            if magazine.count(i) < ransomNote.count(i):
                return False
            return True


# Time Complexity O(n)
sol = Solution()
ransom = "aa"
mag = "ab"
res = sol.canConstruct(ransom, mag)
print(res)

# Time complexity O(n)
