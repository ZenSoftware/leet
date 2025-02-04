from group_anagrams import Solution 

def test1():
    result = Solution().groupAnagrams(["eat","tea","tan","ate","nat","bat"])
    assert result == [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]