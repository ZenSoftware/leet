# https://leetcode.com/problems/flatten-binary-tree-to-linked-list/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def flatten(self, root: Optional[TreeNode]) -> None:
        if not root:
            return None

        nodes = []
        def dfs(node: Optional[TreeNode]) -> None:
            nodes.append(node)

            if node.left:
                dfs(node.left)

            if node.right:
                dfs(node.right)
        
        dfs(root)

        for i in range(len(nodes)-1):
            nodes[i].left = None
            nodes[i].right = nodes[i+1]
        
        return nodes[0]