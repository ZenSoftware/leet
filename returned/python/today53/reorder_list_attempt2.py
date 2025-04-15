# https://leetcode.com/problems/reorder-list/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        dummy = ListNode()
        pointer = slow
        while pointer:
            next = pointer.next
            pointer.next = dummy.next
            dummy.next = pointer
            pointer = next

        left = head
        right = dummy.next
        while left != slow:
            left_next = left.next
            right_next = right.next
            left.next = right
            if left_next != slow:
                right.next = left_next
            left = left_next
            right = right_next
        return head
