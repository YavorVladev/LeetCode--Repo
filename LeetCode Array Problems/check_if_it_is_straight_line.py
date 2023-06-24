# You are given an array coordinates,
# coordinates[i] = [x, y], where [x, y]
# represents the coordinate of a point.
# Check if these points make a straight line in the XY plane.
#
#
#
#
#
# Example 1:
#
#
#
# Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
# Output: true
# Example 2:
#
#
#
# Input: coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
# Output: false

class Solution:
    def checkStraightLine(self, coordinates: list[list[int]]) -> bool:
        (x1, y1), (x2, y2) = coordinates[:2]
        for i in range(2, len(coordinates)):
            (x, y) = coordinates[i]
            if (y2 - y1) * (x1 - x) != (y1 - y) * (x2 - x1):
                return False
        return True


sol = Solution()
cor = [[1, 2], [2, 3], [3, 4], [4, 5], [5, 6], [6, 7]]
# cor = [[1, 2], [2, 4], [4, 6], [4, 5], [5, 6], [6, 7]]
# cor = [[1, 2], [2, 5], [7, 8], [9, 9], [5, 6], [6, 7]]
res = sol.checkStraightLine(cor)
print(res)


