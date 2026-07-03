from agent_solution import ListNode, Solution

s = Solution()


def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    vals = []
    while head:
        vals.append(head.val)
        head = head.next
    return vals


# Example 1: normal list
head = make_list([1, 2, 3, 4, 5])
assert to_list(s.reverseList(head)) == [5, 4, 3, 2, 1]

# Example 2: two nodes
head = make_list([1, 2])
assert to_list(s.reverseList(head)) == [2, 1]

# Example 3: empty list
head = make_list([])
assert s.reverseList(head) is None

# Single node
head = make_list([7])
result = s.reverseList(head)
assert to_list(result) == [7]
assert result is head

# Negative and repeated values
head = make_list([-1, 0, -1, 5, 5])
assert to_list(s.reverseList(head)) == [5, 5, -1, 0, -1]

print("All tests passed.")
