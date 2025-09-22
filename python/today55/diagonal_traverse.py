# https://leetcode.com/problems/diagonal-traverse/description/
from typing import List


class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        last_row = len(mat) - 1
        last_col = len(mat[0]) - 1
        up_right = True
        pos = [0, 0]
        result = []

        while not (pos[0] == last_row and pos[1] == last_col):
            result.append(mat[pos[0]][pos[1]])

            if pos[0] == 0 and up_right:
                up_right = not up_right
                if pos[1] == last_col:
                    pos[0] += 1
                else:
                    pos[1] += 1
            elif pos[1] == last_col and up_right:
                up_right = not up_right
                pos[0] += 1
            elif pos[1] == 0 and not up_right:
                up_right = not up_right
                if pos[0] == last_row:
                    pos[1] += 1
                else:
                    pos[0] += 1
            elif pos[0] == last_row and not up_right:
                up_right = not up_right
                pos[1] += 1
            elif up_right:
                pos[0] -= 1
                pos[1] += 1
            else:
                pos[0] += 1
                pos[1] -= 1

        result.append(mat[pos[0]][pos[1]])
        return result
