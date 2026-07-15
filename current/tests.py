"""
Tests for Maximum Depth of Binary Tree.

Run with: python3 current/tests.py
"""

from typing import List, Optional

from agent_solution import Solution, TreeNode


def build_tree(values: List[Optional[int]]) -> Optional[TreeNode]:
    """Build a tree from a LeetCode-style level-order list with None gaps."""
    if not values or values[0] is None:
        return None

    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[1:]
    root = nodes[0]
    queue = [root]
    i = 0
    while queue and i < len(kids):
        node = queue.pop(0)
        if i < len(kids):
            node.left = kids[i]
            if node.left is not None:
                queue.append(node.left)
            i += 1
        if i < len(kids):
            node.right = kids[i]
            if node.right is not None:
                queue.append(node.right)
            i += 1
    return root


def run_tests() -> None:
    sol = Solution()
    cases = [
        ([3, 9, 20, None, None, 15, 7], 3),
        ([], 0),
        ([1], 1),
        ([1, None, 2], 2),
        ([1, 2], 2),
        ([1, 2, 3, 4, 5, 6, 7], 3),
        ([1, 2, None, 3, None, 4, None, 5], 5),
    ]

    for i, (values, expected) in enumerate(cases):
        root = build_tree(values)
        got = sol.maxDepth(root)
        status = "PASS" if got == expected else "FAIL"
        print(f"Case {i}: {status} input={values} expected={expected} got={got}")
        assert got == expected, f"Case {i} failed: expected {expected}, got {got}"

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
