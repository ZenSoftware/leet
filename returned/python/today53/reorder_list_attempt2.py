# https://leetcode.com/problems/reorder-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(n)
    Space: O(1)
    """

    def reorderList(self, head: Optional[ListNode]) -> None:
        if not head:
            return

        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        prev, cur = None, slow
        while cur:
            tmp = cur.next
            cur.next = prev
            prev = cur
            cur = tmp

        left, right = head, prev
        while right.next:
            tmp = left.next
            left.next = right
            left = tmp

            tmp = right.next
            right.next = left
            right = tmp
