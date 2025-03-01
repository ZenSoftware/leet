from wiggle_sort_ii import Solution

def test1():
    input = [1,5,1,1,6,4]
    Solution().wiggleSort(input)
    assert input == [1, 6, 1, 5, 1, 4]