from best_time_to_buy_and_sell_stock_attempt2 import Solution


def test1():
    assert Solution().maxProfit([7, 1, 5, 3, 6, 4]) == 5


def test2():
    assert Solution().maxProfit([7, 6, 4, 3, 1]) == 0
