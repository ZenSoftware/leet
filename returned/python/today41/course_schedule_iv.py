# https://leetcode.com/problems/course-schedule-iv/description/
from typing import List
from collections import defaultdict, deque


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = defaultdict(list)
        for dependency, dependent in prerequisites:
            graph[dependency].append(dependent)

        def bfs(query: List[int]) -> bool:
            queue = deque([query[0]])
            while queue:
                cur = queue.popleft()
                if cur == query[1]:
                    return True
                queue.extend(graph[cur])
            return False

        result = []
        for query in queries:
            result.append(bfs(query))
        return result
