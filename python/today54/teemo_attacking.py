# https://leetcode.com/problems/teemo-attacking/description/
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        total = 0
        prev = None
        for start in timeSeries:
            cur = [start, start + duration - 1]
            if prev is None or prev[1] < cur[0]:
                if prev is not None:
                    total += prev[1] - prev[0] + 1
                prev = cur
            else:
                prev[1] = cur[1]
        total += prev[1] - prev[0] + 1

        return total
