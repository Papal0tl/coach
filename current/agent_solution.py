"""
Reference solution for Validate Binary Search Tree.

Approach: recursive bounds propagation. Each recursive call carries an open
interval (low, high) that the current node's value must fall strictly inside.
Descending left tightens the upper bound to the parent's value; descending
right tightens the lower bound. This enforces the *global* BST property
(every node in a subtree, not just the immediate child) without needing
sentinel integers, so it also generalizes beyond the 32-bit constraint.
"""

from typing import Optional


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def isValidBST(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: bool
        """
        def validate(node, low, high):
            if node is None:
                return True
            if low is not None and node.val <= low:
                return False
            if high is not None and node.val >= high:
                return False
            return validate(node.left, low, node.val) and validate(node.right, node.val, high)

        return validate(root, None, None)
