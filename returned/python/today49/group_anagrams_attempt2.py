# https://leetcode.com/problems/group-anagrams/description/
from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list)
        for s in strs:
            key = "".join(sorted(s))
            result[key].append(s)
        return list(result.values())
