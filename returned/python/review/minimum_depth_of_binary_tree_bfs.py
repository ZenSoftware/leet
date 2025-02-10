# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = deque([root])
        depth = 1
        while stack:
            level_size = len(stack)
            for _ in range(level_size):
                node = stack.popleft()
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    stack.append(node.left)
                if node.right:
                    stack.append(node.right)
            depth += 1
            
