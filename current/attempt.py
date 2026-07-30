"""
User attempt for Path Sum III.

Write your reasoning in English comments when useful.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root, targetSum):
        """
        :type root: Optional[TreeNode]
        :type targetSum: int
        :rtype: int
        """
        def dfs(node, target):
            if not node:
                return 0
            ans = 0
            if node.val == target:
                ans += 1
            ans += dfs(node.left, target - node.val)
            ans += dfs(node.right, target - node.val)
            return ans
        if not root:
            return 0
        return (dfs(root, targetSum) + self.pathSum(root.left, targetSum) + self.pathSum(root.right, targetSum))
