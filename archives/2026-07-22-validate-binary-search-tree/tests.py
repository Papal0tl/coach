"""
Tests for Validate Binary Search Tree.

Run with the reference solution by default:

    python3 tests.py

Run against the user's attempt instead:

    python3 tests.py attempt
"""

import sys


def build_tree(TreeNode, values):
    """Build a binary tree from a LeetCode-style level-order list with None gaps."""
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


def run_tests(module_name):
    module = __import__(module_name)
    TreeNode = module.TreeNode
    Solution = module.Solution

    cases = [
        ([2, 1, 3], True),
        ([5, 1, 4, None, None, 3, 6], False),
        ([1], True),
        ([1, 1], False),  # duplicate values are not valid
        ([2147483647], True),  # max 32-bit int, boundary check
        ([-2147483648], True),  # min 32-bit int
        ([5, 4, 6, None, None, 3, 7], False),  # 3 < 5 but placed in right subtree
        ([10, 5, 15, None, None, 6, 20], False),  # 6 < 10 but placed under 15's left
        ([3, 1, 5, 0, 2, 4, 6], True),
        ([1, None, 2, None, 3], True),  # right-skewed, strictly increasing
    ]

    failures = 0
    for values, expected in cases:
        root = build_tree(TreeNode, values)
        got = Solution().isValidBST(root)
        status = "PASS" if got == expected else "FAIL"
        if got != expected:
            failures += 1
        print(f"{status}: input={values!r} expected={expected} got={got}")

    print(f"\n{len(cases) - failures}/{len(cases)} passed")
    return failures == 0


if __name__ == "__main__":
    target = sys.argv[1] if len(sys.argv) > 1 else "agent_solution"
    ok = run_tests(target)
    sys.exit(0 if ok else 1)
