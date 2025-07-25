from palindrome_pairs import Solution

def test1():
    assert Solution().palindromePairs(["abcd","dcba","lls","s","sssll"]) == [[0,1],[1,0],[3,2],[2,4]]

def test2():
    assert Solution().palindromePairs(["bat","tab","cat"]) == [[0,1],[1,0]]

def test3():
    assert Solution().palindromePairs(["a",""]) == [[0,1],[1,0]]
