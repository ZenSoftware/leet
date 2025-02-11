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
        queue = deque([root])
        while queue:
            level_result = []
            for _ in range(len(queue)):
                next = queue.popleft()
                level_result.append(next.val)
                if next.left:
                    queue.append(next.left)
                if next.right:
                    queue.append(next.right)
            result.append(level_result)
        return result