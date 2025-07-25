# https://leetcode.com/problems/data-stream-as-disjoint-intervals/description/
from typing import List

class SummaryRanges:

    def __init__(self):
        self.intervals = []

    def addNum(self, value: int) -> None:
        iv = self.intervals
        for i in range(len(iv)):
            if i+1 < len(iv) and iv[i][1] + 1 == value and iv[i+1][0] - 1 == value:
                iv[i][1] = iv[i+1][1]
                del iv[i+1]
                break
            elif iv[i][0] - 1 == value:
                iv[i][0] = value
                break
            elif iv[i][1] + 1 == value:
                iv[i][1] = value
                break
            elif iv[i][0] <= value <= iv[i][1]:
                break
            elif value < iv[i][0]:
                iv.insert(i, [value, value])
                break
        else:
            iv.append([value, value])

    def getIntervals(self) -> List[List[int]]:
        return self.intervals