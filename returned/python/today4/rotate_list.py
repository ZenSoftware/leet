# https://leetcode.com/problems/rotate-list/description/
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_nodes(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    prev = None
    for el in reversed(elements):
        node = ListNode(el)
        node.next = prev
        prev = node
    return prev

def to_array(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []
    result: List[int] = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy = ListNode(next=head)
        pointer = dummy
        trail = dummy
        count = 0

        while pointer.next:
            count += 1
            if count > k:
                trail = trail.next
            pointer = pointer.next

        if k < count:
            pointer.next = dummy.next
            dummy.next = trail.next
            trail.next = None
        else:
            k = k % count
            if k > 0:
                pointer = dummy
                trail = dummy
                count = 0

                while pointer.next:
                    count += 1
                    if count > k:
                        trail = trail.next
                    pointer = pointer.next
    
                pointer.next = dummy.next
                dummy.next = trail.next
                trail.next = None

        return dummy.next