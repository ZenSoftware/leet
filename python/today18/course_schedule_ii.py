# https://leetcode.com/problems/course-schedule-ii/
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = { c:[] for c in range(numCourses) }
        for course, prereq in prerequisites:
            graph[course].append(prereq)
        
        output = []
        visited, cycle = set(), set()
        def dfs(course: int): 
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)
            for prereq in graph[course]:
                if dfs(prereq) == False:
                    return False
            cycle.remove(course)
            visited.add(course)
            output.append(course)
            return True
        
        for c in range(numCourses):
            if dfs(c) == False:
                return []
        return output