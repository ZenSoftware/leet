# https://leetcode.com/problems/merge-k-sorted-lists/description/
from typing import List, Optional
from heapq import heapify, heappop, heappush


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
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
