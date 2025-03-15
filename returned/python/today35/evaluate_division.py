# https://leetcode.com/problems/evaluate-division/
from typing import List
from collections import deque, defaultdict

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        edges = defaultdict(list)
        for i, eq in enumerate(equations):
            edges[eq[0]].append((eq[1], i))
            edges[eq[1]].append((eq[0], i))

        def bfs(query: List[str]) -> List[str]:
            previous = {}            
            queue = deque([query[0]])
            while queue:
                current = queue.popleft()
                if current == query[1]:
                    break
                for adj, i in edges[current]:
                    if adj not in previous:
                        queue.append(adj)
                        previous[adj] = (current, i)
            
            if current != query[1]:
                return []
            
            path = []
            while current != query[0]:
                parent, eqIndex = previous[current]
                path.append(eqIndex)
                current = parent
            return path[::-1]
    
        def solve(query: List[str], path: List[int]) -> int:
            if not path:
                if query[0] == query[1] and query[0] in edges:
                    return 1.0
                return -1.0
            ans = 1
            current = query[0]
            for i in path:
                if current == equations[i][0]:
                    ans *= values[i]
                    current = equations[i][1]
                else:
                    ans /= values[i]
                    current = equations[i][0]
            return ans

        result = []
        for query in queries:
            path = bfs(query)
            result.append(solve(query, path))
        return result