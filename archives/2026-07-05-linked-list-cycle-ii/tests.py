"""
Tests for Linked List Cycle II.
"""

from agent_solution import ListNode, Solution


def build_list(values, pos):
    """Build a linked list from values; pos is the 0-indexed node the tail
    connects to for a cycle, or -1 for no cycle. Returns (head, node_at_pos)."""
    if not values:
        return None, None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]
        return nodes[0], nodes[pos]

    return nodes[0], None


def test_cycle_in_middle():
    head, entry = build_list([3, 2, 0, -4], 1)
    assert Solution().detectCycle(head) is entry


def test_cycle_at_head():
    head, entry = build_list([1, 2], 0)
    assert Solution().detectCycle(head) is entry


def test_no_cycle_single_node():
    head, _ = build_list([1], -1)
    assert Solution().detectCycle(head) is None


def test_empty_list():
    assert Solution().detectCycle(None) is None


def test_self_loop_single_node():
    head, entry = build_list([1], 0)
    assert Solution().detectCycle(head) is entry


def test_cycle_at_tail():
    head, entry = build_list([1, 2, 3, 4], 3)
    assert Solution().detectCycle(head) is entry


def test_no_cycle_long_list():
    head, _ = build_list([1, 2, 3, 4, 5, 6], -1)
    assert Solution().detectCycle(head) is None


if __name__ == "__main__":
    test_cycle_in_middle()
    test_cycle_at_head()
    test_no_cycle_single_node()
    test_empty_list()
    test_self_loop_single_node()
    test_cycle_at_tail()
    test_no_cycle_long_list()
    print("All tests passed.")
