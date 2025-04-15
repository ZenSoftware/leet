# https://leetcode.com/problems/merge-k-sorted-lists/
from typing import List, Optional
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        ListNode.__lt__ = lambda self, other: self.val < other.val

        heap = []
        for l in lists:
            if l:
                heap.append((l.val, l))

        heapify(heap)
        dummy = ListNode()
        pointer = dummy

        while heap:
            _, cur = heappop(heap)
            if cur.next:
                heappush(heap, (cur.next.val, cur.next))
            pointer.next = cur
            pointer = pointer.next

        return dummy.next
