# https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
from typing import Optional, List
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        result = []
        queue = deque([root])
        left_to_right = True
        while queue:
            level_result = []
            for _ in range(len(queue)):
                next = queue.popleft()
                if next.left:
                    queue.append(next.left)
                if next.right:
                    queue.append(next.right)
                level_result.append(next.val)
            if left_to_right:
                result.append(level_result)
            else:
                result.append(level_result[::-1])
            left_to_right = not left_to_right
        return result