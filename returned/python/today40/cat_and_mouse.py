# https://leetcode.com/problems/cat-and-mouse/description/
from typing import List


class Solution:
    def catMouseGame(self, graph: List[List[int]]) -> int:
        cat_visited = set([2])
        mouse_visited = set([1])

        def dfs(cat, mouse, mouses_turn):
            if mouse == 0:
                return 1
            if cat == mouse:
                return 2
            if mouses_turn and mouse in mouse_visited:
                return 0
            if not mouses_turn and cat in cat_visited:
                return 0

            if mouses_turn:
                move = graph[mouse][0]
                for option in graph[mouse]:
                    if option != cat:
                        move = option
                    elif option not in mouse_visited:
                        move = option
                mouse_visited.add(move)
                return dfs(cat, move, False)
            else:
                move = graph[cat][0]
                cat_visited.add(move)
                return dfs(move, mouse, True)

        return dfs(2, 1, True)
