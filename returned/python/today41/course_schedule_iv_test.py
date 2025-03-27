from course_schedule_iv import Solution


def test1():
    result = Solution().checkIfPrerequisite(2, [[1, 0]], [[0, 1], [1, 0]])
    assert result == [False, True]


def test2():
    result = Solution().checkIfPrerequisite(2, [], [[1, 0], [0, 1]])
    assert result == [False, False]


def test3():
    result = Solution().checkIfPrerequisite(
        3, [[1, 2], [1, 0], [2, 0]], [[1, 0], [1, 2]]
    )
    assert result == [True, True]
