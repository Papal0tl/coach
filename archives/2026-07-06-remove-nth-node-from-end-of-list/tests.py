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


def run_case(values, n, expected):
    head = build_list(values)
    result = Solution().removeNthFromEnd(head, n)
    actual = to_list(result)
    status = "PASS" if actual == expected else "FAIL"
    print(f"{status}: input={values}, n={n}, expected={expected}, actual={actual}")


if __name__ == "__main__":
    run_case([1, 2, 3, 4, 5], 2, [1, 2, 3, 5])
    run_case([1], 1, [])
    run_case([1, 2], 1, [1])
    run_case([1, 2], 2, [2])
    run_case([1, 2, 3], 3, [2, 3])
    run_case([1, 2, 3, 4, 5], 5, [2, 3, 4, 5])
