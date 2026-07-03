# Agent reference solution — do not read until after your attempt.

from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # Find the middle using slow/fast pointers.
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Reverse the second half in place.
        prev = None
        cur = slow
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt
        second_head = prev

        # Compare first half with reversed second half.
        first, second = head, second_head
        is_pal = True
        while second:
            if first.val != second.val:
                is_pal = False
                break
            first = first.next
            second = second.next

        # Restore the list (not required by LeetCode, but good practice).
        prev = None
        cur = second_head
        while cur:
            nxt = cur.next
            cur.next = prev
            prev = cur
            cur = nxt

        return is_pal
