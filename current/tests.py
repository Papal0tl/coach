"""
Tests for Invert Binary Tree.
"""

from agent_solution import Solution, TreeNode


def build_tree(values):
    """Build a tree from a LeetCode-style level-order list with None gaps."""
    if not values or values[0] is None:
        return None
    nodes = [None if v is None else TreeNode(v) for v in values]
    kids = nodes[::-1]
    root = kids.pop()
    for node in nodes:
        if node:
            if kids:
                node.left = kids.pop()
            if kids:
                node.right = kids.pop()
    return root


def tree_to_list(root):
    """Serialize a tree back to a LeetCode-style level-order list, trimming trailing Nones."""
    if root is None:
        return []
    out = []
    queue = [root]
    while queue:
        node = queue.pop(0)
        if node is None:
            out.append(None)
            continue
        out.append(node.val)
        queue.append(node.left)
        queue.append(node.right)
    while out and out[-1] is None:
        out.pop()
    return out


def test_example_1():
    solution = Solution()
    root = build_tree([4, 2, 7, 1, 3, 6, 9])
    result = solution.invertTree(root)
    assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]


def test_example_2():
    solution = Solution()
    root = build_tree([2, 1, 3])
    result = solution.invertTree(root)
    assert tree_to_list(result) == [2, 3, 1]


def test_empty_tree():
    solution = Solution()
    root = build_tree([])
    result = solution.invertTree(root)
    assert result is None


def test_single_node():
    solution = Solution()
    root = build_tree([1])
    result = solution.invertTree(root)
    assert tree_to_list(result) == [1]


def test_left_skewed():
    solution = Solution()
    root = build_tree([3, 2, None, 1])
    result = solution.invertTree(root)
    assert tree_to_list(result) == [3, None, 2, None, 1]


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_empty_tree()
    test_single_node()
    test_left_skewed()
    print("All tests passed.")
