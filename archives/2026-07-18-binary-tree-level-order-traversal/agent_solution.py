"""
Reference solution for Binary Tree Level Order Traversal.

Pattern: breadth-first traversal (BFS) using a FIFO queue, processing one
full level per outer-loop iteration.

Key insight: a plain BFS queue mixes nodes from different levels together as
soon as you push children in. The fix is to snapshot the queue's current
length at the top of each outer-loop iteration (this is exactly the number
of nodes belonging to the current level, since every node already in the
queue was enqueued by the previous level's processing) and only pop that
many nodes before pushing any new children.

Invariant: at the top of each outer-loop iteration, the queue contains
exactly the nodes of one level, in left-to-right order, and nothing else.

Complexity: O(n) time (each node enqueued and dequeued once), O(n) space
for the queue and the output (worst case: a fully "wide" tree, e.g. the
last level of a complete tree holds ~n/2 nodes).
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None:
            return []

        result = []
        queue = deque([root])

        while queue:
            level_size = len(queue)
            level_values = []
            for _ in range(level_size):
                node = queue.popleft()
                level_values.append(node.val)
                if node.left is not None:
                    queue.append(node.left)
                if node.right is not None:
                    queue.append(node.right)
            result.append(level_values)

        return result
