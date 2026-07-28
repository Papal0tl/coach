"""
Agent reference solution for Construct Binary Tree from Preorder and Inorder Traversal.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        # Map value -> index in inorder for O(1) split-point lookup.
        index_of = {val: i for i, val in enumerate(inorder)}
        self.pre_pos = 0

        def build(left: int, right: int) -> Optional[TreeNode]:
            if left > right:
                return None
            root_val = preorder[self.pre_pos]
            self.pre_pos += 1
            root = TreeNode(root_val)
            mid = index_of[root_val]
            # Preorder is [root, ...left subtree..., ...right subtree...],
            # so the next unconsumed preorder value always belongs to the
            # left subtree first, then the right subtree.
            root.left = build(left, mid - 1)
            root.right = build(mid + 1, right)
            return root

        return build(0, len(inorder) - 1)
