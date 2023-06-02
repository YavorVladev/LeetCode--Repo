# Calculate the average salary without including the
# highest and the lowest one.


class Solution:
    def average(self, salary: list[int]) -> float:
        salary.remove(max(salary))
        salary.remove(min(salary))
        return sum(salary) / len(salary)


sol = Solution()
salaries = [1000, 2000, 3000]
res = sol.average(salaries)
print(res)
