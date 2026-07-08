"""
Tests for Reverse Nodes in k-Group.
"""

from agent_solution import ListNode, Solution


def build(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_example_k2():
    head = build([1, 2, 3, 4, 5])
    result = Solution().reverseKGroup(head, 2)
    assert to_list(result) == [2, 1, 4, 3, 5]


def test_example_k3():
    head = build([1, 2, 3, 4, 5])
    result = Solution().reverseKGroup(head, 3)
    assert to_list(result) == [3, 2, 1, 4, 5]


def test_empty_list():
    head = build([])
    result = Solution().reverseKGroup(head, 2)
    assert to_list(result) == []


def test_single_node():
    head = build([1])
    result = Solution().reverseKGroup(head, 1)
    assert to_list(result) == [1]


def test_k_equals_length():
    head = build([1, 2, 3, 4])
    result = Solution().reverseKGroup(head, 4)
    assert to_list(result) == [4, 3, 2, 1]


def test_k_equals_one_is_noop():
    head = build([1, 2, 3, 4, 5])
    result = Solution().reverseKGroup(head, 1)
    assert to_list(result) == [1, 2, 3, 4, 5]


def test_exact_multiple_of_k():
    head = build([1, 2, 3, 4, 5, 6])
    result = Solution().reverseKGroup(head, 3)
    assert to_list(result) == [3, 2, 1, 6, 5, 4]


def test_remainder_shorter_than_k_left_untouched():
    head = build([1, 2, 3, 4, 5, 6, 7])
    result = Solution().reverseKGroup(head, 3)
    assert to_list(result) == [3, 2, 1, 6, 5, 4, 7]


if __name__ == "__main__":
    test_example_k2()
    test_example_k3()
    test_empty_list()
    test_single_node()
    test_k_equals_length()
    test_k_equals_one_is_noop()
    test_exact_multiple_of_k()
    test_remainder_shorter_than_k_left_untouched()
    print("all tests passed")
