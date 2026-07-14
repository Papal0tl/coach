"""
Agent reference solution for Binary Tree Inorder Traversal.

Two approaches are included:
1. Recursive (trivial, given as a baseline).
2. Iterative with an explicit stack (the standard follow-up).

Pattern: tree traversal, explicit-stack simulation of recursion.
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        return self._inorder_iterative(root)

    def _inorder_recursive(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []

        def visit(node: Optional[TreeNode]) -> None:
            if node is None:
                return
            visit(node.left)
            result.append(node.val)
            visit(node.right)

        visit(root)
        return result

    def _inorder_iterative(self, root: Optional[TreeNode]) -> List[int]:
        result: List[int] = []
        stack: List[TreeNode] = []
        cur = root

        # Invariant: `stack` holds the chain of ancestors (all still-unvisited
        # in the "node" sense) along the current left spine, from root down
        # to `cur`'s parent. We walk left as far as possible, then pop, visit,
        # and step right.
        while cur is not None or stack:
            while cur is not None:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            result.append(cur.val)
            cur = cur.right

        return result
