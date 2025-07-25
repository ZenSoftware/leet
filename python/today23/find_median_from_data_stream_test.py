from find_median_from_data_stream import MedianFinder

def test1():
    medianFinder = MedianFinder()
    medianFinder.addNum(1)    # arr = [1]
    medianFinder.addNum(2)    # arr = [1, 2]
    assert medianFinder.findMedian() == 1.5 # return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3)    # arr[1, 2, 3]
    assert medianFinder.findMedian() == 2.0 # return 2.0
 