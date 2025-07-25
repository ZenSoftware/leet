from minimum_number_of_arrows_to_burst_balloons import Solution


def test1():
    balloons = [[10, 16], [2, 8], [1, 6], [7, 12]]
    assert Solution().findMinArrowShots(balloons) == 2


def test2():
    balloons = [[1, 2], [3, 4], [5, 6], [7, 8]]
    assert Solution().findMinArrowShots(balloons) == 4


def test3():
    balloons = [[1, 2], [2, 3], [3, 4], [4, 5]]
    assert Solution().findMinArrowShots(balloons) == 2
