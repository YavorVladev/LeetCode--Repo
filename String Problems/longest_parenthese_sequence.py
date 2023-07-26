# Given a string containing just the characters '(' and ')',
# return the length of the longest valid (well-formed) parentheses substring


# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:
#
# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".
# Example 3:
#
# Input: s = ""
# Output: 0

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        # base case check
        if not s:
            return 0
        stack = [-1]  #
        max_len = 0
        for i, ch in enumerate(s):
            if ch == '(':
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    curr_len = i - stack[len(stack) - 1]
                    max_len = max(curr_len, max_len)
        return max_len

#     Time Complexity O(n)
