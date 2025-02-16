from largest_number import Solution

def test1():
    assert Solution().largestNumber([10,2]) == '210'

def test2():
    assert Solution().largestNumber([3,30,34,5,9]) == '9534330'

def test3():
    assert Solution().largestNumber([34323,3432]) == '343234323'

def test4():
    assert Solution().largestNumber([0,0]) == '0'

