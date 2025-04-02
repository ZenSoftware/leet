# https://leetcode.com/problems/delete-node-in-a-bst/description/
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        if not root:
            return root

        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None and root.right is None:
                return None
            elif root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                successor = self.get_successor(root.right)
                self.deleteNode(root, successor.val)
                root.val = successor.val

        return root

    def get_successor(self, root: TreeNode) -> TreeNode:
        if not root.left:
            return root
        return self.get_successor(root.left)
