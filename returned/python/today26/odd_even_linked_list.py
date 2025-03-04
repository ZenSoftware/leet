# https://leetcode.com/problems/odd-even-linked-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        odd_dummy = ListNode(None)
        even_dummy = ListNode(None)
        odd = odd_dummy
        even = even_dummy
        is_odd = True
        
        while head:
            if is_odd:
                odd.next = head
                odd = odd.next
            else:
                even.next = head
                even = even.next
            is_odd = not is_odd
            head = head.next
        
        odd.next = even_dummy.next
        even.next = None

        return odd_dummy.next