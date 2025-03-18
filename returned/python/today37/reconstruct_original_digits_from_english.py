# https://leetcode.com/problems/reconstruct-original-digits-from-english/
from collections import Counter
from typing import Dict

class Solution:
    def countNums(self, s: str) -> Dict[int, int]:
        char_occ = Counter(s)
        num_occ = {}
        
        # z only appears in 'zero'
        num_occ['0'] = char_occ['z']

        # w only appears in 'two'
        num_occ['2'] = char_occ['w']

        # u only appears in 'four'
        num_occ['4'] = char_occ['u']

        # x only appears in 'six'
        num_occ['6'] = char_occ['x']

        # g only appears in 'eight'
        num_occ['8'] = char_occ['g']

        # o appears in 'one', 'two' and 'four'
        num_occ['1'] = char_occ['o'] - num_occ['0'] - num_occ['2'] - num_occ['4']

        # h appears in 'three' and 'eight'
        num_occ['3'] = char_occ['h'] - num_occ['8']

        # f appears in 'five' and 'four'
        num_occ['5'] = char_occ['f'] - num_occ['4']

        # v appears in 'seven' and 'five'
        num_occ['7'] = char_occ['v'] - num_occ['5']

        # n appears in 'nine', 'five', 'six' and 'eight'
        num_occ['9'] = char_occ['i'] - num_occ['5'] - num_occ['6'] - num_occ['8']

        return num_occ

    def originalDigits(self, s: str) -> str:
        return ''.join([digit*count for digit, count in sorted(self.countNums(s).items())])