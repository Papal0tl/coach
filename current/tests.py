"""
Tests for Merge k Sorted Lists.
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
    while node is not None:
        out.append(node.val)
        node = node.next
    return out


def test_example_basic():
    lists = [build([1, 4, 5]), build([1, 3, 4]), build([2, 6])]
    result = Solution().mergeKLists(lists)
    assert to_list(result) == [1, 1, 2, 3, 4, 4, 5, 6]


def test_empty_array():
    result = Solution().mergeKLists([])
    assert result is None


def test_array_of_one_empty_list():
    result = Solution().mergeKLists([None])
    assert result is None


def test_single_list():
    lists = [build([1, 2, 3])]
    result = Solution().mergeKLists(lists)
    assert to_list(result) == [1, 2, 3]


def test_mix_of_empty_and_nonempty():
    lists = [None, build([1]), None, build([0, 2])]
    result = Solution().mergeKLists(lists)
    assert to_list(result) == [0, 1, 2]


def test_all_empty_lists():
    lists = [None, None, None]
    result = Solution().mergeKLists(lists)
    assert result is None


def test_duplicate_values_across_lists():
    lists = [build([1, 1, 1]), build([1, 1]), build([1])]
    result = Solution().mergeKLists(lists)
    assert to_list(result) == [1, 1, 1, 1, 1, 1]


def test_negative_values():
    lists = [build([-5, -1, 3]), build([-4, 0])]
    result = Solution().mergeKLists(lists)
    assert to_list(result) == [-5, -4, -1, 0, 3]


if __name__ == "__main__":
    test_example_basic()
    test_empty_array()
    test_array_of_one_empty_list()
    test_single_list()
    test_mix_of_empty_and_nonempty()
    test_all_empty_lists()
    test_duplicate_values_across_lists()
    test_negative_values()
    print("All tests passed.")
