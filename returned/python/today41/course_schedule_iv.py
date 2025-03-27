# https://leetcode.com/problems/course-schedule-iv/description/
from typing import List
from collections import defaultdict


class Solution:
    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        cache = defaultdict(set)
        graph = defaultdict(set)
        for a, b in prerequisites:
            graph[b].add(a)

        def dfs(course):
            if course in cache:
                return cache[course]
            prereqs = set([course])
            for adj in graph[course]:
                prereqs.update(dfs(adj))
            cache[course] = prereqs
            return prereqs

        result = []
        for prereq, course in queries:
            result.append(prereq in dfs(course))
        return result
