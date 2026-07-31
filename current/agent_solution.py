"""
Agent reference solution for Binary Tree Maximum Path Sum.

Not shown to the user during coaching unless the mode allows a full reveal.
"""


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        best = float("-inf")

        def gain(node):
            nonlocal best
            if node is None:
                return 0
            left_gain = max(gain(node.left), 0)
            right_gain = max(gain(node.right), 0)
            # A path "through" this node may use both children (bend here).
            best = max(best, node.val + left_gain + right_gain)
            # But a path this node can *offer upward* to its parent may only
            # use one side, since a path cannot branch.
            return node.val + max(left_gain, right_gain)

        gain(root)
        return best
