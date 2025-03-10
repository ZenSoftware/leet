from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        if not root: 
            return True
        
        def check(p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
            if not p and not q:
                return True
            if (not p and q) or (p and not q) or p.val != q.val:
                return False
            return check(p.left, q.right) and check(p.right, q.left)
        
        return check(root.left, root.right)
