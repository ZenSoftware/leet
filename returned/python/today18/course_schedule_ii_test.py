from course_schedule_ii import Solution

def test1():
    assert Solution().findOrder(2, [[1,0]]) == [0,1]

def test2():
    assert Solution().findOrder(4, [[1,0],[2,0],[3,1],[3,2]]) == [0, 1, 2, 3]

def test3():
    assert Solution().findOrder(1, []) == [0]