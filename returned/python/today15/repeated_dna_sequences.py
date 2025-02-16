# https://leetcode.com/problems/repeated-dna-sequences/description/
from typing import List
from collections import defaultdict

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hash = defaultdict(int)

        for i in range(len(s) - 9):
            hash[s[i:i+10]] += 1
        
        result = []
        for seq, count in hash.items():
            if count >= 2:
                result.append(seq)
        
        return result