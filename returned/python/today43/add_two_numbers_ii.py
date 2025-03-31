# https://leetcode.com/problems/add-two-numbers-ii/description/
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        def get_num(l: Optional[ListNode]) -> int:
            res = 0
            while l:
                res *= 10
                res += l.val
                l = l.next
            return res

        n1 = get_num(l1)
        n2 = get_num(l2)

        dummy = ListNode()
        head = dummy
        for c in str(n1 + n2):
            head.next = ListNode(int(c))
            head = head.next
        return dummy.next
