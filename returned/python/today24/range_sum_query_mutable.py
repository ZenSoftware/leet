# https://leetcode.com/problems/range-sum-query-mutable/description/
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix = [0]
        for i in range(len(nums)):
            self.prefix.append(nums[i] + self.prefix[i])

    def update(self, index: int, val: int) -> None:
        if self.nums[index] != val:
            self.nums[index] = val
            for i in range(index, len(self.nums)):
                self.prefix[i+1] = self.nums[i] + self.prefix[i]

    def sumRange(self, left: int, right: int) -> int:
        return self.prefix[right+1] - self.prefix[left]
