"""
Tests for Flatten Binary Tree to Linked List.
"""

from agent_solution import Solution, TreeNode


def build_tree(values):
    """Build a tree from a LeetCode-style level-order list with None gaps."""
    if not values or values[0] is None:
        return None
    root = TreeNode(values[0])
    queue = [root]
    i = 1
    while queue and i < len(values):
        node = queue.pop(0)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.left = TreeNode(v)
                queue.append(node.left)
        if i < len(values):
            v = values[i]
            i += 1
            if v is not None:
                node.right = TreeNode(v)
                queue.append(node.right)
    return root


def flattened_to_list(root):
    """Walk the right-only chain after flatten(), asserting left is always None."""
    result = []
    cur = root
    while cur:
        assert cur.left is None, "left pointer must be None after flatten"
        result.append(cur.val)
        cur = cur.right
    return result


def test_example_1():
    root = build_tree([1, 2, 5, 3, 4, None, 6])
    Solution().flatten(root)
    assert flattened_to_list(root) == [1, 2, 3, 4, 5, 6]


def test_empty_tree():
    root = build_tree([])
    Solution().flatten(root)
    assert root is None


def test_single_node():
    root = build_tree([0])
    Solution().flatten(root)
    assert flattened_to_list(root) == [0]


def test_left_only_chain():
    # 3 -> 2 -> 1 as left children; pre-order is 3,2,1
    root = TreeNode(3, left=TreeNode(2, left=TreeNode(1)))
    Solution().flatten(root)
    assert flattened_to_list(root) == [3, 2, 1]


def test_right_only_chain():
    # Already a right-only chain; should be unchanged
    root = TreeNode(1, right=TreeNode(2, right=TreeNode(3)))
    Solution().flatten(root)
    assert flattened_to_list(root) == [1, 2, 3]


def test_mixed_left_and_right_children():
    # 1(left=2,right=3); 2(right=4); 3(right=5) -> pre-order 1,2,4,3,5
    root = build_tree([1, 2, 3, None, 4, None, 5])
    Solution().flatten(root)
    assert flattened_to_list(root) == [1, 2, 4, 3, 5]


if __name__ == "__main__":
    test_example_1()
    test_empty_tree()
    test_single_node()
    test_left_only_chain()
    test_right_only_chain()
    test_mixed_left_and_right_children()
    print("All tests passed.")
