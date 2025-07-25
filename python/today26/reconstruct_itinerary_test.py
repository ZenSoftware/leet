from reconstruct_itinerary import Solution

def test1():
    input = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    assert Solution().findItinerary(input) == ["JFK","MUC","LHR","SFO","SJC"]

def test2():
    input = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    assert Solution().findItinerary(input) == ["JFK","ATL","JFK","SFO","ATL","SFO"]
    