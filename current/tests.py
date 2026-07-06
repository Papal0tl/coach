"""
Tests for Swap Nodes in Pairs.
"""

from agent_solution import ListNode, Solution


def build_list(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head is not None:
        out.append(head.val)
        head = head.next
    return out


def run_case(values, expected):
    head = build_list(values)
    result = Solution().swapPairs(head)
    actual = to_list(result)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: input={values}, expected={expected}, actual={actual}")


if __name__ == "__main__":
    run_case([1, 2, 3, 4], [2, 1, 4, 3])
    run_case([], [])
    run_case([1], [1])
    run_case([1, 2], [2, 1])
    run_case([1, 2, 3], [2, 1, 3])
    run_case([1, 2, 3, 4, 5, 6], [2, 1, 4, 3, 6, 5])
