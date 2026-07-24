"""
User attempt for Kth Smallest Element in a BST.

Write your reasoning in English comments when useful.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        def inorder(node):
            if not node:
                return None
            left = inorder(node.left)
            if left is not None:
                return left
            self.count += 1
            if self.count == k:
                return node.val
            return inorder(node.right)
        return inorder(root)