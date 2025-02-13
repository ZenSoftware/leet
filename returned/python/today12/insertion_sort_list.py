# https://leetcode.com/problems/insertion-sort-list/description/
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(float('-inf'), next=head)
        pointer = head
        prev = dummy
        while pointer:
            next_node = pointer.next
            if pointer.val < prev.val:
                temp = dummy
                while pointer.val > temp.next.val:
                    temp = temp.next
                pointer.next = temp.next
                temp.next = pointer
                prev.next = next_node
            else:
                prev = prev.next
            pointer = next_node
        
        return dummy.next
