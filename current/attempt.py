"""
User attempt for Copy List with Random Pointer.

Write your reasoning in English comments when useful.
"""


class Solution:
    def copyRandomList(self, head):
        if head is None:
            return None

        map = {}
        cur = head
        while cur:
            map[cur] = Node(cur.val)
            cur = cur.next

        cur = head
        while cur:
            new_node = map[cur]
            if cur.next:
                new_node.next = map[cur.next]
            else:
                new_node.next = None
            if cur.random:
                new_node.random = map[cur.random]
            else:
                new_node.random = None
            cur = cur.next
        return map[head]
