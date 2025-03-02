from dijsktras import GraphNode, shortest_path

def test1():
    A = GraphNode('A')
    B = GraphNode('B')
    C = GraphNode('C')
    D = GraphNode('D')
    E = GraphNode('E')
    F = GraphNode('F')
    A.adjacent = [(3, B), (20, D), (5, F)]
    B.adjacent = [(9, C), (3, D)]
    C.adjacent = [(30, E), (40, F)]
    D.adjacent = [(25, E)]
    F.adjacent = [(4, B)]
    shortest_path(A, C) == (12, [A, B, C])