from sort_items_by_groups_respecting_dependencies import Solution


def test1():
    group = [-1, -1, 1, 0, 0, 1, 0, -1]
    beforeItems = [[], [6], [5], [6], [3, 6], [], [], []]
    result = Solution().sortItems(8, 2, group, beforeItems)
    assert result == [0, 5, 2, 6, 3, 4, 7, 1]
