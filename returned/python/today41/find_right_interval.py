# https://leetcode.com/problems/find-right-interval/description/
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indexed = [(interval, i) for i, interval in enumerate(intervals)]
        indexed.sort()
        answer = [-1] * n
        for i in range(0, n):
            j_interval, j = indexed[i]
            for i2 in range(i, n):
                k_interval, k = indexed[i2]
                if j_interval[1] <= k_interval[0]:
                    answer[j] = k
                    break
        return answer
