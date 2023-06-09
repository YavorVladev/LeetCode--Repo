# Given a linked list, swap every two
# adjacent nodes and return its head.
# You must solve the problem without modifying
# the values in the list's nodes (i.e., only nodes themselves may be changed.)
#
#
#
# Example 1:
#
#
# Input: head = [1,2,3,4]
# Output: [2,1,4,3]
# Example 2:

#
# Input: head = []
# Output: []
# Example 3:
#
# Input: head = [1]
# Output: [1]

class Solution:
    def swapPairs(self, head):
        if not (head and head.next): return head

        newHead = head.next
        head.next, newHead.next = self.swapPairs(head.next.next), head

        return newHead

    # Time Complexity O(n)


sol = Solution()
nodes = [1, 2, 3, 4]
res = sol.swapPairs(nodes)
print(res)

