# https://leetcode.com/problems/teemo-attacking/description/
from typing import List


class Solution:
    def findPoisonedDuration(self, timeSeries: List[int], duration: int) -> int:
        intervals = []
        for start in timeSeries:
            cur = [start, start + duration - 1]
            if not intervals or intervals[-1][1] < cur[0]:
                intervals.append(cur)
            else:
                intervals[-1][1] = cur[1]

        time = 0
        for interval in intervals:
            time += interval[1] - interval[0] + 1

        return time
