# https://leetcode.com/problems/path-sum-ii/description/
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:
            return []
        
        result = []
        def dfs(node: Optional[TreeNode], sum: int, path: List[int]) -> None:
            if node.left == None and node.right == None and sum - node.val == 0:
                result.append(path + [node.val])
            
            path.append(node.val)
            if node.left:
                dfs(node.left, sum-node.val, path)
            if node.right:
                dfs(node.right, sum-node.val, path)
            path.pop()
        
        dfs(root, targetSum, [])
        return result