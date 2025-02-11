# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root: TreeNode, path: List[int]) -> None:
            path.append(root.val)
            if root.left == None and root.right == None:
                nonlocal total
                total += int("".join([str(x) for x in path]))
            if root.left:
                dfs(root.left, path)
            if root.right:
                dfs(root.right, path)
            path.pop()
        dfs(root, [])
        return total