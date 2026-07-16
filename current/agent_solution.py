"""
Agent reference solution for Invert Binary Tree.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        root.left, root.right = self.invertTree(root.right), self.invertTree(root.left)
        return root
