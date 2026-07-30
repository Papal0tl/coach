"""
Reference tests for Path Sum III.

Run against agent_solution.py to validate, or point `SOLUTION_MODULE`
at attempt.py to check the user's implementation.
"""

import importlib
import sys
import unittest
from collections import deque

SOLUTION_MODULE = "agent_solution"


def build_tree(values):
    """Build a tree from a LeetCode-style level-order list (None = missing node)."""
    if not values or values[0] is None:
        return None

    mod = importlib.import_module(SOLUTION_MODULE)
    TreeNode = mod.TreeNode

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1
    while queue and i < len(values):
        node = queue.popleft()
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.left = TreeNode(val)
                queue.append(node.left)
        if i < len(values):
            val = values[i]
            i += 1
            if val is not None:
                node.right = TreeNode(val)
                queue.append(node.right)
    return root


class TestPathSumIII(unittest.TestCase):
    def setUp(self):
        mod = importlib.import_module(SOLUTION_MODULE)
        self.solution = mod.Solution()

    def test_example_1(self):
        root = build_tree([10, 5, -3, 3, 2, None, 11, 3, -2, None, 1])
        self.assertEqual(self.solution.pathSum(root, 8), 3)

    def test_example_2(self):
        root = build_tree([5, 4, 8, 11, None, 13, 4, 7, 2, None, None, 5, 1])
        self.assertEqual(self.solution.pathSum(root, 22), 3)

    def test_empty_tree(self):
        root = build_tree([])
        self.assertEqual(self.solution.pathSum(root, 0), 0)

    def test_single_node_matches(self):
        root = build_tree([5])
        self.assertEqual(self.solution.pathSum(root, 5), 1)

    def test_single_node_no_match(self):
        root = build_tree([5])
        self.assertEqual(self.solution.pathSum(root, 1), 0)

    def test_negative_values(self):
        root = build_tree([1, -2, -3, 1, 3, -2, None, -1])
        self.assertEqual(self.solution.pathSum(root, -1), 4)

    def test_all_negative_target_zero(self):
        # chain of zeros: every contiguous subpath sums to 0
        root = build_tree([0, 0, 0, 0])
        self.assertEqual(self.solution.pathSum(root, 0), 8)

    def test_path_must_go_downward_not_start_at_root(self):
        # path 5 -> 3 (not through root) must count
        root = build_tree([1, 5, None, 3])
        self.assertEqual(self.solution.pathSum(root, 3), 1)
        self.assertEqual(self.solution.pathSum(root, 8), 1)


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] in ("attempt", "agent_solution"):
        SOLUTION_MODULE = sys.argv.pop(1)
    unittest.main()
