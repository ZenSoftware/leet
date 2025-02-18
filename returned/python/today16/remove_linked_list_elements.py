# https://leetcode.com/problems/remove-linked-list-elements/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        prev = dummy

        while head:
            if head.val == val:
                prev.next = head.next
            else:
                prev = prev.next
            head = head.next
        
        return dummy.next
