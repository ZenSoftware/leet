from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        stack = deque([root])
        while stack:
            level_size = len(stack)
            level_result = []
            for _ in range(level_size):
                next = stack.popleft()
                level_result.append(next.val)
                if next.left:
                    stack.append(next.left)
                if next.right:
                    stack.append(next.right)
            result.append(level_result)
        return result