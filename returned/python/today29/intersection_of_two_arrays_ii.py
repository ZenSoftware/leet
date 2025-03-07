# https://leetcode.com/problems/intersection-of-two-arrays-ii/description/
from typing import List
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        counts1, counts2 = Counter(nums1), Counter(nums2)
        result = []
        for n in set(nums1).intersection(set(nums2)):
            count = min(counts1[n], counts2[n])
            result.extend([n]*count)
        return result