"""
Local tests for Kth Smallest Element in a BST.

Run: python3 tests.py
"""

from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list with None gaps."""
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            left_val = values[i]
            i += 1
            if left_val is not None:
                node.left = TreeNode(left_val)
                queue.append(node.left)
        if i < len(values):
            right_val = values[i]
            i += 1
            if right_val is not None:
                node.right = TreeNode(right_val)
                queue.append(node.right)
    return root


def run_tests(solution_cls):
    sol = solution_cls()
    cases = [
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
        ([1], 1, 1),
        ([2, 1, 3], 2, 2),
        ([2, 1, 3], 1, 1),
        ([2, 1, 3], 3, 3),
        ([5, 3, 6, 2, 4, None, None, 1], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 6, 6),
        ([4, 3, None, 2, None, 1], 1, 1),  # left-skewed tree
        ([7, 3, 15, None, None, 9, 20], 4, 15),
    ]

    passed = 0
    for i, (values, k, expected) in enumerate(cases, start=1):
        root = build_tree(values)
        result = sol.kthSmallest(root, k)
        status = "PASS" if result == expected else "FAIL"
        if result == expected:
            passed += 1
        print(f"Test {i}: {status} (input={values}, k={k}, expected={expected}, got={result})")

    print(f"\n{passed}/{len(cases)} tests passed")


if __name__ == "__main__":
    import sys
    import os

    sys.path.insert(0, os.path.dirname(__file__))
    from agent_solution import Solution as AgentSolution

    print("=== Testing agent_solution.py ===")
    run_tests(AgentSolution)
