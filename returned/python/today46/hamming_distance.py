# https://leetcode.com/problems/hamming-distance/description/


class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        return (x ^ y).bit_count()
