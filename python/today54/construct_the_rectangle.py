# https://leetcode.com/problems/construct-the-rectangle/description/
from typing import List
from math import sqrt, ceil, floor


class Solution:
    def constructRectangle(self, area: int) -> List[int]:
        ideal = ceil(sqrt(area))
        while ideal < area:
            if (area % ideal) == 0:
                return [ideal, floor(area / ideal)]
            ideal += 1
        return [area, 1]
