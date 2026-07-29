"""
Reference solution for Path Sum III.
"""

from collections import defaultdict


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
        prefix_count = defaultdict(int)
        prefix_count[0] = 1

        def dfs(node, running_sum):
            if node is None:
                return 0

            running_sum += node.val
            count = prefix_count[running_sum - targetSum]

            prefix_count[running_sum] += 1
            count += dfs(node.left, running_sum)
            count += dfs(node.right, running_sum)
            prefix_count[running_sum] -= 1

            return count

        return dfs(root, 0)
