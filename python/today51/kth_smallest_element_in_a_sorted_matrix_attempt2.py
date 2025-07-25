# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
from typing import List
from heapq import heapify, heappop, heappush


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        n = len(matrix)
        indexes = [0] * n
        heap = []
        for row in range(n):
            heap.append((matrix[row][0], row))
        heapify(heap)
        count = 0
        while count < k:
            cell, row = heappop(heap)
            indexes[row] += 1
            if indexes[row] < n:
                item = (matrix[row][indexes[row]], row)
                heappush(heap, item)
            count += 1
        return cell
