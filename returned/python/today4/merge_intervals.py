# https://leetcode.com/problems/merge-intervals/description/
from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        result: List[List[int]] = []
        prev_min = intervals[0][0]
        prev_max = intervals[0][1]
        for interval in intervals:
            if prev_max >= interval[0] and prev_min <= interval[1]:
                prev_min = min(prev_min, interval[0])
                prev_max = max(prev_max, interval[1])
            else:
                result.append([prev_min, prev_max])
                prev_min = interval[0]
                prev_max = interval[1]
        result.append([prev_min, prev_max])
        return result