from random_pick_index import Solution

def test1():
    rand_pick = Solution([1, 2, 3, 3, 3])
    picked = rand_pick.pick(3)
    assert picked == 2 or picked == 3 or picked == 4