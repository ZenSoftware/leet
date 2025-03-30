# https://leetcode.com/problems/path-sum-iii/description/
from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        paths = 0
        pathSums = defaultdict(int)
        pathSums[0] = 1

        def dfs(root, cur):
            if not root:
                return

            cur += root.val
            nonlocal paths
            paths += pathSums[cur - targetSum]

            pathSums[cur] += 1
            dfs(root.left, cur)
            dfs(root.right, cur)
            pathSums[cur] -= 1

        dfs(root, 0)
        return paths
