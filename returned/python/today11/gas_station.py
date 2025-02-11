# https://leetcode.com/problems/gas-station/
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) - sum(cost) < 0:
            return -1
        
        for i in range(len(gas) - 1):
            tank = gas[i]
            for j in range(i, len(gas) - 1):
                if tank - cost[j] >= 0:
                    tank = tank - cost[j] + gas[j+1]
                else:
                    break
                if j == len(gas) - 2:
                    return i
        
        return len(gas) - 1