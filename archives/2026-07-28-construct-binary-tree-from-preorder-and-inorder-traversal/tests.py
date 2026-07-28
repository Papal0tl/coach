"""
Tests for Construct Binary Tree from Preorder and Inorder Traversal.
"""

from agent_solution import Solution, TreeNode


def trees_equal(a, b):
    if a is None and b is None:
        return True
    if a is None or b is None:
        return False
    return (
        a.val == b.val
        and trees_equal(a.left, b.left)
        and trees_equal(a.right, b.right)
    )


def test_example_1():
    # preorder = [3,9,20,15,7], inorder = [9,3,15,20,7]
    # tree: 3 -> left 9, right 20 -> left 15, right 7
    solution = Solution()
    root = solution.buildTree([3, 9, 20, 15, 7], [9, 3, 15, 20, 7])

    expected = TreeNode(3, TreeNode(9), TreeNode(20, TreeNode(15), TreeNode(7)))
    assert trees_equal(root, expected)


def test_example_2_single_node():
    solution = Solution()
    root = solution.buildTree([-1], [-1])

    expected = TreeNode(-1)
    assert trees_equal(root, expected)


def test_left_skewed():
    # tree: 3 -> left 2 -> left 1
    solution = Solution()
    root = solution.buildTree([3, 2, 1], [1, 2, 3])

    expected = TreeNode(3, TreeNode(2, TreeNode(1)))
    assert trees_equal(root, expected)


def test_right_skewed():
    # tree: 1 -> right 2 -> right 3
    solution = Solution()
    root = solution.buildTree([1, 2, 3], [1, 2, 3])

    expected = TreeNode(1, None, TreeNode(2, None, TreeNode(3)))
    assert trees_equal(root, expected)


def test_full_small_tree():
    # tree:      1
    #          /   \
    #         2     3
    #        / \   / \
    #       4   5 6   7
    preorder = [1, 2, 4, 5, 3, 6, 7]
    inorder = [4, 2, 5, 1, 6, 3, 7]
    solution = Solution()
    root = solution.buildTree(preorder, inorder)

    expected = TreeNode(
        1,
        TreeNode(2, TreeNode(4), TreeNode(5)),
        TreeNode(3, TreeNode(6), TreeNode(7)),
    )
    assert trees_equal(root, expected)


def test_left_child_only_at_root():
    # tree: 1 -> left 2
    solution = Solution()
    root = solution.buildTree([1, 2], [2, 1])

    expected = TreeNode(1, TreeNode(2))
    assert trees_equal(root, expected)


if __name__ == "__main__":
    test_example_1()
    test_example_2_single_node()
    test_left_skewed()
    test_right_skewed()
    test_full_small_tree()
    test_left_child_only_at_root()
    print("All tests passed.")
