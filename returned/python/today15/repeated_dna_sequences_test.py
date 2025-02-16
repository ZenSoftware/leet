from repeated_dna_sequences import Solution

def test1():
    result = Solution().findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT")
    assert result == ["AAAAACCCCC","CCCCCAAAAA"]

def test2():
    result = Solution().findRepeatedDnaSequences("AAAAAAAAAAAAA")
    assert result == ["AAAAAAAAAA"]

def test3():
    result = Solution().findRepeatedDnaSequences("AAAAAAAAAAA")
    assert result == ["AAAAAAAAAA"]