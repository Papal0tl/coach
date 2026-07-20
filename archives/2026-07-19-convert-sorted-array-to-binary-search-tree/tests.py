"""
Tests for Convert Sorted Array to Binary Search Tree.

LeetCode accepts any valid height-balanced BST over the input values, so
tests check structural properties (BST order + balance) rather than an
exact tree shape.
"""

from agent_solution import Solution, TreeNode


def inorder(node):
    if node is None:
        return []
    return inorder(node.left) + [node.val] + inorder(node.right)


def height(node):
    if node is None:
        return 0
    return 1 + max(height(node.left), height(node.right))


def is_balanced(node):
    if node is None:
        return True
    left_h, right_h = height(node.left), height(node.right)
    return abs(left_h - right_h) <= 1 and is_balanced(node.left) and is_balanced(node.right)


def check(nums, root):
    if not nums:
        return root is None
    return inorder(root) == nums and is_balanced(root)


def run_tests():
    sol = Solution()
    cases = [
        [-10, -3, 0, 5, 9],
        [1, 3],
        [1],
        [1, 2, 3, 4, 5, 6, 7],  # odd length, exact power-of-two-minus-1
        [1, 2, 3, 4, 5, 6],  # even length
        list(range(1, 101)),  # larger input
    ]
    for nums in cases:
        root = sol.sortedArrayToBST(nums)
        ok = check(nums, root)
        status = "PASS" if ok else "FAIL"
        print(f"{status}: input={nums[:10]}{'...' if len(nums) > 10 else ''} inorder_ok_and_balanced={ok}")


if __name__ == "__main__":
    run_tests()
