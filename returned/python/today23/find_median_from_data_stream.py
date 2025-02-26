# https://leetcode.com/problems/find-median-from-data-stream/
from heapq import heappush, heappop

class MedianFinder:

    def __init__(self):
        self.left = []
        self.right = []

    def addNum(self, num: int) -> None:
        if len(self.left) == 0:
            self._pushLeft(num)
            return
 
        if num <= self._peekLeft():
            self._pushLeft(num)
        else:
            self._pushRight(num)

        while len(self.left) < len(self.right):
            self._pushLeft(self._popRight())
        while len(self.left) - 1 > len(self.right):
            self._pushRight(self._popLeft())

    def findMedian(self) -> float:
        if len(self.left) == len(self.right):
            return (self._peekLeft() + self._peekRight()) / 2
        else:
            return self._peekLeft()
    
    def _popLeft(self) -> int:
        return -heappop(self.left)

    def _popRight(self) -> int:
        return heappop(self.right)

    def _pushLeft(self, num: int):
        heappush(self.left, -num)
    
    def _pushRight(self, num: int):
        heappush(self.right, num)

    def _peekLeft(self):
        return -self.left[0]

    def _peekRight(self):
        return self.right[0]