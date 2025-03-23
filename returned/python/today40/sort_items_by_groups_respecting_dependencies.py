# https://leetcode.com/problems/sort-items-by-groups-respecting-dependencies/description/
from typing import List
from collections import deque, defaultdict


class Solution:
    def sortItems(
        self, n: int, m: int, group: List[int], beforeItems: List[List[int]]
    ) -> List[int]:

        def topo_sort(nodes, graph, indegree):
            queue = deque([node for node in nodes if node not in indegree])
            res = []
            while queue:
                cur = queue.popleft()
                res.append(cur)
                for adj in graph[cur]:
                    indegree[adj] -= 1
                    if indegree[adj] == 0:
                        queue.append(adj)
            return res

        # Ensure items with no group have unique ids
        item_groups = defaultdict(list)
        group_id = m
        for i in range(n):
            if group[i] == -1:
                group[i] = group_id
                group_id += 1

        item_graph = defaultdict(list)
        item_indegree = defaultdict(int)

        # u is a dependency of v
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] == group[v]:
                    item_graph[u].append(v)
                    item_indegree[v] += 1

        for i, g in enumerate(group):
            item_groups[g].append(i)

        sorted_items = defaultdict(list)
        for g, item_group in item_groups.items():
            sorted_items[g] = topo_sort(item_group, item_graph, item_indegree)
            if len(item_group) != len(sorted_items[g]):
                return []

        group_graph = defaultdict(list)
        group_indegree = defaultdict(int)

        # u is a dependency of v
        for v, u_list in enumerate(beforeItems):
            for u in u_list:
                if group[u] != group[v]:
                    group_graph[group[u]].append(group[v])
                    group_indegree[group[v]] += 1

        sorted_groups = topo_sort(range(group_id), group_graph, group_indegree)
        if len(sorted_groups) != len(range(group_id)):
            return []

        result = []
        for g in sorted_groups:
            result.extend(sorted_items[g])

        return result
