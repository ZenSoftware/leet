from minimum_cost_for_tickets import Solution

def test1():
    assert Solution().mincostTickets([1,4,6,7,8,20], [2,7,15]) == 11

def test2():
    assert Solution().mincostTickets([1,2,3,4,5,6,7,8,9,10,30,31], [2,7,15]) == 17