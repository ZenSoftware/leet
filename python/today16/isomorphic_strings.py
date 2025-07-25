# https://leetcode.com/problems/isomorphic-strings/description/

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        s_cache = dict()
        t_cache = dict()
        
        for i in range(len(s)):
            if s[i] in s_cache:
                if t[i] != s_cache[s[i]]:
                    return False
            else:
                s_cache[s[i]] = t[i]
            
            if t[i] in t_cache:
                if s[i] != t_cache[t[i]]:
                    return False
            else:
                t_cache[t[i]] = s[i]

        return True
