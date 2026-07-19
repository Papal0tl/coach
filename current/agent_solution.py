"""
Reference solution for Convert Sorted Array to Binary Search Tree.

Pattern: recursive divide-and-conquer over an index range of the array,
mirroring the split/recurse/combine shape from sort-list and merge-k-sorted-
lists, but building a tree instead of a list.

Key insight: any contiguous sorted sub-range can become a valid BST subtree
by picking its middle element as the subtree root (BST property: everything
left of the middle is smaller, everything right is larger, both already
true because the array is sorted). Choosing the *middle* index specifically
(rather than, say, the first or last) is what keeps the two recursive
subtrees within one node of each other in height, which is exactly the
height-balanced requirement.

Invariant: a call on range [lo, hi] returns the root of a valid,
height-balanced BST over exactly nums[lo..hi] (inclusive), or None when
lo > hi (empty range).

Complexity: O(n) time (each element becomes exactly one node once), O(log n)
additional space for the recursion stack (tree height is O(log n) because
the split is balanced), not counting the O(n) output tree itself.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> Optional[TreeNode]:
        def build(lo: int, hi: int) -> Optional[TreeNode]:
            if lo > hi:
                return None
            mid = (lo + hi) // 2
            node = TreeNode(nums[mid])
            node.left = build(lo, mid - 1)
            node.right = build(mid + 1, hi)
            return node

        return build(0, len(nums) - 1)
