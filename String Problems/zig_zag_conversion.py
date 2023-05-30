# The string "PAYPALISHIRING" is
# written in a zigzag pattern on a given
# number of rows like this:
# (you may want to display this pattern
# in a fixed font for better legibility)
#
# P   A   H   N
# A P L S I I G
# Y   I   R


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
        answer = ''
        n = len(s)
        diff = 2 * (numRows - 1)
        diagonal_diff = diff
        second_index = 0
        index = 0
        for i in range(numRows):
            index = i
            while index < n:
                answer += s[index]
                if i != 0 and i != numRows - 1:
                    diagonal_diff = diff - 2 * i
                    second_index = index + diagonal_diff
                    if second_index < n:
                        answer += s[second_index]
                index += diff
        return answer


sol = Solution()
given_string = "PAHNAPLSIIGYIR"
given_rows = 3
res = sol.convert(given_string, given_rows)
print(res)
