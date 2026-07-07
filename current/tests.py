"""
Tests for Reverse Nodes in k-Group.
"""

from agent_solution import ListNode, Solution


def build(values):
    dummy = ListNode(0)
    cur = dummy
    for v in values:
        cur.next = ListNode(v)
        cur = cur.next
    return dummy.next


def to_list(head):
    out = []
    while head:
        out.append(head.val)
        head = head.next
    return out


def test_examples():
    solution = Solution()
    assert solution is not None


if __name__ == "__main__":
    test_examples()
