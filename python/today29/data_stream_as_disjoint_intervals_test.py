from data_stream_as_disjoint_intervals import SummaryRanges

def test1():
    summaryRanges = SummaryRanges()
    summaryRanges.addNum(1)      # arr = [1]
    assert summaryRanges.getIntervals() == [[1, 1]]
    summaryRanges.addNum(3)      # arr = [1, 3]
    assert summaryRanges.getIntervals() == [[1, 1], [3, 3]]
    summaryRanges.addNum(7)      # arr = [1, 3, 7]
    assert summaryRanges.getIntervals() == [[1, 1], [3, 3], [7, 7]]
    summaryRanges.addNum(2)      # arr = [1, 2, 3, 7]
    assert summaryRanges.getIntervals() == [[1, 3], [7, 7]]
    summaryRanges.addNum(6)      # arr = [1, 2, 3, 6, 7]
    assert summaryRanges.getIntervals() == [[1, 3], [6, 7]]