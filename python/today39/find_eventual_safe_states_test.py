from find_eventual_safe_states import Solution


def test1():
    graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    assert Solution().eventualSafeNodes(graph) == [2, 4, 5, 6]


def test2():
    graph = [[1, 2, 3, 4], [1, 2], [3, 4], [0, 4], []]
    assert Solution().eventualSafeNodes(graph) == [4]
