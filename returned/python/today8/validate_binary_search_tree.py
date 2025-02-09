# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        def valid(node, left, right):
            if not node:
                return True
            if not (left < node.val < right):
                return False
            
            left_valid = valid(node.left, left, node.val)
            right_valid = valid(node.right, node.val, right)
            return left_valid and right_valid
        return valid(root, float('-inf'), float('inf'))