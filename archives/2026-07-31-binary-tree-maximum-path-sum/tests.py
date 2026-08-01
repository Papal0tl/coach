"""
Tests for Binary Tree Maximum Path Sum.

Run against either agent_solution.Solution or attempt.Solution by editing
the import below.
"""

from agent_solution import Solution, TreeNode


def build(values):
    """Build a tree from a LeetCode-style level-order list with None gaps."""
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = list(nodes[1:])
    root = nodes[0]
    frontier = [root]
    i = 0
    while frontier and i < len(kids):
        node = frontier.pop(0)
        if i < len(kids):
            node.left = kids[i]
            if kids[i] is not None:
                frontier.append(kids[i])
            i += 1
        if i < len(kids):
            node.right = kids[i]
            if kids[i] is not None:
                frontier.append(kids[i])
            i += 1
    return root


def run_tests():
    sol = Solution()
    cases = [
        ([1, 2, 3], 6),
        ([-10, 9, 20, None, None, 15, 7], 42),
        ([1], 1),
        ([-3], -3),
        ([-1, -2, -3], -1),  # all negative: best path is the single max node
        ([2, -1], 2),  # negative child should be excluded
        ([1, -2, 3], 4),  # only the positive branch should be attached
        ([1, None, 2, None, 3], 6),  # right skew
    ]
    for values, expected in cases:
        root = build(values)
        got = sol.maxPathSum(root)
        status = "PASS" if got == expected else "FAIL"
        print(f"{status}: input={values} expected={expected} got={got}")


if __name__ == "__main__":
    run_tests()
