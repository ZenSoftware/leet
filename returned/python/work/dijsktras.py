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
        curDistance, curNode = heappop(heap)
        if curNode == end:
            break
        if curNode in visited:
            continue
        visited.add(curNode)
        for edgeDistance, neighbor in curNode.adjacent:
            distance = curDistance + edgeDistance
            if neighbor not in visited and distance < distances[neighbor]:
                distances[neighbor] = distance
                predecessors[neighbor] = curNode
                heappush(heap, (distance, neighbor))
    
    path = []
    curNode = end
    while curNode != start:
        path.append(predecessors[curNode])
        curNode = predecessors[curNode]
    path.append(start)
    return (distances[end], path[::-1])
