# https://leetcode.com/problems/serialize-and-deserialize-bst/description/
from typing import Optional
from collections import deque


class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        if not root:
            return "null"

        queue = deque([root])
        levels = [[str(root.val)]]

        while queue:
            level = []
            for _ in range(len(queue)):
                cur = queue.popleft()

                if cur.left:
                    level.append(str(cur.left.val))
                    queue.append(cur.left)
                else:
                    level.append("null")

                if cur.right:
                    level.append(str(cur.right.val))
                    queue.append(cur.right)
                else:
                    level.append("null")

            levels.append(level)

        res = []
        for i in range(0, len(levels) - 1):
            res.append(",".join(levels[i]))
        return "|".join(res)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        levels = []
        for str_level in data.split("|"):
            level = []
            for cell in str_level.split(","):
                if cell == "null":
                    level.append(None)
                else:
                    level.append(TreeNode(int(cell)))
            levels.append(level)

        for i in range(len(levels) - 1):
            j = 0
            for cell in levels[i]:
                if cell is not None:
                    cell.left = levels[i + 1][j]
                    j += 1
                    cell.right = levels[i + 1][j]
                    j += 1
                else:
                    j += 2
        return levels[0][0]
