# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = [n for n in lists if n is not None]
        heapify(heap)
        dummy = ListNode(None)
        pointer = dummy

        while heap:
            cur = heappop(heap)
            if cur.next:
                heappush(heap, cur.next)
            pointer.next = cur
            pointer = pointer.next

        return dummy.next
