"""
Tests for Symmetric Tree.
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


def test_symmetric_example():
    solution = Solution()
    root = build_tree([1, 2, 2, 3, 4, 4, 3])
    assert solution.isSymmetric(root) is True
    assert solution.isSymmetricIterative(root) is True


def test_asymmetric_example():
    solution = Solution()
    root = build_tree([1, 2, 2, None, 3, None, 3])
    assert solution.isSymmetric(root) is False
    assert solution.isSymmetricIterative(root) is False


def test_single_node():
    solution = Solution()
    root = build_tree([1])
    assert solution.isSymmetric(root) is True
    assert solution.isSymmetricIterative(root) is True


def test_asymmetric_missing_child():
    solution = Solution()
    root = build_tree([1, 2, 2, None, 2])
    assert solution.isSymmetric(root) is False
    assert solution.isSymmetricIterative(root) is False


def test_empty_tree():
    solution = Solution()
    root = build_tree([])
    assert solution.isSymmetric(root) is True
    assert solution.isSymmetricIterative(root) is True


def test_symmetric_with_duplicate_values():
    solution = Solution()
    root = build_tree([2, 3, 3, 4, 5, 5, 4])
    assert solution.isSymmetric(root) is True
    assert solution.isSymmetricIterative(root) is True


if __name__ == "__main__":
    test_symmetric_example()
    test_asymmetric_example()
    test_single_node()
    test_asymmetric_missing_child()
    test_empty_tree()
    test_symmetric_with_duplicate_values()
    print("All tests passed.")
