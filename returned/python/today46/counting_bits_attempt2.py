# https://leetcode.com/problems/counting-bits/description/
from typing import List


class Solution:
    """
    Time: O(n)
    Space: O(1)

    Multiplying a number by 2 conserves the number of bits in the number
    1 (001) -> 2 (010) -> 4(100)
    Alternatively, the number of bits in a number will be the same as
    the number of bits in half that number. (right bit shift by 1)

    In the case the number is odd, there will be 1 more bit than
    the number of bits in half that number
    2 (010) -> 5 (011)
    """

    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        for i in range(n + 1):
            result[i] = result[i >> 1] + (i & 1)
        return result
