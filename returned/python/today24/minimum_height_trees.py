# https://leetcode.com/problems/minimum-height-trees/
from typing import List
from collections import defaultdict, deque

class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:
        adjacencies = defaultdict(set)
        for a, b in edges:
            adjacencies[a].add(b)
            adjacencies[b].add(a)
        
        heights = defaultdict(lambda: [])
        
        for i in range(n):
            visited = set([i])
            queue = deque([i])
            height = 1
            while queue:
                for _ in range(len(queue)):
                    node = queue.popleft()
                    adjacent = adjacencies[node].difference(visited)
                    queue.extend(adjacent)
                    visited.update(adjacent)
                height += 1
                if heights and height > min(heights):
                    break
            heights[height].append(i)

        return heights[min(heights)]