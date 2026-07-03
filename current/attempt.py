from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        vals = []

        cur = head
        while cur is not None:
            vals.append(cur.val)
            cur = cur.next
        
        rev_val = []
        for i in range(len(vals), -1, -1, -1):
            rev_val.append(cur.val[i])

        if vals == rev_val:
            return true
        else:
            return false
