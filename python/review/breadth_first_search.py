from typing import List
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

def bfs(root: Node) -> List[int]:
    result = []
    queue = deque([root])

    while queue:
        level_vals = []
        for _ in range(len(queue)):
            node = queue.popleft()
            level_vals.append(node.val)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)
        result.append(level_vals)
    
    return result
