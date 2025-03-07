# https://leetcode.com/problems/minimum-cost-for-tickets/description/
from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        memo = {}
        
        def binary_search(start: int, ticket_days: int) -> int:
            target = days[start] + ticket_days
            l = start
            r = min(start+ticket_days, len(days)-1)
            while l <= r:
                m = (l + r) // 2
                if target < days[m]:
                    r = m - 1
                elif target > days[m]:
                    l = m + 1
                else:
                    return m
            return l
        
        def dfs(i: int, total) -> int:
            if (i, total) in memo:
                return memo[(i, total)]
            
            if i >= len(days):
                return total

            one_day = dfs(i+1, total+costs[0])
            
            next_index = binary_search(i, 7)
            seven_day = dfs(next_index, total+costs[1])

            next_index = binary_search(i, 30)
            thirty_day = dfs(next_index, total+costs[2])

            memo[(i,total)] = min(one_day, seven_day, thirty_day)
            return memo[(i, total)]

        return dfs(0, 0)