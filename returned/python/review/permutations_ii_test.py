from permutations_ii import Solution

def test1():
    result = Solution().permuteUnique([1,1,2])
    assert result == [[1,1,2],[1,2,1],[2,1,1]]

def test2():
    result = Solution().permuteUnique([1,2,3])
    assert result == [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]