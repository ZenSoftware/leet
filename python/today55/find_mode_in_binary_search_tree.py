# https://leetcode.com/problems/find-mode-in-binary-search-tree/description/
from typing import Optional, List
from collections import deque, defaultdict


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def findMode(self, root: Optional[TreeNode]) -> List[int]:
        counts = defaultdict(int)
        queue = deque()
        if root:
            queue.append(root)

        while queue:
            node: TreeNode = queue.popleft()
            counts[node.val] += 1

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        result = []
        largest = float("-inf")
        for key, value in counts.items():
            if value > largest:
                result = [key]
                largest = value
            elif value == largest:
                result.append(key)
        return result
