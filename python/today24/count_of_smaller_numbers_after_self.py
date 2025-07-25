# https://leetcode.com/problems/count-of-smaller-numbers-after-self/
from typing import List

class BinaryIndexTree:
    def __init__(self, size: int):
        self.tree = [0] * (size+1)

    def update(self, i: int, value: int):
        i += 1
        while i < len(self.tree):
            self.tree[i] += value
            i += i & -i
        
    def query(self, i: int):
        i += 1
        result = 0
        while i > 0:
            result += self.tree[i]
            i -= i & -i
        return result

class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        e = { v: i for i, v in enumerate(sorted(set(nums))) }
        bit = BinaryIndexTree(len(e))
        indexes = [e[n] for n in nums]
        result = []
        for i in reversed(indexes):
            count = bit.query(i)
            result.append(count)
            bit.update(i+1, 1)
        return result[::-1]