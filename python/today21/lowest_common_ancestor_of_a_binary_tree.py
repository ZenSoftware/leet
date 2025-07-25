# https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/description/
from typing import List

class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        p_path = self.getPath(root, p)
        q_path = self.getPath(root, q)

        if len(p_path) >= len(q_path):
            q_set = set(q_path)
            for node in reversed(p_path):
                if node in q_set:
                    return node
        else:
            p_set = set(p_path)
            for node in reversed(q_path):
                if node in p_set:
                    return node

    def getPath(self, root: TreeNode, target: TreeNode) -> List[TreeNode]:
        result = []
        def dfs(node: TreeNode, parents: List[TreeNode]):
            if result:
                return
            
            parents.append(node)

            if node == target:
                result.extend(parents)
                return

            if node.left:
                dfs(node.left, parents)
            if node.right:
                dfs(node.right, parents)
            
            parents.pop()
        dfs(root, [])
        return result