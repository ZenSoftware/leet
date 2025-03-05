# https://leetcode.com/problems/self-crossing/description/
from typing import List

class Solution:
    def isSelfCrossing(self, d: List[int]) -> bool:
        for i in range(3, len(d)):
            if d[i] >= d[i-2] and d[i-1] <= d[i-3]:
                return True
            if i >= 4:
                if (d[i] + d[i-4]) >= d[i-2] and d[i-3] == d[i-1]:
                    return True
            if i >= 5:
                if (d[i-4] + d[i]) >= d[i-2] and d[i-2] > d[i-4] and (d[i-1] + d[i-5]) >= d[i-3] and d[i-1] < d[i-3]:
                    return True
        return False