from edit_distance import Solution

def test1():
    assert Solution().minDistance('horse', 'ros') == 3

def test2():
    assert Solution().minDistance('intention', 'execution') == 5