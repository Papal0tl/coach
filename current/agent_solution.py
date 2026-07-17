"""
Agent reference solution for Symmetric Tree.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        return self._is_mirror(root.left, root.right)

    def _is_mirror(self, t1: Optional[TreeNode], t2: Optional[TreeNode]) -> bool:
        if t1 is None and t2 is None:
            return True
        if t1 is None or t2 is None:
            return False
        if t1.val != t2.val:
            return False
        return self._is_mirror(t1.left, t2.right) and self._is_mirror(t1.right, t2.left)

    def isSymmetricIterative(self, root: Optional[TreeNode]) -> bool:
        if root is None:
            return True
        queue = [(root.left, root.right)]
        while queue:
            t1, t2 = queue.pop(0)
            if t1 is None and t2 is None:
                continue
            if t1 is None or t2 is None:
                return False
            if t1.val != t2.val:
                return False
            queue.append((t1.left, t2.right))
            queue.append((t1.right, t2.left))
        return True
