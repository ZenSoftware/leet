from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def height_far_left(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return height_far_left(node.left) + 1
        
        def height_far_right(node: Optional[TreeNode]) -> int:
            if not node:
                return 0
            return height_far_right(node.right) + 1
        
        left_height = height_far_left(root)
        right_height = height_far_right(root)
        
        if left_height == right_height:
            return 2 ** left_height - 1
        else:
            return 1 + self.countNodes(root.left) + self.countNodes(root.right)