# https://leetcode.com/problems/course-schedule-iv/description/
from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)

        @cache
        def dfs(course):
            prereqs = set([course])
            for adj in graph[course]:
                prereqs.update(dfs(adj))
            return prereqs

        result = []
        for prereq, course in queries:
            result.append(prereq in dfs(course))
        return result
