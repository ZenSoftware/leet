from insert_delete_get_random_o_1_attempt2 import RandomizedSet


def test1():
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(1) == True
    assert randomizedSet.remove(2) == False
    assert randomizedSet.insert(2) == True
    ran = randomizedSet.getRandom()
    assert ran == 1 or ran == 2
    assert randomizedSet.remove(1) == True
    assert randomizedSet.insert(2) == False
    assert randomizedSet.getRandom() == 2


def test2():
    # ["RandomizedSet","insert","insert","remove","insert","remove","getRandom"]
    # [       [],         [0],     [1],     [0],     [2],     [1],      []]
    # [       null,       true,    true,    true,    true,    true,      2]
    randomizedSet = RandomizedSet()
    assert randomizedSet.insert(0) == True
    assert randomizedSet.insert(1) == True
    assert randomizedSet.remove(0) == True
    assert randomizedSet.insert(2) == True
    assert randomizedSet.remove(1) == True
    assert randomizedSet.getRandom() == 2
