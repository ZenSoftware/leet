from typing import List

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        eval = triangle[len(triangle)-1]
        for row in range(len(triangle)-2, -1, -1):
            next = []
            for col in range(0, len(triangle[row])):
                 smallest = triangle[row][col] + min(eval[col], eval[col+1])
                 next.append(smallest)
            eval = next
        return eval[0]