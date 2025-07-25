# https://leetcode.com/problems/find-eventual-safe-states/description/
from typing import List


class Solution:
    """
    Time: O(E + V)
    Space: O(n)
    """

    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        safe_cache = {}

        def dfs(i):
            if i in safe_cache:
                return safe_cache[i]
            safe_cache[i] = False
            for adj in graph[i]:
                if not dfs(adj):
                    return False
            safe_cache[i] = True
            return True

        result = []
        for i in range(len(graph)):
            if dfs(i):
                result.append(i)
        return result
