# https://leetcode.com/problems/binary-tree-paths/description/
from typing import Optional, List

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []

        def dfs(root: Optional[TreeNode], path: List[str]):
            if not root:
                return
            path.append(str(root.val))
            if root.left == None and root.right == None:
                result.append('->'.join(path))
            dfs(root.left, path)
            dfs(root.right, path)
            path.pop()

        dfs(root, [])
        return result