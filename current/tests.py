"""
Tests for Copy List with Random Pointer.
"""

from agent_solution import Node, Solution


def build(pairs):
    """pairs: list of [val, random_index_or_None] -> head Node, or None for empty."""
    if not pairs:
        return None
    nodes = [Node(val) for val, _ in pairs]
    for i, node in enumerate(nodes):
        node.next = nodes[i + 1] if i + 1 < len(nodes) else None
        random_index = pairs[i][1]
        node.random = nodes[random_index] if random_index is not None else None
    return nodes[0]


def flatten(head):
    """head -> list of [val, random_index_or_None], using node identity for indices."""
    nodes = []
    cur = head
    while cur is not None:
        nodes.append(cur)
        cur = cur.next
    index_of = {node: i for i, node in enumerate(nodes)}
    return [
        [node.val, index_of[node.random] if node.random is not None else None]
        for node in nodes
    ]


def assert_deep_copy(original_pairs, head, copy_head):
    """Verify copy has same structure but no shared node objects with the original."""
    assert flatten(copy_head) == original_pairs

    orig_nodes = set()
    cur = head
    while cur is not None:
        orig_nodes.add(id(cur))
        cur = cur.next

    cur = copy_head
    while cur is not None:
        assert id(cur) not in orig_nodes
        cur = cur.next


def test_example_1():
    pairs = [[7, None], [13, 0], [11, 4], [10, 2], [1, 0]]
    head = build(pairs)
    copy_head = Solution().copyRandomList(head)
    assert_deep_copy(pairs, head, copy_head)


def test_example_2():
    pairs = [[1, 1], [2, 1]]
    head = build(pairs)
    copy_head = Solution().copyRandomList(head)
    assert_deep_copy(pairs, head, copy_head)


def test_example_3():
    pairs = [[3, None], [3, 0], [3, None]]
    head = build(pairs)
    copy_head = Solution().copyRandomList(head)
    assert_deep_copy(pairs, head, copy_head)


def test_empty_list():
    assert Solution().copyRandomList(None) is None


def test_single_node_random_self():
    pairs = [[5, 0]]
    head = build(pairs)
    copy_head = Solution().copyRandomList(head)
    assert_deep_copy(pairs, head, copy_head)


def test_no_random_pointers():
    pairs = [[1, None], [2, None], [3, None]]
    head = build(pairs)
    copy_head = Solution().copyRandomList(head)
    assert_deep_copy(pairs, head, copy_head)


def test_original_unmodified():
    pairs = [[1, 2], [2, 0], [3, 1]]
    head = build(pairs)
    before = flatten(head)
    Solution().copyRandomList(head)
    assert flatten(head) == before


if __name__ == "__main__":
    test_example_1()
    test_example_2()
    test_example_3()
    test_empty_list()
    test_single_node_random_self()
    test_no_random_pointers()
    test_original_unmodified()
    print("All tests passed.")
