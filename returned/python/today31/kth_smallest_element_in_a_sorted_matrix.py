# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
from typing import List
from heapq import heapify, heappush, heappop

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS = len(matrix)
        heap = []
        for r in range(ROWS):
            item = (matrix[r][0], r, 0)
            heap.append(item)
        heapify(heap)

        count = 0
        while heap:
            val, r, c = heappop(heap)
            count += 1
            if count >= k:
                return val
            if c+1 < len(matrix[r]):
                item = (matrix[r][c+1], r, c+1)
                heappush(heap, item)