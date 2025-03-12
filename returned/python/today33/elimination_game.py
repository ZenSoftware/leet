# https://leetcode.com/problems/elimination-game/

class Solution:
    def lastRemaining(self, n: int) -> int:
        arr = [i for i in range(1,n+1)]
        left_to_right = True
        while len(arr) > 1:
            if left_to_right:
                arr = [arr[i] for i in range(1, len(arr), 2)]
            else:
                arr = [arr[i] for i in reversed(range(len(arr)-2, -1, -2))]
            left_to_right = not left_to_right
        return arr[0]