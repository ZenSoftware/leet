from typing import Optional

class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cache = set()

        while head:
            if head in cache:
                return True
            cache.add(head)
            head = head.next

        return False