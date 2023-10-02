# Given two integers representing the numerator and denominator of a fraction,
# return the fraction in string format.
#
# If the fractional part is repeating,
# enclose the repeating part in parentheses.
#
# If multiple answers are possible, return any of them.
#
# It is guaranteed that the length of the answer string is less
# than 104 for all the given inputs.
#
#
# -------------------------------------------#
# Example 1:                                 #
# -------------------------------------------#
# Input: numerator = 1, denominator = 2      #
# Output: "0.5"                              #
# Example 2:                                 #
# -------------------------------------------#
# Input: numerator = 2, denominator = 1      #
# Output: "2"                                #
# Example 3:                                 #
# -------------------------------------------#
# Input: numerator = 4, denominator = 333    #
# Output: "0.(012)"                          #
# -------------------------------------------#


class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        neg = (numerator < 0 and denominator > 0) or (numerator > 0 and denominator < 0)
        numerator = abs(numerator)
        denominator = abs(denominator)

        res = [str(numerator // denominator)]
        index = 1
        numerator %= denominator
        if numerator != 0:
            res.append(".")
            index += 1
        dic = {}

        while numerator != 0:
            if numerator in dic:
                res = res[:dic[numerator]] + ["("] + res[dic[numerator]:] + [")"]
                break
            else:
                dic[numerator] = index
            numerator *= 10
            res.append(str(numerator // denominator))
            index += 1
            numerator %= denominator
        return "".join(res) if not neg else "-" + "".join(res)

#     Time Complexity O(n)

sol = Solution()
num = 1
dom = 2
res = sol.fractionToDecimal(num, dom)
print(res)


