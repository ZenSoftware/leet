# https://leetcode.com/problems/insertion-sort-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(float('-inf'), next=head)
        current = head
        prev = dummy
        while current:
            next = current.next
            if current.val < prev.val:
                temp = dummy
                while current.val > temp.next.val:
                    temp = temp.next
                current.next = temp.next
                temp.next = current
                prev.next = next
            else:
                prev = prev.next
            current = next
        
        return dummy.next
