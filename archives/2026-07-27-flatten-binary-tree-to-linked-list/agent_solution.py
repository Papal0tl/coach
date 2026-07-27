"""
Agent reference solution for Flatten Binary Tree to Linked List.

This file is separate from the user's attempt. Do not reveal it by default.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        """
        Morris-style in-place flatten, O(n) time, O(1) extra space.

        Invariant: when we arrive at `cur`, everything to the left of `cur`
        in pre-order has already been flattened and is no longer reachable
        through `cur.left`. We only ever need to fix up `cur`'s own left
        subtree (if any) before moving on.
        """
        cur = root
        while cur:
            if cur.left:
                # Find the rightmost node of the left subtree: this is the
                # last node in the left subtree's own pre-order sequence,
                # and it must connect to cur's original right subtree so
                # the overall pre-order order is preserved.
                predecessor = cur.left
                while predecessor.right:
                    predecessor = predecessor.right
                predecessor.right = cur.right
                cur.right = cur.left
                cur.left = None
            cur = cur.right
