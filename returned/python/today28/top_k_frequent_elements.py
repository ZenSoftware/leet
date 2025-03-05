# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = defaultdict(int)
        for n in nums:
            counter[n] += 1

        nums_sorted = sorted(counter.items(), key=lambda x: x[1], reverse=True)
        nums_sorted = [k for k,v in nums_sorted]
        return nums_sorted[:k]