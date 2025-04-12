from all_o_one_data_structure_attempt2 import AllOne


def test1():
    allOne = AllOne()
    allOne.inc("hello")
    allOne.inc("hello")
    allOne.getMaxKey() == "hello"
    allOne.getMinKey() == "hello"
    allOne.inc("leet")
    allOne.getMaxKey() == "hello"
    allOne.getMinKey() == "leet"
