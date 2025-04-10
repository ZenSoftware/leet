from three_sum_attemp2 import Solution


def test1():
    assert Solution().threeSum([-1, 0, 1, 2, -1, -4]) == [[-1, -1, 2], [-1, 0, 1]]


def test2():
    assert Solution().threeSum([0, 1, 1]) == []


def test3():
    assert Solution().threeSum([0, 0, 0]) == [[0, 0, 0]]


def test4():
    nums = [2, -3, 0, -2, -5, -5, -4, 1, 2, -2, 2, 0, 2, -4, 5, 5, -10]
    result = Solution().threeSum(nums)
    assert result == [
        [-10, 5, 5],
        [-5, 0, 5],
        [-4, 2, 2],
        [-3, -2, 5],
        [-3, 1, 2],
        [-2, 0, 2],
    ]


def test5():
    nums = [-2, 0, 1, 1, 2]
    result = Solution().threeSum(nums)
    assert result == [[-2, 0, 2], [-2, 1, 1]]
