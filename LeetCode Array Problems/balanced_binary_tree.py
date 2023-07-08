# Given a binary tree, determine if it is height-balanced.

class Solution(object):
    def isBalanced(self, root):
        return (self.Height(root) >= 0)

    def Height(self, root):
        if root is None:  return 0
        leftheight, rightheight = self.Height(root.left), self.Height(root.right)
        if leftheight < 0 or rightheight < 0 or abs(leftheight - rightheight) > 1:  return -1
        return max(leftheight, rightheight) + 1


sol = Solution()
root = [3, 9, 20, None, None, 15, 7]
res = sol.isBalanced(root)
print(res)
