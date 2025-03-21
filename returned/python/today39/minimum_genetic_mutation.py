# https://leetcode.com/problems/minimum-genetic-mutation/description/
from typing import List
from collections import defaultdict, deque


class Solution:
    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # Construct unweighted bi-directional graph
        graph = defaultdict(set)
        for gene in bank:
            if self.differ_by(startGene, gene) == 1:
                graph[startGene].add(gene)

        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if self.differ_by(bank[i], bank[j]) == 1:
                    graph[bank[i]].add(bank[j])
                    graph[bank[j]].add(bank[i])

        # Breadth first search
        queue = deque([startGene])
        visited = set([startGene])
        result = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return result
                for adj in graph[gene]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            result += 1

        # We've exhausted our search thus there is no path to endGene
        return -1

    def differ_by(self, g1: str, g2: str) -> int:
        count = 0
        for i in range(8):
            if g1[i] != g2[i]:
                count += 1
        return count
