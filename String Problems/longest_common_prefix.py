# Write a function to find
# the longest common prefix string
# amongst an array of strings.
#
# If there is no common prefix,
# return an empty string "".
#
#
#
# Example 1:
#
# Input: strs = ["flower","flow","flight"]
# Output: "fl"
# Example 2:
#
# Input: strs = ["dog","racecar","car"]
# Output: ""
# Explanation:
# There is no common prefix
# amongst the input strings.


class Solution:
    def longestCommonPrefix(self, v: list[str]) -> str:
        ans = ""
        v = sorted(v)
        first = v[0]
        last = v[-1]
        for i in range(min(len(first), len(last))):
            if (first[i] != last[i]):
                return ans
            ans += first[i]
        return ans
