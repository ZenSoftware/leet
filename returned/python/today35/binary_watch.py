# https://leetcode.com/problems/binary-watch/description/
from typing import List

BIT_COUNTS = {}
for i in range(60):
    BIT_COUNTS[i] = bin(i).count('1')

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                if BIT_COUNTS[h] + BIT_COUNTS[m] == turnedOn:
                    time = '{0}:{1:02d}'.format(h, m)
                    result.append(time)
        return result