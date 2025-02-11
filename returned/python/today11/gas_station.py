# https://leetcode.com/problems/gas-station/
from typing import List

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        total_gas = 0
        for g in gas:
            total_gas += g

        total_cost = 0
        for c in cost:
            total_cost += c
        
        if total_gas - total_cost < 0:
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