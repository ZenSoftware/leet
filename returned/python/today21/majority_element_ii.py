# https://leetcode.com/problems/majority-element-ii/description/
from typing import List
from collections import defaultdict

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        cache = defaultdict(int)
        for n in nums:
            cache[n] += 1
        threshold = len(nums) // 3
        result = []
        for n, count in cache.items():
            if count > threshold:
                result.append(n)
        return result
