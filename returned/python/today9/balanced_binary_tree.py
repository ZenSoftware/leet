# https://leetcode.com/problems/balanced-binary-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        result = True

        def tree_height(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            
            left_height = tree_height(node.left)
            right_height = tree_height(node.right)

            nonlocal result
            result = result and abs(left_height - right_height) <= 1

            return 1 + max(left_height, right_height)
        
        tree_height(root)
        return result