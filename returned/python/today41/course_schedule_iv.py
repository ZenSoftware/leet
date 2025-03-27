# https://leetcode.com/problems/course-schedule-iv/description/
from typing import List
from collections import defaultdict
from functools import cache


class Solution:
    """
    Time: O(n^3)
    Space: O(n^2)
    """

    def checkIfPrerequisite(
        self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]
    ) -> List[bool]:
        graph = defaultdict(set)
        for prereq, course in prerequisites:
            graph[course].add(prereq)

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
