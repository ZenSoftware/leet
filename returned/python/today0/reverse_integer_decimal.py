class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        x = abs(x)
        result = 0

        while x != 0:
            remainder = x % 10
            result = result * 10 + remainder
            x = x // 10
        
        result *= sign

        if (-2)**31 <= result and result <= 2**31 - 1:
            return result
        
        return 0