from cat_and_mouse import Solution


def test1():
    graph = [[2, 5], [3], [0, 4, 5], [1, 4, 5], [2, 3], [0, 2, 3]]
    assert Solution().catMouseGame(graph) == 0
