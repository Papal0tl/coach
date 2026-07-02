from agent_solution import ListNode, Solution

s = Solution()


def make_list(vals):
    dummy = ListNode(0)
    cur = dummy
    for v in vals:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def make_intersecting(valsA, valsB, shared_vals):
    # Build shared tail
    shared_head = make_list(shared_vals)

    # Build unique prefixes
    headA = make_list(valsA)
    headB = make_list(valsB)

    # Attach shared tail to end of each prefix
    def tail(node):
        while node.next:
            node = node.next
        return node

    if headA:
        tail(headA).next = shared_head
    else:
        headA = shared_head

    if headB:
        tail(headB).next = shared_head
    else:
        headB = shared_head

    return headA, headB, shared_head


# Example 1: intersection at node val=8
headA, headB, shared = make_intersecting([4, 1], [5, 6, 1], [8, 4, 5])
assert s.getIntersectionNode(headA, headB) is shared

# Example 2: no intersection
headA = make_list([2, 6, 4])
headB = make_list([1, 5])
assert s.getIntersectionNode(headA, headB) is None

# Intersection at first node (identical lists from the start)
shared = make_list([1, 2, 3])
assert s.getIntersectionNode(shared, shared) is shared

# Intersection at last node only
headA, headB, shared = make_intersecting([1, 2], [3], [9])
assert s.getIntersectionNode(headA, headB) is shared

# Single-node lists, no intersection
headA = make_list([1])
headB = make_list([2])
assert s.getIntersectionNode(headA, headB) is None

# Single-node lists, intersection (same node)
node = ListNode(1)
assert s.getIntersectionNode(node, node) is node

# listA starts at intersection directly, listB has a prefix before it
shared = make_list([5, 6, 7])
headB = make_list([1, 2])
cur = headB
while cur.next:
    cur = cur.next
cur.next = shared
assert s.getIntersectionNode(shared, headB) is shared

print("All tests passed.")
