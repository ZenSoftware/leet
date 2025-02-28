# https://leetcode.com/problems/minimum-height-trees/
from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        if n == 1:
            return [0]
        
        adjacencies = defaultdict(list)
        for a, b in edges:
            adjacencies[a].append(b)
            adjacencies[b].append(a)

        edge_count = {}
        leaves = deque()
        for source, neighbors in adjacencies.items():
            if len(neighbors) == 1:
                leaves.append(source)
            edge_count[source] = len(neighbors)

        while leaves:
            if n <= 2:
                return list(leaves)
            for _ in range(len(leaves)):
                leaf = leaves.popleft()
                n -= 1
                for neighbor in adjacencies[leaf]:
                    edge_count[neighbor] -= 1
                    if edge_count[neighbor] == 1:
                        leaves.append(neighbor)
                