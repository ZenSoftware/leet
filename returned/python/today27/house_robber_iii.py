# https://leetcode.com/problems/house-robber-iii/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def rob(self, root: Optional[TreeNode]) -> int:
        def dfs(root: Optional[TreeNode]) -> List[int]:
            if not root:
                return [0,0]

            leftWithRoot, leftWithoutRoot = dfs(root.left)
            rightWithRoot, rightWithoutRoot = dfs(root.right)
            
            withRoot = root.val + leftWithoutRoot + rightWithoutRoot
            withoutRoot = max(leftWithRoot, leftWithoutRoot) + max(rightWithRoot, rightWithoutRoot)
            return [withRoot, withoutRoot]
        
        withRoot, withoutRoot = dfs(root)
        return max(withRoot, withoutRoot)
