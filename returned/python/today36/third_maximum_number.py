# https://leetcode.com/problems/third-maximum-number/description/
from typing import List
from heapq import heapify, heappop

class Solution:
    '''
    Time: O(n)
    Space: O(n)
    '''
    def thirdMax(self, nums: List[int]) -> int:
        max_heap = [-x for x in set(nums)]
        heapify(max_heap)
        if len(max_heap) < 3:
            return -max_heap[0]
        heappop(max_heap)
        heappop(max_heap)
        return -heappop(max_heap)