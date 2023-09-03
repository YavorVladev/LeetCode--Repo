# You are given n points in the plane that are all distinct,
# where points[i] = [xi, yi]. A boomerang is a tuple of points
# (i, j, k) such that the distance between i and j equals the distance
# between i and k (the order of the tuple matters).
#
# Return the number of boomerangs.
#
#
#
# Example 1:
#
# Input: points = [[0,0],[1,0],[2,0]]
# Output: 2
# Explanation: The two boomerangs are [[1,0],[0,0],[2,0]] and [[1,0],[2,0],[0,0]].

# Example 2:
#
# Input: points = [[1,1],[2,2],[3,3]]
# Output: 2
# Example 3:
#
# Input: points = [[1,1]]
# Output: 0

class Solution:
    def numberOfBoomerangs(self, points: list[list[int]]) -> int:
        if len(points) < 3:
            return 0
        import math

        def distance(p1, p2):
            x1, y1 = p1
            x2, y2 = p2
            return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)

        def getBoomerangs(p1_idx):
            p1 = points[p1_idx]

            distances = defaultdict(lambda: 0)
            for p2_idx, p2 in enumerate(points):
                if p2_idx == p1_idx:
                    continue

                dist = distance(p1, p2)
                distances[dist] += 1

            return sum(
                val * (val - 1)
                for val in distances.values()
                if val >= 2
            )

        result = sum(
            getBoomerangs(idx)
            for idx in range(len(points))
        )
        return result

#     Time Complexity O(n)
