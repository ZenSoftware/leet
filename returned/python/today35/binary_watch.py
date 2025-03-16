# https://leetcode.com/problems/binary-watch/description/
from typing import List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                hour_bits = bin(h).count('1')
                minute_bits = bin(m).count('1')
                if hour_bits + minute_bits == turnedOn:
                    time = '{0}:{1:02d}'.format(h, m)
                    result.append(time)
        return result