# https://leetcode.com/problems/kth-largest-element-in-an-array/
from typing import List
from heapq import heapify, heappop

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        neg_nums = list(map(lambda x: x * -1, nums))
        heapify(neg_nums)
        for _ in range(k):
            ans = heappop(neg_nums)
        return ans * -1
