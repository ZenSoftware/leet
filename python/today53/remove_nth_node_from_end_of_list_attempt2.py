# https://leetcode.com/problems/remove-nth-node-from-end-of-list/description/
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

    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        pointer = head
        trail = dummy
        count = 0
        while pointer:
            if count >= n:
                trail = trail.next
            pointer = pointer.next
            count += 1
        trail.next = trail.next.next
        return dummy.next
