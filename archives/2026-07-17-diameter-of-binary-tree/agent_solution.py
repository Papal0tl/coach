"""
Reference solution for Diameter of Binary Tree.

Pattern: recursive bottom-up combine, tracking two distinct quantities per call:
- the return value (subtree height, for the parent's own height computation)
- a side-effect update to running-best diameter (a path that terminates AT
  this node, using both children's heights, which is NOT the same thing the
  function returns to its caller)

Key insight: the diameter is not necessarily a path through the root, but it
IS always the case that the longest path has some single highest node where
it "turns" — at that node, the path length equals left_height + right_height
(no +1, since height is edge-count to the deepest leaf, and the path through
the node uses one edge into each subtree). Every node is a candidate turning
point, so we evaluate `left + right` at every node during a single post-order
pass and keep the running max.

Invariant: after depth(node) returns, `best` holds the max value of
(left_height + right_height) over every node visited so far in the subtree
rooted at the original root's already-explored portion; depth(node) itself
returns the height of `node` (edges to its deepest leaf), not the diameter.

Complexity: O(n) time (each node visited once), O(h) space for the recursion
stack, where h is the tree height.
"""

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.best = 0

        def depth(node: Optional[TreeNode]) -> int:
            if node is None:
                return 0
            left = depth(node.left)
            right = depth(node.right)
            self.best = max(self.best, left + right)
            return max(left, right) + 1

        depth(root)
        return self.best
