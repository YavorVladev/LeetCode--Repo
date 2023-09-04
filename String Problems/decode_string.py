# Given an encoded string, return its decoded string.
#
# The encoding rule is: k[encoded_string], where the encoded_string
# inside the square brackets is being repeated exactly k times.
# Note that k is guaranteed to be a positive integer.
#
# You may assume that the input string is always valid;
# there are no extra white spaces, square brackets are well-formed, etc.
# Furthermore, you may assume that the original data does not contain any digits
# and that digits are only for those repeat numbers, k. For example, there will not
# be input like 3a or 2[4].
#
# The test cases are generated so that the length of the output will never exceed 105.
#
#
#
# Example 1:
#
# Input: s = "3[a]2[bc]"
# Output: "aaabcbc"

# Example 2:
#
# Input: s = "3[a2[c]]"
# Output: "accaccacc"

# Example 3:
#
# Input: s = "2[abc]3[cd]ef"
# Output: "abcabccdcdcdef"


class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        cur = ""
        k = 0
        for c in s:
            if c == "[":
                stack.append((cur, k))
                cur, k = "", 0  # reset global vars
            elif c == "]":
                enc, n = stack.pop()
                cur = enc + n * cur
            elif c.isdigit():
                k = k * 10 + int(c)  # for two and three digit numbers
            else:
                cur += c  # track the lower case letters
        return cur
