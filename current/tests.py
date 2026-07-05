"""
Tests for Merge Two Sorted Lists.
"""

from agent_solution import ListNode, Solution


def build(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(node):
    out = []
    while node:
        out.append(node.val)
        node = node.next
    return out


def run(list1_values, list2_values, expected):
    solution = Solution()
    result = solution.mergeTwoLists(build(list1_values), build(list2_values))
    assert to_list(result) == expected, f"merge({list1_values}, {list2_values}) -> {to_list(result)}, expected {expected}"


def test_examples():
    run([1, 2, 4], [1, 3, 4], [1, 1, 2, 3, 4, 4])
    run([], [], [])
    run([], [0], [0])


def test_edge_cases():
    run([1], [], [1])
    run([], [1], [1])
    run([1, 1, 1], [1, 1], [1, 1, 1, 1, 1])
    run([-3, 0, 5], [-2, -1, 6], [-3, -2, -1, 0, 5, 6])
    run([1, 2, 3], [4, 5, 6], [1, 2, 3, 4, 5, 6])
    run([4, 5, 6], [1, 2, 3], [1, 2, 3, 4, 5, 6])


if __name__ == "__main__":
    test_examples()
    test_edge_cases()
    print("All tests passed.")
