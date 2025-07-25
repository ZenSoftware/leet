from island_perimeter import Solution


def test1():
    grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
    assert Solution().islandPerimeter(grid) == 16


def test2():
    grid = [[1]]
    assert Solution().islandPerimeter(grid) == 4


def test3():
    grid = [[1, 0]]
    assert Solution().islandPerimeter(grid) == 4
