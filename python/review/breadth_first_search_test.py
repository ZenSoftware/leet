from breadth_first_search import bfs, Node

def test1():
    a = Node(1)
    b = Node(2)
    c = Node(3)
    d = Node(4)
    e = Node(5)
    f = Node(6)
    g = Node(7)

    a.left = b
    a.right = c
    b.left = d
    b.right = e
    c.left = f
    c.right = g

    assert bfs(a) == [[1], [2, 3], [4, 5, 6, 7]]