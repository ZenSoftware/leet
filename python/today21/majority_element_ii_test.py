from majority_element_ii import Solution

def test1():
    assert Solution().majorityElement([3,2,3]) == [3]

def test2():
    assert Solution().majorityElement([1]) == [1]

def test3():
    assert Solution().majorityElement([1,2]) == [1,2]