# https://leetcode.com/problems/add-two-numbers-ii/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    """
    Time: O(5n)
    Space: O(1)
    """

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def reverse_list(l: Optional[ListNode]) -> Optional[ListNode]:
            dummy = ListNode(None)
            while l:
                next_node = l.next
                l.next = dummy.next
                dummy.next = l
                l = next_node
            return dummy.next

        l1 = reverse_list(l1)
        l2 = reverse_list(l2)

        res = ListNode(None)
        carry = 0
        while l1 or l2:
            d1, d2 = 0, 0
            if l1:
                d1 = l1.val
            if l2:
                d2 = l2.val

            total = d1 + d2 + carry
            if total >= 10:
                digit_node = ListNode(total - 10)
                carry = 1
            else:
                digit_node = ListNode(total)
                carry = 0
            digit_node.next = res.next
            res.next = digit_node

            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return res.next
