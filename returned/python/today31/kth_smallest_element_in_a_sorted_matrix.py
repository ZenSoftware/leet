# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/description/
from typing import List
from collections import defaultdict

class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        ROWS = len(matrix)
        COLS = len(matrix[0])
        counts = defaultdict(int)
        for r in range(ROWS):
            for c in range(COLS):
                counts[matrix[r][c]] += 1
        counts = dict(sorted(counts.items()))
        
        ans_count = 0
        for n, c in counts.items():
            ans_count += c
            if ans_count >= k:
                return n