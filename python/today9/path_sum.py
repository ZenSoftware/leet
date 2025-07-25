# https://leetcode.com/problems/path-sum/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if not root:
            return False
        
        def dfs(node: Optional[TreeNode], sum: int):
            if node.left == None and node.right == None and sum - node.val == 0:
                return True
            
            can_sum_left = False
            if node.left:
                can_sum_left = dfs(node.left, sum-node.val)
            
            can_sum_right = False
            if node.right:
                can_sum_right = dfs(node.right, sum-node.val)

            return can_sum_left or can_sum_right

        return dfs(root, targetSum)