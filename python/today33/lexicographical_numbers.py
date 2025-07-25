# https://leetcode.com/problems/lexicographical-numbers/description/
from typing import List

class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        res = []

        def dfs(cur: int):
            if cur > n:
                return False
            res.append(cur)
            cur *= 10
            for i in range(10):
                if not dfs(cur + i):
                    break
            return True
        
        for i in range(1,10):
            dfs(i)
        return res