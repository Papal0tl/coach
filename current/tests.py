"""
Tests for Sort List (LC 148).

Run against either agent_solution.py or attempt.py by editing the import.
"""

from agent_solution import ListNode, Solution


def build(values):
    dummy = ListNode()
    tail = dummy
    for v in values:
        tail.next = ListNode(v)
        tail = tail.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def run_tests():
    sol = Solution()
    cases = [
        ([4, 2, 1, 3], [1, 2, 3, 4]),
        ([-1, 5, 3, 4, 0], [-1, 0, 3, 4, 5]),
        ([], []),
        ([1], [1]),
        ([2, 1], [1, 2]),
        ([1, 1, 1], [1, 1, 1]),
        ([5, 4, 3, 2, 1], [1, 2, 3, 4, 5]),
        ([3, -2, -5, 0, 8, -8], [-8, -5, -2, 0, 3, 8]),
    ]

    passed = 0
    for i, (values, expected) in enumerate(cases):
        head = build(values)
        result = sol.sortList(head)
        actual = to_list(result)
        ok = actual == expected
        passed += ok
        status = "PASS" if ok else "FAIL"
        print(f"Test {i + 1}: {status} (input={values}, expected={expected}, got={actual})")

    print(f"\n{passed}/{len(cases)} tests passed")


if __name__ == "__main__":
    run_tests()
