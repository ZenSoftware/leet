# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        result = float('inf')
        
        def calcMin(node: Optional[TreeNode], depth: int) -> None:
            if node.left == None and node.right == None:
                nonlocal result
                result = min(result, depth)
                return
            
            if depth > result:
                return

            if node.left:
                calcMin(node.left, depth+1)
            
            if node.right:
                calcMin(node.right, depth+1)
            
        calcMin(root, 1)
        return result