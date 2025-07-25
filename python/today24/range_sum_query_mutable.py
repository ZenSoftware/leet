# https://leetcode.com/problems/range-sum-query-mutable/description/
# https://www.youtube.com/watch?v=T_xe9p7-zwQ
# https://www.youtube.com/watch?v=uSFzHCZ4E-8
from typing import List

class BinaryIndexTree:
    def __init__(self, nums: List[int]):
        self.tree = [0] * (len(nums)+1)
        for i, v in enumerate(nums):
            self.update(i, v)

    def update(self, i: int, val: int) -> None:
        i += 1
        while i < len(self.tree):
            self.tree[i] += val
            i += i & -i

    def get_sum(self, i: int) -> int:
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

class NumArray:
    def __init__(self, nums: List[int]):
        self.nums = nums
        self.bit = BinaryIndexTree(nums)

    def update(self, index: int, val: int) -> None:
        delta = val - self.nums[index]
        self.bit.update(index, delta)
        self.nums[index] = val

    def sumRange(self, left: int, right: int) -> int:
        return self.bit.get_sum(right) - self.bit.get_sum(left-1)