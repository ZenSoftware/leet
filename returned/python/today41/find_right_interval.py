# https://leetcode.com/problems/find-right-interval/description/
from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)
        indexed = [(interval, i) for i, interval in enumerate(intervals)]
        indexed.sort()

        def search(end, lo=0):
            left, right = lo, n - 1
            while left <= right:
                mid = (left + right) // 2
                start = indexed[mid][0][0]
                if end > start:
                    left = mid + 1
                else:
                    right = mid - 1
            return left if left < n else None

        result = [-1] * n
        for lo, [(_, end), index] in enumerate(indexed):
            pos = search(end, lo)
            if pos is not None:
                result[index] = indexed[pos][1]
        return result
