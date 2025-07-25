# https://leetcode.com/problems/restore-ip-addresses/
from typing import List

class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        result = []

        def backtrack(i: int, address: List[str]):
            if len(address) == 4:
                if i == len(s):
                    result.append(".".join(address))
                return
            if i >= len(s):
                return

            address.append(s[i])
            backtrack(i+1, address)
            address.pop()
            
            if s[i] != '0':
                if i+2 <= len(s):
                    address.append(s[i:i+2])
                    backtrack(i+2, address)
                    address.pop()

                if i+3 <= len(s) and int(s[i:i+3]) <= 255:
                    address.append(s[i:i+3])
                    backtrack(i+3, address)
                    address.pop()
        
        backtrack(0, [])
        return result