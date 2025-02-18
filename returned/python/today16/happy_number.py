# https://leetcode.com/problems/happy-number/description/

class Solution:
    def isHappy(self, n: int) -> bool:
        visited = set()
        while n != 1:
            val = 0
            while n != 0:
                val += (n % 10) ** 2
                n //= 10
            n = val
            if n in visited:
                return False
            visited.add(n)
        return True