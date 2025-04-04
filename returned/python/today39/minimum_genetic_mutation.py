# https://leetcode.com/problems/minimum-genetic-mutation/description/
from typing import List
from collections import defaultdict, deque


class Solution:
    """
    n = number of genes in the bank
    Time: O(n^2)
    Space: O(n)
    """

    def minMutation(self, startGene: str, endGene: str, bank: List[str]) -> int:
        # A gene is adjacent if it differs by 1 character.
        # startGene may not be in bank, thus start by addinging it to the graph.
        graph = defaultdict(set)
        for gene in bank:
            if self.differ_by(startGene, gene) == 1:
                graph[startGene].add(gene)

        # Construct the rest of the unweighted bi-directional graph
        for i in range(len(bank) - 1):
            for j in range(i + 1, len(bank)):
                if self.differ_by(bank[i], bank[j]) == 1:
                    graph[bank[i]].add(bank[j])
                    graph[bank[j]].add(bank[i])

        # Breadth first search, level order traversal.
        # After each level, increment mutation_count by 1
        queue = deque([startGene])
        visited = set([startGene])
        mutation_count = 0
        while queue:
            for _ in range(len(queue)):
                gene = queue.popleft()
                if gene == endGene:
                    return mutation_count
                for adj in graph[gene]:
                    if adj not in visited:
                        queue.append(adj)
                        visited.add(adj)
            mutation_count += 1

        # We've exhausted our search, thus there is no path to endGene
        return -1

    def differ_by(self, g1: str, g2: str) -> int:
        count = 0
        for i in range(8):
            if g1[i] != g2[i]:
                count += 1
        return count
