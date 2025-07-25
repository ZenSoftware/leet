from typing import List

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        
        result = [[1],[1,1]]

        for i in range(2, numRows):
            next = [1]
            for j in range(0, i-1):
                next.append(result[i-1][j] + result[i-1][j+1])
            next.append(1)
            result.append(next)
            
        return result