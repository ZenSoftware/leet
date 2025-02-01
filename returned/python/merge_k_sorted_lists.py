# https://leetcode.com/problems/merge-k-sorted-lists/description/
from typing import List, Optional
from heapq import heapify, heappop, heappush

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
    def __lt__(self, other):
        self.val < other.val
    def __le__(self, other):
        self.val <= other.val
    def __gt__(self, other):
        self.val > other.val
    def __ge__(self, other):
        self.val >= other.val

def to_nodes(elements: List[int]) -> Optional[ListNode]:
    if not elements:
        return None
    prev = None
    for e in reversed(elements):
        node = ListNode(e)
        node.next = prev
        prev = node
    return prev

def to_node_list(elements: List[List[int]]) -> List[Optional[ListNode]]:
    result = []
    for e in elements:
        result.append(to_nodes(e))
    return result


def to_array(head: Optional[ListNode]) -> List[int]:
    if not head:
        return []
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        dummy = ListNode()
        current = dummy

        heapify(lists)

        while lists:
            smallest = heappop(lists)
            current.next = smallest
            if smallest.next:
                heappush(lists, smallest.next)
            current = current.next

        return dummy.next