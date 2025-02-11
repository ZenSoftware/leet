# https://leetcode.com/problems/clone-graph/description/
from typing import Optional
from collections import deque

class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return node
        
        visited = {node: Node(node.val)}
        queue = deque([node])
        while queue:
            for _ in range(len(queue)):
                n = queue.popleft()
                for adj in n.neighbors:
                    if adj not in visited:
                        visited[adj] = Node(adj.val)
                        queue.append(adj)

        for n in visited:
            for adj in n.neighbors:
                 visited[n].neighbors.append(visited[adj])
        
        return visited[node]