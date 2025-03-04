# https://leetcode.com/problems/count-of-range-sum/
from typing import List

class BinaryIndexTree:
    def __init__(self, nums: List[int] = []):
        self.tree = [0] * (len(nums) + 1)
        for i, n in enumerate(nums):
            self.update(i, n)
        
    def update(self, i: int, val: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def query(self, i: int) -> int:
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

class Solution:
    def countRangeSum(self, nums: List[int], lower: int, upper: int) -> int:
        tree = BinaryIndexTree(nums)
        count = 0
        for start in range(len(nums)):
            for end in range(start, len(nums)):
                rangeSum = tree.query(end) - tree.query(start-1)
                if lower <= rangeSum <= upper:
                    count += 1
        return count