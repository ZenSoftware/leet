# https://leetcode.com/problems/remove-duplicates-from-sorted-list/description/
from typing import Optional, List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def to_nodes(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    prev = None
    for e in reversed(elements):
        node = ListNode(e)
        node.next = prev
        prev = node
    return prev

def to_array(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(None, head)
        p = dummy

        while p:
            if p.next and p.val == p.next.val:
                dup = p.next
                while dup.next and dup.val == dup.next.val:
                    dup = dup.next
                p.next = dup.next
            p = p.next

        return dummy.next