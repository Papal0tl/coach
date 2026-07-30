"""
Reference tests for Lowest Common Ancestor of a Binary Tree.

Run against agent_solution.py to validate, or point `SOLUTION_MODULE`
at attempt.py to check the user's implementation.
"""

import importlib
import sys
import unittest
from collections import deque

SOLUTION_MODULE = "agent_solution"


def build_tree(values):
    """
    Build a tree from a LeetCode-style level-order list (None = missing node).
    Returns (root, val_to_node) so tests can pass actual node objects for p/q.
    """
    mod = importlib.import_module(SOLUTION_MODULE)
    TreeNode = mod.TreeNode

    if not values or values[0] is None:
        return None, {}

    root = TreeNode(values[0])
    val_to_node = {values[0]: root}
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.left = TreeNode(val)
                val_to_node[val] = node.left
                queue.append(node.left)
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                val_to_node[val] = node.right
                queue.append(node.right)
    return root, val_to_node


class TestLowestCommonAncestor(unittest.TestCase):
    def setUp(self):
        mod = importlib.import_module(SOLUTION_MODULE)
        self.solution = mod.Solution()

    def test_example_1(self):
        root, nodes = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[5], nodes[1])
        self.assertEqual(result.val, 3)

    def test_example_2(self):
        root, nodes = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[5], nodes[4])
        self.assertEqual(result.val, 5)

    def test_two_node_tree(self):
        root, nodes = build_tree([1, 2])
        result = self.solution.lowestCommonAncestor(root, nodes[1], nodes[2])
        self.assertEqual(result.val, 1)

    def test_one_is_ancestor_of_other_deep(self):
        root, nodes = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[5], nodes[7])
        self.assertEqual(result.val, 5)

    def test_nodes_in_different_subtrees_deep(self):
        root, nodes = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[7], nodes[0])
        self.assertEqual(result.val, 3)

    def test_p_is_root(self):
        root, nodes = build_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[3], nodes[8])
        self.assertEqual(result.val, 3)

    def test_left_skewed_tree(self):
        root, nodes = build_tree([1, 2, None, 3, None, 4])
        result = self.solution.lowestCommonAncestor(root, nodes[4], nodes[2])
        self.assertEqual(result.val, 2)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("attempt", "agent_solution"):
        SOLUTION_MODULE = sys.argv.pop(1)
    unittest.main()
