# A valid IP address consists of exactly four integers separated by single dots.
# Each integer is between 0 and 255 (inclusive) and cannot have leading zeros.
#
# For example, "0.1.2.201" and "192.168.1.1" are valid IP addresses, but "0.011.255.245",
# "192.168.1.312" and "192.168@1.1" are invalid IP addresses.
# Given a string s containing only digits, return all possible
# valid IP addresses that can be formed by inserting dots into s. You are not
# allowed to reorder or remove any digits in s. You may return the valid IP addresses in any order.
#
#
#
# Example 1:
#
# Input: s = "25525511135"
# Output: ["255.255.11.135","255.255.111.35"]

# Example 2:
#
# Input: s = "0000"
# Output: ["0.0.0.0"]

# Example 3:
#
# Input: s = "101023"
# Output: ["1.0.10.23","1.0.102.3","10.1.0.23","10.10.2.3","101.0.2.3"]


class Solution:
    def valid(self, temp: str) -> bool:
        if len(temp) > 3 or len(temp) == 0:
            return False
        if len(temp) > 1 and temp[0] == '0':
            return False
        if len(temp) and int(temp) > 255:
            return False
        return True

    def solve(self, ans, output, ind, s, dots):
        if dots == 3:
            if self.valid(s[ind:]):
                ans.append(output + s[ind:])
            return
        for i in range(ind, min(ind + 3, len(s))):
            if self.valid(s[ind:i + 1]):
                new_output = output + s[ind:i + 1] + '.'
                self.solve(ans, new_output, i + 1, s, dots + 1)

    def restoreIpAddresses(self, s: str) -> List[str]:
        ans = []
        self.solve(ans, "", 0, s, 0)
        return ans


#     Time Complexity O(n)

# SECOND SOLUTION COMING SOON



# def restore_ip_addresses(s):
#     def backtrack(start, path):
#         if len(path) == 4:
#             if start == len(s):
#                 valid_ips.append(".".join(path))
#             return
#
#         for i in range(1, 4):
#             if start + i <= len(s):
#                 segment = s[start:start+i]
#                 if (segment[0] != '0' or segment == '0') and int(segment) <= 255:
#                     backtrack(start + i, path + [segment])
#
#     valid_ips = []
#     backtrack(0, [])
#     return valid_ips

#     Time Complexity O(n)

sol = Solution()
s = "101023"
res = sol.restoreIpAddresses(s)
print(res)
