"""
Tests for Add Two Numbers.
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
    values = []
    while node is not None:
        values.append(node.val)
        node = node.next
    return values


def run(solution, l1_values, l2_values):
    l1 = build(l1_values)
    l2 = build(l2_values)
    result = solution.addTwoNumbers(l1, l2)
    return to_list(result)


def test_examples():
    solution = Solution()

    assert run(solution, [2, 4, 3], [5, 6, 4]) == [7, 0, 8]
    assert run(solution, [0], [0]) == [0]
    assert run(solution, [9, 9, 9, 9, 9, 9, 9], [9, 9, 9, 9]) == [8, 9, 9, 9, 0, 0, 0, 1]


def test_unequal_length():
    solution = Solution()

    # 1 + 999 = 1000 -> reversed [0,0,0,1]
    assert run(solution, [1], [9, 9, 9]) == [0, 0, 0, 1]
    # 99 + 1 = 100 -> reversed [0,0,1]
    assert run(solution, [9, 9], [1]) == [0, 0, 1]


def test_no_carry_needed():
    solution = Solution()

    # 12 + 34 (reversed: 21 + 43) = 543 reversed digits check via direct sum
    # l1 = [2,1] -> 12, l2 = [4,3] -> 34, sum = 46 -> reversed [6,4]
    assert run(solution, [2, 1], [4, 3]) == [6, 4]


def test_trailing_carry_single_digit():
    solution = Solution()

    # 5 + 5 = 10 -> reversed [0,1]
    assert run(solution, [5], [5]) == [0, 1]


def test_same_length_all_nines():
    solution = Solution()

    # 99 + 99 = 198 -> reversed [8,9,1]
    assert run(solution, [9, 9], [9, 9]) == [8, 9, 1]


if __name__ == "__main__":
    test_examples()
    test_unequal_length()
    test_no_carry_needed()
    test_trailing_carry_single_digit()
    test_same_length_all_nines()
    print("All tests passed.")
