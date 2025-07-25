# https://leetcode.com/problems/unique-binary-search-trees-ii/description/
from typing import List, Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        def generate(left: int, right: int) -> List[Optional[TreeNode]]:
            if left > right:
                return [None]

            res = []
            for val in range(left, right+1):
                for left_tree in generate(left, val-1):
                    for right_tree in generate(val+1, right):
                        root = TreeNode(val, left_tree, right_tree)
                        res.append(root)
            return res
        return generate(1, n)
            
