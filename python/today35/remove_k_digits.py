# https://leetcode.com/problems/remove-k-digits/description/

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        res = []
        for n in num:
            while res and k > 0 and n < res[-1]:
                res.pop()
                k -= 1
            res.append(n)
        
        if k > 0:
            res = res[:len(res)-k]
        
        i = 0
        while i < len(res) and res[i] == '0':
            i += 1
        if i > 0:
            res = res[i:]

        if not res:
            return '0'
        else:
            return ''.join(res)