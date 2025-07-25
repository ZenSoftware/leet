# https://leetcode.com/problems/recover-binary-search-tree/description/
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        prev = None
        firstWrong = None
        secondWrong = None
        def inOrder(node: Optional[TreeNode]) -> None:
            nonlocal prev, firstWrong, secondWrong

            if node.left:
                inOrder(node.left)

            if prev and prev.val > node.val:
                if firstWrong:
                    secondWrong = node
                    return
                else:
                    firstWrong = prev
                    secondWrong = node
            prev = node

            if node.right:
                inOrder(node.right)

        inOrder(root)
        firstWrong.val, secondWrong.val = secondWrong.val, firstWrong.val