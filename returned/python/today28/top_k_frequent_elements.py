# https://leetcode.com/problems/top-k-frequent-elements/description/
from typing import List
from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        return [n for n,c in Counter(nums).most_common(k)]