# https://leetcode.com/problems/find-largest-value-in-each-tree-row/description/
from collections import deque


class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution(object):
    def largestValues(self, root):
        if not root:
            return []

        result = []
        queue = deque([root])
        while queue:
            largest = float("-inf")
            for node in queue:
                if node.val > largest:
                    largest = node.val
            result.append(largest)

            for _ in range(len(queue)):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

        return result
