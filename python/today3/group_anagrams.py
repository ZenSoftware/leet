# https://leetcode.com/problems/group-anagrams/description/
from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result_dict = {}
        for s in strs:
            char_list = list(s)
            char_list.sort()
            sorted_str = ''.join(char_list)
            if sorted_str in result_dict:
                result_dict[sorted_str].append(s)
            else:
                result_dict[sorted_str] = [s]       
        return list(result_dict.values())