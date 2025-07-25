from longest_substring_with_at_least_k_repeating_characters import Solution

def test1():
    assert Solution().longestSubstring('aaabb', 3) == 3

def test2():
    assert Solution().longestSubstring('ababbc', 2) == 5