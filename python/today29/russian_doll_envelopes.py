# https://leetcode.com/problems/russian-doll-envelopes/
from typing import List

class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        envelopes.sort(key=lambda x: (x[0], -x[1]))
        LIS = [1] * len(envelopes)
        for i in reversed(range(len(envelopes))):
            for j in range(i+1, len(envelopes)):
                if envelopes[i][1] < envelopes[j][1]:
                    LIS[i] = max(LIS[i], 1 + LIS[j])
        return max(LIS)