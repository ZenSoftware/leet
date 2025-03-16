# https://leetcode.com/problems/binary-watch/description/
from typing import Counter, List

class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        result = []
        for h in range(12):
            for m in range(60):
                hour = '{0:b}'.format(h)
                hour_bits = Counter(hour)['1']

                minutes = '{0:b}'.format(m)
                minutes_bits = Counter(minutes)['1']
                
                if hour_bits + minutes_bits == turnedOn:
                    time = '{0}:{1:02d}'.format(h, m)
                    result.append(time)
        return result