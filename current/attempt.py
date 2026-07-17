"""
User attempt for Symmetric Tree.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root.left == root.right:
            return True
        else:
            return False
        self.isSymmetric(root.left)
        self.isSymmetric(root.right)
