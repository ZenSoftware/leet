# https://leetcode.com/problems/swap-nodes-in-pairs/
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
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(next=head)
        p = dummy

        while p and p.next and p.next.next:
            p1 = p
            p2 = p.next
            p3 = p.next.next
            p4 = p3.next if p3.next else None

            p2.next = p4
            p3.next = p2
            p1.next = p3

            p = p.next.next

        return dummy.next