# https://leetcode.com/problems/power-of-three/description/

POWERS_OF_3 = [1, 3, 9, 27, 81, 243, 729, 2187, 6561, 19683, 59049, 177147, 531441, 1594323, 4782969, 14348907, 43046721, 129140163, 387420489, 1162261467]

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            return False
        return n in POWERS_OF_3
    
def compute_largest_power3():
    MAX_INT = (2 ** 31) - 1
    POWERS_OF_3 = []
    i = 0
    while 3 ** i < MAX_INT:
        POWERS_OF_3.append(3 ** i)
        i += 1
    print(POWERS_OF_3)
