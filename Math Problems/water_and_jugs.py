# You are given two jugs with capacities jug1Capacity and jug2Capacity liters.
# There is an infinite amount of water supply available. Determine whether it
# is possible to measure exactly targetCapacity liters using these two jugs.
#
# If targetCapacity liters of water are measurable, you must have targetCapacity
# liters of water contained within one or both buckets by the end.
#
# Operations allowed:
#
# Fill any of the jugs with water.
# Empty any of the jugs.
# Pour water from one jug into another till the other jug is completely full,
# or the first jug itself is empty.
#
#


# Example 1:
#
# Input: jug1Capacity = 2, jug2Capacity = 6, targetCapacity = 5
# Output: false
# Example 2:
#
# Input: jug1Capacity = 1, jug2Capacity = 2, targetCapacity = 3
# Output: true


import math


class Solution:
    def canMeasureWater(self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int) -> bool:
        if jug1Capacity + jug2Capacity < targetCapacity:
            return False

        gcd_of_j1_and_j2 = math.gcd(jug1Capacity, jug2Capacity)
        return targetCapacity % gcd_of_j1_and_j2 == 0

# Time Complexity O(1)