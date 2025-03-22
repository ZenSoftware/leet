# https://leetcode.com/problems/loud-and-rich/description/
from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        graph = defaultdict(set)
        for a, b in richer:
            graph[b].add((quiet[a], a))

        @cache
        def dfs(curr: int) -> List:
            result = set()
            for adj in graph[curr]:
                result.add(adj)
                result.update(dfs(adj[1]))
            return result

        answer = []
        for i in range(len(quiet)):
            richer_than_curr = list(dfs(i))
            richer_than_curr.append((quiet[i], i))
            _, a = min(richer_than_curr)
            answer.append(a)
        return answer
