# https://youtu.be/pLElbKBc4RU?si=D9foyptO8-yLwapt

from collections import defaultdict
from typing import List, Tuple
from heapq import heappop, heappush

class GraphNode:
    def __init__(self, label: str = None):
        self.label = label
        self.adjacent = []

def shortest_path(start: GraphNode, end: GraphNode) -> Tuple[int, List[GraphNode]]:
    distances = defaultdict(lambda: float('inf'))
    predecessors = {}
    visited = set()
    heap = [(0, start)]

    while heap:
        currDistance, currNode = heappop(heap)
        if currNode == end:
            break
        if currNode in visited:
            continue
        visited.add(currNode)
        for edgeDistance, neighbor in currNode.adjacent:
            distance = currDistance + edgeDistance
            if neighbor not in visited and distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = currNode
                heappush(heap, (distance, neighbor))
    
    path = []
    currNode = end
    while currNode != start:
        path.append(predecessors[currNode])
        currNode = predecessors[currNode]
    path.append(start)
    return (distances[end], path[::-1])
