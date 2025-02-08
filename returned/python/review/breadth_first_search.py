from typing import List
from collections import deque

class Node:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right= right

def bfs(root: Node) -> List[int]:
    result = []
    stack = deque()
    stack.append(root)

    while stack:
        level_size = len(stack)
        level_vals = []
        for _ in range(level_size):
            node = stack.popleft()
            level_vals.append(node.val)
            if node.left:
                stack.append(node.left)
            if node.right:
                stack.append(node.right)
        result.append(level_vals)
    
    return result

if __name__ == '__main__':
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    result = bfs(a)
    print(result)