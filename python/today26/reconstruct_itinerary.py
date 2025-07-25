# https://leetcode.com/problems/reconstruct-itinerary/
from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        paths = []

        def backtrack(path: List[str], remaining: List[List[str]]):
            if len(remaining) == 0:
                paths.append(path.copy())
                return
        
            for i, ticket in enumerate(remaining):
                if path[-1] == ticket[0]:
                    path.append(ticket[1])
                    next_remaining = remaining.copy()
                    del next_remaining[i]
                    backtrack(path, next_remaining)
                    path.pop()
        
        for i, ticket in enumerate(tickets):
            if ticket[0] == 'JFK':
                path = [ticket[0], ticket[1]]
                remaining = tickets.copy()
                del remaining[i]
                backtrack(path, remaining)

        paths.sort()
        return paths[0]