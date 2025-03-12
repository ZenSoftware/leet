from first_unique_character_in_a_string import Solution

def test1():
    assert Solution().firstUniqChar('leetcode') == 0

def test2():
    assert Solution().firstUniqChar('loveleetcode') == 2

def test3():
    assert Solution().firstUniqChar('aabb') == -1