# https://leetcode.com/problems/merge-two-sorted-lists/
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
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        elif not list2:
            return list1

        if list1.val <= list2.val:
            head = list1
            p1 = list1
            p2 = list2
        else:
            head = list2
            p1 = list2
            p2 = list1

        while p1 and p2:
            while p1.next and p2 and (p1.next.val <= p2.val):
                p1 = p1.next

            if p1.val <= p2.val:
                p1next = p1.next
                p2next = p2.next
                p1.next = p2
                p2.next = p1next
                p1 = p2
                p2 = p2next
            else:
                p1 = p1.next

        return head