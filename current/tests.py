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


# Example 1: even length, palindrome
head = make_list([1, 2, 2, 1])
assert s.isPalindrome(head) is True
assert to_list(head) == [1, 2, 2, 1]  # list restored

# Example 2: even length, not a palindrome
head = make_list([1, 2])
assert s.isPalindrome(head) is False
assert to_list(head) == [1, 2]

# Odd length, palindrome
head = make_list([1, 2, 3, 2, 1])
assert s.isPalindrome(head) is True

# Odd length, not a palindrome
head = make_list([1, 2, 3, 4, 5])
assert s.isPalindrome(head) is False

# Single node
head = make_list([7])
assert s.isPalindrome(head) is True

# Two equal nodes
head = make_list([3, 3])
assert s.isPalindrome(head) is True

print("All tests passed.")
