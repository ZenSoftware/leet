# https://leetcode.com/problems/reverse-linked-list/
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

    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()

        while head:
            next = head.next
            head.next = dummy.next
            dummy.next = head
            head = next

        return dummy.next
