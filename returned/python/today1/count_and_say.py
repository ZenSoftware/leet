# https://leetcode.com/problems/count-and-say/description/

class Solution:
    def countAndSay(self, n: int) -> str:
        def rle(chars: str, s: int) -> str:
            if s == n:
                return chars
            output = ''
            current = chars[0]
            count = 0
            for c in chars:
                if c == current:
                    count += 1
                else:
                    output += str(count) + current
                    current = c
                    count = 1
            output += str(count) + current
            return rle(output, s+1)
        return rle('1',1)
