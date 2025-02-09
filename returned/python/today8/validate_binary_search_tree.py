# https://leetcode.com/problems/validate-binary-search-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        left_valid = self.allLessThan(root, root.left) and self.isValidBST(root.left)
        right_valid = self.allGreaterThan(root, root.right) and self.isValidBST(root.right)
        return left_valid and right_valid
    
    def allGreaterThan(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        if root.val >= node.val:
            return False
        return self.allGreaterThan(root, node.left) and self.allGreaterThan(root, node.right)
    
    def allLessThan(self, root: Optional[TreeNode], node: Optional[TreeNode]) -> bool:
        if not node:
            return True
        if root.val <= node.val:
            return False
        return self.allLessThan(root, node.left) and self.allLessThan(root, node.right)
