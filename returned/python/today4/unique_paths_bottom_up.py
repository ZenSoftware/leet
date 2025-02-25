# https://leetcode.com/problems/unique-paths/description/
from typing import Dict

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row = [1] * n

        for i in range(m-1):
            new_row = [1] * n
            for j in range(n-2, -1, -1):
                new_row[j] = row[j] + new_row[j+1]
            row = new_row

        return row[0]