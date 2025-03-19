# https://leetcode.com/problems/n-ary-tree-level-order-traversal/description/
from typing import List, Optional
from collections import deque

class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return []
        queue = deque()
        queue.append(root)
        result = []
        while queue:
            level = []
            for _ in range(len(queue)):
                current = queue.popleft()
                level.append(current.val)
                for child in current.children:
                    queue.append(child)
            result.append(level)
        return result
