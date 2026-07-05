from agent_solution import ListNode, Solution


def build_list_with_cycle(values, pos):
    if not values:
        return None

    nodes = [ListNode(v) for v in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]

    if pos != -1:
        nodes[-1].next = nodes[pos]

    return nodes[0]


def run_tests():
    sol = Solution()

    assert sol.hasCycle(build_list_with_cycle([3, 2, 0, -4], 1)) is True
    assert sol.hasCycle(build_list_with_cycle([1, 2], 0)) is True
    assert sol.hasCycle(build_list_with_cycle([1], -1)) is False
    assert sol.hasCycle(build_list_with_cycle([], -1)) is False
    assert sol.hasCycle(build_list_with_cycle([1], 0)) is True  # single-node self-loop
    assert sol.hasCycle(build_list_with_cycle([1, 2, 3, 4, 5], -1)) is False

    print("All tests passed.")


if __name__ == "__main__":
    run_tests()
