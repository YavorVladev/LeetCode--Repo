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



# SECOND SOLUTION COMING SOON




# def fractionToDecimal(numerator, denominator):
#     if numerator == 0:
#         return "0"
#
#     result = []
#
#     # Handle the sign
#     if (numerator < 0) ^ (denominator < 0):
#         result.append("-")
#
#     numerator = abs(numerator)
#     denominator = abs(denominator)
#
#     # Calculate the integer part
#     result.append(str(numerator // denominator))
#
#     # Calculate the fractional part
#     remainder = numerator % denominator
#     if remainder == 0:
#         return ''.join(result)
#
#     result.append(".")
#     fraction_part = []
#     seen_remainders = {}
#
#     while remainder != 0:
#         if remainder in seen_remainders:
#             # Repeating pattern detected
#             start_repeat_index = seen_remainders[remainder]
#             non_repeat_part = fraction_part[:start_repeat_index]
#             repeat_part = fraction_part[start_repeat_index:]
#             return ''.join(result) + ''.join(non_repeat_part) + "(" + ''.join(repeat_part) + ")"
#
#         seen_remainders[remainder] = len(fraction_part)
#         remainder *= 10
#         fraction_part.append(str(remainder // denominator))
#         remainder %= denominator
#
#     return ''.join(result) + ''.join(fraction_part)

# Time Complexity O(n)




sol = Solution()
num = 1
dom = 2
res = sol.fractionToDecimal(num, dom)
print(res)







