from group_anagrams_attempt2 import Solution


def test1():
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
    result = Solution().groupAnagrams(strs)
    assert result == [["eat", "tea", "ate"], ["tan", "nat"], ["bat"]]


def test2():
    strs = [""]
    result = Solution().groupAnagrams(strs)
    assert result == [[""]]


def test3():
    strs = ["a"]
    result = Solution().groupAnagrams(strs)
    assert result == [["a"]]
