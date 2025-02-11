from typing import List

class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0:
            return [1]
        
        prev = [1,1]
        for i in range(2,rowIndex+1):
            next = [1]
            for j in range(0,i-1):
                next.append(prev[j] + prev[j+1])
            next.append(1)
            prev = next

        return prev