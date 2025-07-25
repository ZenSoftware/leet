# https://leetcode.com/problems/loud-and-rich/description/
from typing import List
from collections import defaultdict, deque


class Solution:
    def loudAndRich(self, richer: List[List[int]], quiet: List[int]) -> List[int]:
        n = len(quiet)
        graph = defaultdict(set)
        indegree = [0] * n
        for a, b in richer:
            graph[a].add(b)
            indegree[b] += 1

        queue = deque()
        for i, degree in enumerate(indegree):
            if degree == 0:
                queue.append(i)

        answer = list(range(n))
        while queue:
            node = queue.popleft()

            for neighbor in graph[node]:
                if quiet[answer[node]] < quiet[answer[neighbor]]:
                    answer[neighbor] = answer[node]

                indegree[neighbor] -= 1
                if indegree[neighbor] == 0:
                    queue.append(neighbor)

        return answer
