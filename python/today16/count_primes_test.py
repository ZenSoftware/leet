from count_primes import Solution

def test1():
    assert Solution().countPrimes(10) == 4

def test2():
    assert Solution().countPrimes(0) == 0

def test3():
    assert Solution().countPrimes(1) == 0