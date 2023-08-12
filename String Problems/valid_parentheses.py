class Solution:
    def isValid(self, s: str) -> bool:

        is_good = False

        for i in range(len(s) - 1):
            if s[i] == "(":
                if s[i + 1] == ")":
                    is_good = True
                else:
                    is_good = False

            elif s[i] == "[":
                if s[i + 1] == "]":
                    is_good = True
                else:
                    is_good = False

            elif s[i] == "{":
                if s[i + 1] == "}":
                    is_good = True
                else:
                    is_good = False

        return is_good

# Time Complexity O(n)

sol = Solution()
text = "(){}}{"
res = sol.isValid(text)
print(res)