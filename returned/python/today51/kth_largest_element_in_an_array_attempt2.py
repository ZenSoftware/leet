# https://leetcode.com/problems/kth-largest-element-in-an-array/description/
from heapq import heapify, heappop
from typing import List


class Solution:
    """
    Time: O(klogn)
    Space: O(n)
    """

    def findKthLargest(self, nums: List[int], k: int) -> int:
        max_heap = [-n for n in nums]
        heapify(max_heap)
        for _ in range(k):
            res = heappop(max_heap)
        return -res
