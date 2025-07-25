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
        
        queue = deque([root])
        depth = 1
        while queue:
            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left == None and node.right == None:
                    return depth
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            depth += 1
            
