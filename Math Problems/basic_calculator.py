# Given a string s representing a valid expression, implement
# a basic calculator to evaluate it, and return the result of the evaluation.
#
# Note: You are not allowed to use any built-in function
# which evaluates strings as mathematical expressions, such as eval().

# Input: s = "(1+(4+5+2)-3)+(6+8)"
# Output: 23

class Solution:
    def calculate(self, expression: str) -> int:
        # recurse when brackets encountered
        def helper(s, index):
            result = 0
            sign = 1
            currnum = 0
            i = index
            while i < len(s):
                c = s[i]
                if c.isdigit():
                    currnum = currnum * 10 + int(c)
                elif c in '-+':  # update the sign
                    result += sign * currnum
                    sign = 1 if c == '+' else -1
                    currnum = 0
                elif c == '(':  # pause and call helper for the next section
                    res, i = helper(s, i + 1)
                    result += sign * res
                elif c == ')':  # return results, index to resume to caller
                    result += sign * currnum
                    break
                i += 1
            # return result and current index
            return result, i

        if not expression:
            return 0
        # enclose input with brackets and call helper
        return helper('(' + expression + ')', 0)[0]
