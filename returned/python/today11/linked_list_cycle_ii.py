# https://leetcode.com/problems/linked-list-cycle-ii/description/
from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        cache = set()

        while head.next:
            if head.next in cache:
                return head.next
            cache.add(head)
            head = head.next

        return None
